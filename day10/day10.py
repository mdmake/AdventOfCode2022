def partOne(filename: str):
    x = 1
    cycle = 0
    rez = 0
    with open(filename) as f:
        for line in f:

            if 'noop' in line:
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    rez += cycle * x
                    print(cycle, x)

            else:
                _, var = line.strip().split()
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    rez += cycle * x
                    print(cycle, x)
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    rez += cycle * x
                    print(cycle, x)

                x += int(var)

    if cycle in [20, 60, 100, 140, 180, 220]:
        rez += cycle * x
        print(cycle, x)

    return x, cycle, rez


def partTwo(filename: str):
    x = 1
    cycle = 0
    rez = 0
    baseline = ['.'] * 40
    newline = baseline.copy()
    with open(filename) as f:
        for line in f:
            if 'noop' in line:

                if abs(cycle % 40 - x) < 2:
                    newline[cycle % 40] = '#'
                cycle += 1

                if cycle % 40 == 0:
                    print(''.join(newline))
                    newline = baseline.copy()

            else:
                _, var = line.strip().split()
                if abs(cycle % 40 - x) < 2:
                    newline[cycle % 40] = '#'
                cycle += 1

                if cycle % 40 == 0:
                    print(''.join(newline))
                    newline = baseline.copy()


                if abs(cycle % 40 - x) < 2:
                    newline[cycle % 40] = '#'
                cycle += 1

                if cycle % 40 == 0:
                    print(''.join(newline))
                    newline = baseline.copy()

                x += int(var)

    if cycle in [20, 60, 100, 140, 180, 220]:
        rez += cycle * x
        print(cycle, x)

    return x, cycle, rez


if __name__ == '__main__':
    print(partOne('input.txt'))
    print(partTwo('input.txt'))
