from pathlib import Path
from itertools import groupby
from math import prod


def solve_part1(data: str) -> int:
    grid = [row.split() for row in data.splitlines()]
    n, m = len(grid), len(grid[0])
    operations = grid[-1]
    result = 0
    for col in range(m):
        nums = [int(grid[row][col]) for row in range(n - 1)]
        op = operations[col]
        result += sum(nums) if op == '+' else prod(nums)
    return result


def solve_part2(data: str) -> int:
    lines = data.splitlines()
    max_len = max(len(l) for l in lines)
    grid = [l.ljust(max_len) for l in lines]
    cols = ["".join(row[c] for row in grid) for c in range(max_len)]

    is_separator = lambda col: col.strip() == ""
    blocks = [list(group) for is_sep, group in groupby(cols, key=is_separator) if not is_sep]

    result = 0
    for block in blocks:
        nums = [int("".join(c for c in col[:-1] if c.isdigit()))
                for col in reversed(block) if any(c.isdigit() for c in col)]
        op = next(c[-1] for c in block if c[-1] in "+*")
        result += sum(nums) if op == '+' else prod(nums)

    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
