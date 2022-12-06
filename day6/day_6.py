from collections import deque


def puzzle(filename: str, lenght: int) -> int:
    with open(filename) as f:
        data = f.readline().strip()

    buffer = deque(maxlen=lenght)
    for i, ch in enumerate(data):
        buffer.append(ch)
        if len(set(buffer)) == lenght:
            return i + 1

    return -1


if __name__ == '__main__':
    print(puzzle('input.txt', 4))
    print(puzzle('input.txt', 14))
