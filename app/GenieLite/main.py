"""AgentCore entrypoint for the Genie Lite contest specimen."""

from collections import OrderedDict
from typing import Any

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

from genie_lite.create_specialist import build_create_tool
from genie_lite.state import GenieState
from model.load import load_model


app = BedrockAgentCoreApp()
log = app.logger

ECHO_SYSTEM_PROMPT = """
You are Echo, the governed conversational bridge for Genie Lite.

Carry the human's intent into specialist work without doing the specialist's
work yourself. For artifact creation, visibly call CREATE through the
route_to_create tool. Reflect the goal accurately, ask only a materially
necessary question, and make the route visible in the return.

Never claim that a proposal is approved, executed, deployed, or verified when
it is not. CREATE cannot grant authority. Human authorization is required for
consequential action. If the human corrects the direction, apply that correction
to the next CREATE brief and say what changed.

Return concise sections named ECHO HEARD, ROUTE, CREATE RETURN, AUTHORITY, and
LIMITS. Do not sell Genie Lite as an "AI friend." Center human authority,
specialist routing, receipts, and recovery.
""".strip()


def _extract_prompt(payload: dict) -> str | list[dict]:
    """Accept a validated harness message list or a plain prompt string."""
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    if "messages" in payload:
        messages = payload["messages"]
        if not isinstance(messages, list):
            raise ValueError("messages must be a list")
        return strip_trailing_tool_use(messages)
    prompt = payload.get("prompt", "")
    if not isinstance(prompt, str):
        raise ValueError("prompt must be a string")
    return prompt


def strip_trailing_tool_use(messages: Any) -> list[dict]:
    """Remove incomplete trailing tool-use blocks before framework invocation."""
    if not isinstance(messages, list):
        raise ValueError("messages must be a list")
    normalized = list(messages)
    while normalized:
        last = normalized[-1]
        if not isinstance(last, dict):
            raise ValueError("each message must be an object")
        content = last.get("content", [])
        if not isinstance(content, list) or not all(isinstance(block, dict) for block in content):
            raise ValueError("message content must be a list of objects")
        without_tool_use = [block for block in content if "toolUse" not in block]
        if len(without_tool_use) == len(content):
            break
        if without_tool_use:
            normalized[-1] = {**last, "content": without_tool_use}
            break
        normalized.pop()
    return normalized


class SessionRuntime:
    """In-process session state; useful state does not imply durable authority."""

    def __init__(self, session_id: str):
        self.state = GenieState(session_id=session_id)
        self.model = load_model()
        self.agent = Agent(
            model=self.model,
            system_prompt=ECHO_SYSTEM_PROMPT,
            tools=[build_create_tool(self.model, self.state)],
        )


def session_factory(max_sessions: int = 128):
    cache: OrderedDict[str, SessionRuntime] = OrderedDict()

    def get_or_create(session_id: str) -> SessionRuntime:
        if session_id in cache:
            cache.move_to_end(session_id)
            return cache[session_id]
        if len(cache) >= max_sessions:
            cache.popitem(last=False)
        cache[session_id] = SessionRuntime(session_id)
        return cache[session_id]

    return get_or_create


get_or_create_session = session_factory()


@app.entrypoint
async def invoke(payload, context):
    session_id = getattr(context, "session_id", "default-session")
    runtime = get_or_create_session(session_id)
    prompt = _extract_prompt(payload)
    if isinstance(prompt, str):
        runtime.state.record_human_input(prompt)
    log.info("Invoking Genie Lite session %s", session_id)
    async for event in runtime.agent.stream_async(prompt):
        if isinstance(event, dict) and "event" in event:
            yield event


if __name__ == "__main__":
    app.run()
