from pathlib import Path


def solve_part1(data: str) -> int:
    operations = data.splitlines()

    position = 50
    result = 0
    for operation in operations:
        direction = operation[0]
        steps = int(operation[1:])

        if direction == "R":
            position = (position + steps) % 100
        elif direction == "L":
            position = (position - steps) % 100
        else:
            raise ValueError("Unexpected direction")

        if position == 0:
            result += 1

    return result


def solve_part2(data: str) -> int:
    operations = data.splitlines()

    position = 50
    result = 0
    for operation in operations:
        direction = operation[0]
        steps = int(operation[1:])
        cycles_count = steps // 100

        if direction == "R":
            position = position + steps
        elif direction == "L":
            position = position - steps
        else:
            raise ValueError("Unexpected direction")

        if position >= 100 or position <= 0:
            result += max(1, cycles_count)
        position = position % 100

    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
