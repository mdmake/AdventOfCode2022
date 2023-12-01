import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"QItem({self.row}, {self.col})"


def readFile(filename):
    # data = np.zeros((41, 173), dtype=int)
    data = np.zeros((5, 8), dtype=int)
    visited = np.zeros((5, 8), dtype=bool)

    with open(filename) as f:
        i = 0
        for line in f:
            nline = line.strip()
            for j, ch in enumerate(nline):
                if ch == 'E':

                    data[i][j] = ord('z') - ord('a') + 1
                    target = Point(i, j)
                    print('target', i, j)
                elif ch == 'S':
                    data[i][j] = 0
                else:
                    data[i][j] = ord(ch) - ord('a') + 1

            i += 1
    sns.heatmap(data, annot=False)
    plt.show()

    return data, target


def minDistance(grid, source):
    #price = np.zeros((41, 173), dtype=int)
    price = np.zeros((5, 8), dtype=bool)
    queue = []
    queue.append(source)
    price[source.row][source.col] = 0

    while len(queue) != 0:
        source = queue.pop(0)

        # Destination found;
        # if (grid[source.row][source.col] == 'd'):
        #     return source.dist

        if grid[source.row][source.col] == 1:
            sns.heatmap(price, annot=False)
            plt.show()
            return price[source.row][source.col]

        # moving up
        if valid(source.row, source.col, source.row - 1, source.col, grid,  price):
            queue.append(Point(source.row - 1, source.col))
            price[source.row - 1][source.col] = price[source.row][source.col] + 1

        # moving down
        if valid(source.row, source.col, source.row + 1, source.col, grid,  price):
            queue.append(Point(source.row + 1, source.col))
            price[source.row + 1][source.col] = price[source.row][source.col] + 1

        # moving left
        if valid(source.row, source.col, source.row, source.col - 1, grid,  price):
            queue.append(Point(source.row, source.col - 1))
            price[source.row][source.col - 1] = price[source.row][source.col] + 1

        # moving right
        if valid(source.row, source.col, source.row, source.col + 1, grid,  price):
            queue.append(Point(source.row, source.col + 1))
            price[source.row][source.col + 1] = price[source.row][source.col] + 1

    sns.heatmap(price, annot=False)
    plt.show()
    return -1


def minDistance0(grid, source):
    #price = np.zeros((41, 173), dtype=int)
    price = np.zeros((5, 8), dtype=int)

    queue = []
    queue.append(source)
    price[source.row][source.col] = 0

    while len(queue) != 0:
        source = queue.pop(0)



        if grid[source.row][source.col] == 0:
            sns.heatmap(price, annot=False)
            plt.show()
            return price[source.row][source.col]

        # moving up
        if valid(source.row, source.col, source.row - 1, source.col, grid,  price):
            queue.append(Point(source.row - 1, source.col))
            price[source.row - 1][source.col] = price[source.row][source.col] + 1

        # moving down
        if valid(source.row, source.col, source.row + 1, source.col, grid,  price):
            queue.append(Point(source.row + 1, source.col))
            price[source.row + 1][source.col] = price[source.row][source.col] + 1

        # moving left
        if valid(source.row, source.col, source.row, source.col - 1, grid,  price):
            queue.append(Point(source.row, source.col - 1))
            price[source.row][source.col - 1] = price[source.row][source.col] + 1

        # moving right
        if valid(source.row, source.col, source.row, source.col + 1, grid,  price):
            queue.append(Point(source.row, source.col + 1))
            price[source.row][source.col + 1] = price[source.row][source.col] + 1

    sns.heatmap(price, annot=False)
    plt.show()
    return -1


# checking where move is valid or not
def valid(x0, y0, x, y, grid, price):
    if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            ((grid[x0][y0] == grid[x][y] + 1) or (grid[x0][y0] <= grid[x][y]))):
        if price[x][y] == 0:
            return True
        elif price[x][y] > (price[x0][y0] + 1):
            return True
        else:
            return False

    return False


if __name__ == '__main__':
    data, target = readFile('input.txt')

    #print(minDistance(data, target))
    print(minDistance0(data, target))
