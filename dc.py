#!/usr/bin/env python3
"""DC: gerador local de candidatos curtos para usernames do Discord.

A verificação remota é deliberadamente deixada para integrações oficiais do Discord.
O programa não tenta contornar CAPTCHA, autenticação ou rate limits.
"""

from __future__ import annotations

import argparse
import itertools
import json
import string
from pathlib import Path

ALPHABET = string.ascii_lowercase + string.digits


def generate(max_length: int = 3):
    for length in range(1, max_length + 1):
        for chars in itertools.product(ALPHABET, repeat=length):
            yield "".join(chars)


def score(name: str) -> float:
    """Heurística de raridade/atratividade, não disponibilidade real."""
    score = 100 - len(name) * 15
    if len(set(name)) == len(name):
        score += 8
    if any(c.isdigit() for c in name):
        score += 3
    if name[0].isdigit():
        score += 2
    if len(name) == 3 and name[1].isdigit():
        score += 4
    return score


def main():
    parser = argparse.ArgumentParser(description="DC — caçador de nomes curtos para Discord")
    parser.add_argument("--max-length", type=int, choices=(1, 2, 3), default=3)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--output", type=Path, default=Path("candidates.json"))
    args = parser.parse_args()

    candidates = []
    for username in generate(args.max_length):
        candidates.append({"username": username, "score": score(username)})
        if len(candidates) >= args.limit:
            break

    candidates.sort(key=lambda item: (-item["score"], item["username"]))
    args.output.write_text(json.dumps(candidates, indent=2), encoding="utf-8")

    print(f"Gerados {len(candidates)} candidatos em {args.output}")
    print("Nota: score indica apenas raridade/atratividade; não confirma disponibilidade no Discord.")


if __name__ == "__main__":
    main()
