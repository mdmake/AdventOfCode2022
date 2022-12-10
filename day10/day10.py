def partOne(filename: str):
    x = 1
    cycle = 0
    rez = 0

    ticks = {20, 60, 100, 140, 180, 220}
    with open(filename) as f:
        for line in f:

            if 'noop' in line:
                cycle += 1
                if cycle in ticks:
                    rez += cycle * x

            else:
                _, var = line.strip().split()

                cycle += 1
                if cycle in ticks:
                    rez += cycle * x

                cycle += 1
                if cycle in ticks:
                    rez += cycle * x

                x += int(var)

    print(rez)


def partTwo(filename: str):
    LEN = 40
    x = 1
    cycle = 0
    baseline = ['.'] * LEN
    newline = baseline.copy()
    with open(filename) as f:
        for line in f:
            if 'noop' in line:

                if abs(cycle % LEN - x) < 2:
                    newline[cycle % LEN] = '#'
                cycle += 1
                if cycle % LEN == 0:
                    print(''.join(newline))
                    newline = baseline.copy()

            else:
                _, var = line.strip().split()

                if abs(cycle % LEN - x) < 2:
                    newline[cycle % LEN] = '#'
                cycle += 1
                if cycle % LEN == 0:
                    print(''.join(newline))
                    newline = baseline.copy()

                if abs(cycle % LEN - x) < 2:
                    newline[cycle % LEN] = '#'
                cycle += 1
                if cycle % LEN == 0:
                    print(''.join(newline))
                    newline = baseline.copy()

                x += int(var)


if __name__ == '__main__':
    partOne('input.txt')
    partTwo('input.txt')
