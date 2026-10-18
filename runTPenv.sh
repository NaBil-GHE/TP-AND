#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
venv_activate="$script_dir/.venv/bin/activate"

if [[ ! -f "$venv_activate" ]]; then
    printf 'Virtual environment not found: %s\n' "$script_dir/.venv" >&2
    exit 1
fi

cd -- "$script_dir"
source "$venv_activate"
 