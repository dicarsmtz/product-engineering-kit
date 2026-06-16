#!/usr/bin/env python3
"""Convert acceptance criteria lines into a Jira ADF bullet list document."""

from __future__ import annotations

import argparse
import json
import sys


def clean_criterion(line: str) -> str:
    line = line.strip()
    for prefix in ("- [ ] ", "- [x] ", "- ", "* "):
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return line


def to_adf(criteria: list[str]) -> dict:
    items = []
    for criterion in criteria:
        text = clean_criterion(criterion)
        if not text:
            continue
        items.append(
            {
                "type": "listItem",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": text}],
                    }
                ],
            }
        )

    return {
        "version": 1,
        "type": "doc",
        "content": [{"type": "bulletList", "content": items}],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert acceptance criteria to Jira ADF JSON."
    )
    parser.add_argument(
        "criteria",
        nargs="*",
        help="Criteria strings. If omitted, criteria are read from stdin.",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    args = parser.parse_args()

    criteria = args.criteria or sys.stdin.read().splitlines()
    indent = 2 if args.pretty else None
    print(json.dumps(to_adf(criteria), indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
