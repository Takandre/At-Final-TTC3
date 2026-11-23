#!/usr/bin/env python3
"""Command-line calculator for two numeric operands."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence


def calculate(first: float, operation: str, second: float) -> float:
    """Calculate an arithmetic operation between two numbers."""
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ValueError("divisão por zero não é permitida")
        return first / second
    raise ValueError(f"operação inválida: {operation}")


def _format_result(result: float) -> str:
    """Avoid trailing .0 for results that are mathematically integral."""
    if result.is_integer():
        return str(int(result))
    return str(result)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calcula uma operação entre dois números."
    )
    parser.add_argument("first", help="primeiro número")
    parser.add_argument(
        "operation",
        choices=("+", "-", "*", "/"),
        help="operação: +, -, * ou /",
    )
    parser.add_argument("second", help="segundo número")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        first = float(args.first)
        second = float(args.second)
    except ValueError as error:
        print(f"erro: operandos devem ser números ({error})", file=sys.stderr)
        return 2

    try:
        result = calculate(first, args.operation, second)
    except ValueError as error:
        print(f"erro: {error}", file=sys.stderr)
        return 1

    print(_format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())