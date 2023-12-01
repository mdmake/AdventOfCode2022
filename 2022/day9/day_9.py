from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def sign(value: int):
    if not value:
        return 0

    return 1 if value > 0 else -1


def getNodePosition(head: Point, tail: Point):
    if head == tail:
        return tail

    dx = head.x - tail.x
    dy = head.y - tail.y

    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail
    return Point(tail.x + sign(dx), tail.y + sign(dy))


def puzzle(filename: str, length: int):
    data = {
        # dir, x, y
        'R': Point(1, 0),
        'L': Point(-1, 0),
        'U': Point(0, 1),
        'D': Point(0, -1),
    }

    current = [Point(0, 0) for _ in range(length)]
    history = set()
    history.add(current[-1])
    with open(filename) as f:
        for line in f:
            direction, steps = line.strip().split()
            for k in range(int(steps)):
                current[0] = Point(
                    current[0].x + data[direction].x,
                    current[0].y + data[direction].y
                )

                for i in range(length - 1):
                    current[i + 1] = getNodePosition(current[i], current[i + 1])

                history.add(current[-1])

    return len(history)


if __name__ == '__main__':
    print(puzzle('input.txt', 2))
    print(puzzle('input.txt', 10))
