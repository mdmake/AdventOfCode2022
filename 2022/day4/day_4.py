def isIn(l1: int, r1: int, l2: int, r2: int) -> bool:
    if (l1 <= l2 and r1 >= r2) or (l1 >= l2 and r1 <= r2):
        return True
    return False


def isOverlap(l1: int, r1: int, l2: int, r2: int) -> bool:
    if (
            l2 <= l1 <= r2 or
            l2 <= r1 <= r2 or
            l1 <= l2 <= r1 or
            l1 <= r2 <= r1
    ):
        return True
    return False


def partOne(filename: str) -> int:
    s = 0
    with open(filename) as f:
        for line in f:
            s1, s2 = line.strip().split(',')
            l1, r1 = map(int, s1.split('-'))
            l2, r2 = map(int, s2.split('-'))

            if isIn(l1, r1, l2, r2):
                s += 1
    return s


def partTwo(filename: str) -> int:
    s = 0
    with open(filename) as f:
        for line in f:
            s1, s2 = line.strip().split(',')
            l1, r1 = map(int, s1.split('-'))
            l2, r2 = map(int, s2.split('-'))
            if isOverlap(l1, r1, l2, r2):
                s += 1
    return s


if __name__ == '__main__':
    print(partOne('input.txt'))
    print(partTwo('input.txt'))
