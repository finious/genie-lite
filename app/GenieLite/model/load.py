"""Bedrock model configuration for AWS-sponsored workshop credits."""

from strands.models.bedrock import BedrockModel


NOVA_MODEL_ID = "amazon.nova-pro-v1:0"


def load_model() -> BedrockModel:
    """Return the explicitly selected Amazon Nova Pro model."""
    return BedrockModel(model_id=NOVA_MODEL_ID)
