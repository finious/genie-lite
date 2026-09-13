#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
app_dir="$repo_dir/app/GenieLite"
python_bin="$app_dir/.venv/bin/python"

if [[ ! -x "$python_bin" ]]; then
  python_bin="python3"
fi

echo "== Git state =="
git -C "$repo_dir" status --short --branch

echo "== Credit-free proof tests =="
(
  cd "$app_dir"
  PYTHONDONTWRITEBYTECODE=1 "$python_bin" -m unittest discover -s tests -v
)

echo "== AgentCore schema =="
(
  cd "$repo_dir"
  agentcore validate --json
)

echo "== Model fence =="
grep -n 'amazon.nova-pro-v1:0' "$app_dir/model/load.py"

echo "== Tutorial-default fence =="
if grep -R -n -E 'global\.anthropic|exa\.ai|add_numbers|You are a helpful assistant' \
  "$app_dir" --exclude='uv.lock' --exclude-dir='.venv' --exclude-dir='__pycache__'; then
  echo "ERROR: tutorial/default runtime content remains" >&2
  exit 1
fi

echo "LOCAL CHECK: PASS"
