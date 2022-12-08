from typing import List


def readData(filename: str):
    forest = []
    with open(filename) as f:
        for line in f:
            forest.append([int(ch) for ch in line.strip()])

    return forest


def partOne(forest: List[List[int]]) -> int:
    row = len(forest)
    col = len(forest[0])

    visibility = [[0 for _ in range(col)] for _ in range(row)]

    # left
    for i in range(row):
        tallest = -1
        for j in range(col):
            if forest[i][j] > tallest:
                visibility[i][j] = 1
                tallest = forest[i][j]

    # right
    for i in range(row):
        tallest = -1
        for j in range(col - 1, -1, -1):
            if forest[i][j] > tallest:
                visibility[i][j] = 1
                tallest = forest[i][j]

    # top
    for j in range(col):
        tallest = -1
        for i in range(row):
            if forest[i][j] > tallest:
                visibility[i][j] = 1
                tallest = forest[i][j]

    # bottom
    for j in range(col):
        tallest = -1
        for i in range(row - 1, -1, -1):
            if forest[i][j] > tallest:
                visibility[i][j] = 1
                tallest = forest[i][j]

    return sum([sum(items) for items in visibility])


def countVisibility(forest: List[List[int]], pos_i: int, pos_j: int, row: int, col: int) -> int:
    # down
    i = pos_i + 1
    down_count = 0
    while i < row:
        if forest[i][pos_j] < forest[pos_i][pos_j]:
            down_count += 1
            i += 1
        else:
            down_count += 1
            break

    # up
    i = pos_i - 1
    up_count = 0
    while i >= 0:
        if forest[i][pos_j] < forest[pos_i][pos_j]:
            up_count += 1
            i -= 1
        else:
            up_count += 1
            break

    # right
    j = pos_j + 1
    right_count = 0
    while j < col:
        if forest[pos_i][j] < forest[pos_i][pos_j]:
            right_count += 1
            j += 1
        else:
            right_count += 1
            break

    # left
    j = pos_j - 1
    left_count = 0
    while j >= 0:
        if forest[pos_i][j] < forest[pos_i][pos_j]:
            left_count += 1
            j -= 1
        else:
            left_count += 1
            break

    return down_count * up_count * right_count * left_count


def partTwo(forest) -> int:
    row = len(forest)
    col = len(forest[0])

    maxVisibility = 0
    for i in range(row):
        for j in range(col):
            visibility = countVisibility(forest, i, j, row, col)
            if maxVisibility < visibility:
                maxVisibility = visibility

    return maxVisibility


def main():
    filename = 'input.txt'
    forest = readData(filename)

    print(partOne(forest))
    print(partTwo(forest))


if __name__ == '__main__':
    main()
