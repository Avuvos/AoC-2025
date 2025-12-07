from functools import cache
from pathlib import Path


def solve_part1(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]
    n, m = len(grid), len(grid[0])

    def traverse(i: int, j: int) -> int:
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '|':
            return 0
        grid[i][j] = '|'
        if i + 1 == n:
            return 0
        if grid[i + 1][j] == '^':
            return 1 + traverse(i + 1, j + 1) + traverse(i + 1, j - 1)
        return traverse(i + 1, j)

    return traverse(0, m // 2)


def solve_part2(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]
    n, m = len(grid), len(grid[0])

    @cache
    def traverse(i: int, j: int) -> int:
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0
        if i + 1 == n:
            return 1
        if grid[i + 1][j] == '^':
            return traverse(i + 1, j + 1) + traverse(i + 1, j - 1)
        return traverse(i + 1, j)

    return traverse(0, m // 2)


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
