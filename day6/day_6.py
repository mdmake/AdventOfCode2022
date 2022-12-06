from collections import deque


def partOne(filename):
    with open(filename) as f:
        data = f.readline().strip()

    buffer = deque(maxlen=14)
    for i, ch in enumerate(data):
        buffer.append(ch)
        if len(set(buffer)) == 14:
            return i+1

    return -1


def partTwo(filename):
    pass


if __name__ == '__main__':
    print(partOne('input.txt'))
    #print(partTwo('input.txt'))
