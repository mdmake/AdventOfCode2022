class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.subdir = {}
        self.files = {}
        self.parent = parent
        self.size = 0


def checkSum(node: Directory) -> (int, int):
    rez = 0
    minrez = 0
    for k, v in node.subdir.items():
        r, mr = checkSum(v)
        rez += r
        minrez += mr

    rez += sum(node.files.values())
    node.size = rez

    if rez <= 100000:
        minrez += rez
    else:
        minrez += 0

    return rez, minrez


def findSmallest(node: Directory, need: int) -> (int, int):
    rez = 0
    minValues = []
    for k, v in node.subdir.items():
        r, minv = findSmallest(v, need)
        minValues.append(minv)
        rez += r

    rez += sum(node.files.values())
    minValues.append(rez)

    totalMinValue = float('inf')
    for item in minValues:
        if need <= item < totalMinValue:
            totalMinValue = item

    return rez, totalMinValue


def createTree(filename):
    root = None
    currenNode = None
    with open(filename) as f:
        for line in f:
            if '$ cd' in line:
                _, cd, dirname = line.strip().split()
                if dirname == '/':
                    if not currenNode:
                        root = Directory('root')
                        currenNode = root
                    else:
                        currenNode = root

                elif dirname == '..':
                    currenNode = currenNode.parent
                else:
                    currenNode = currenNode.subdir[dirname]

            elif '$ ls' in line:
                pass
            else:
                first, second = line.strip().split()
                if first == 'dir':
                    node = Directory(second, currenNode)
                    currenNode.subdir[second] = node
                else:
                    currenNode.files[second] = int(first)

    return root


def main(filename):
    TOTALSPACE = 70000000
    NEEDEDSPACE = 30000000

    root = createTree(filename)
    rootSize, result = checkSum(root)
    needed = NEEDEDSPACE - (TOTALSPACE - rootSize)

    _, smallest = findSmallest(root, needed)
    return result, smallest


if __name__ == '__main__':
    partOneSolution, partTwoSolution = main('input.txt')
    print(partOneSolution)
    print(partTwoSolution)
