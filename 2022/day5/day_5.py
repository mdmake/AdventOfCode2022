from typing import List


def constructStack(data: List[List[str]]) -> List[List[str]]:
    stack = [[] for _ in range(9)]

    for item in data[::-1]:
        for i in range(9):
            if item[i]:
                stack[i] += item[i],
    return stack


def puzzle(filename: str, craneModel: int) -> str:
    n = 4
    data = []
    with open(filename) as f:
        for line in f:
            if '[' in line and ']' in line:
                ln = line.strip().replace('[', ' ').replace(']', ' ')
                data.append([ln[i:i + n].strip() for i in range(0, len(line.strip()), n)])

            if '1   2   3   4   5   6   7   8   9' in line:
                stacks = constructStack(data)

            if 'mov' in line:
                command = line.strip().split()
                count = int(command[1])
                src = int(command[3]) - 1
                dst = int(command[5]) - 1

                if craneModel == 9000:
                    for _ in range(count):
                        stacks[dst].append(stacks[src].pop())
                elif craneModel == 9001:
                    items = stacks[src][-count:]
                    stacks[src] = stacks[src][:-count]
                    stacks[dst] += items
                else:
                    raise Exception("The elves don't have a crane like that!!")

    return ''.join([item[-1] for item in stacks])


if __name__ == '__main__':
    print(puzzle('input.txt', 9000))
    print(puzzle('input.txt', 9001))
