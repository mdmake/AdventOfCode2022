from typing import Tuple


def sign(value: int):
    if not value:
        return 0

    return 1 if value > 0 else -1


def getNodePosition(head: Tuple[int, int], tail: Tuple[int, int]):
    if head == tail:
        return tail

    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail
    return tail[0] + sign(head[0] - tail[0]), tail[1] + sign(head[1] - tail[1])


def puzzle(filename: str, length: int):
    data = {
        # dir, x, y
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    current = [(0, 0) for _ in range(length)]
    allpos = set()
    allpos.add(current[-1])
    with open(filename) as f:
        for line in f:
            direction, steps = line.strip().split()
            for k in range(int(steps)):
                delta = data[direction]
                current[0] = tuple(p + d for p, d in zip(current[0], delta))

                for i in range(length - 1):
                    current[i + 1] = getNodePosition(current[i], current[i + 1])

                allpos.add(current[-1])

    return len(allpos)


if __name__ == '__main__':
    print(puzzle('input.txt', 2))
    print(puzzle('input.txt', 10))
