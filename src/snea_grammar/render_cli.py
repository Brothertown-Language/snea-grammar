# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""CLI: render a grammar view from the knowledge base.

    uv run python -m snea_grammar.render_cli --view descriptive [--out PATH]

Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
"""

import argparse
from pathlib import Path

from .render import load_knowledge_base, render_descriptive, render_prescriptive, render_teaching

RENDERERS = {
    "descriptive": render_descriptive,
    "teaching": render_teaching,
    "prescriptive": render_prescriptive,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a grammar view from the knowledge base")
    parser.add_argument("--view", choices=sorted(RENDERERS), required=True)
    parser.add_argument("--out", type=Path, default=None, help="output path (default: stdout)")
    args = parser.parse_args()

    kb = load_knowledge_base()
    document = RENDERERS[args.view](kb)
    if args.out is None:
        print(document)
    else:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(document, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
