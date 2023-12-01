def getOrd(ch):
    if ord('a') <= ord(ch) <= ord('z'):
        return ord(ch) - ord('a') + 1
    # if ord('A')<=ord(ch)<=ord('Z'):
    return ord(ch) - ord('A') + 27


def partOne(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            trancateLine = line.strip()
            n = len(trancateLine) // 2
            s += sum([getOrd(ch) for ch in (set(trancateLine[:n]) & set(set(trancateLine[n:])))])

    return s


def partTwo(filename):

    s = 0
    trancateLine = set()
    with open(filename) as f:
        for i, line in enumerate(f):
            if i%3 == 0:
                s += sum([getOrd(ch) for ch in trancateLine])
                trancateLine = set(line.strip())
            else:
                trancateLine &= set(line.strip())
    s += sum([getOrd(ch) for ch in trancateLine])

    return s


if __name__ == '__main__':
    print(partOne('input.txt'))
    print(partTwo('input.txt'))
