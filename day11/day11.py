class Monkey:

    def __init__(self, num, items, operation, test, lr, reduce):
        self.name = num
        self.items = items
        self.operation = operation
        self.test = test
        self.modulo = 0
        self.lr = lr
        self.reduce = reduce
        self.count = 0

    def setNeighbour(self, leftMonkey: 'Monkey', rightMonkey: 'Monkey'):
        self.left = leftMonkey
        self.right = rightMonkey

    def send(self, item, left=True):
        if left:
            self.left.items.append(item)
        else:
            self.right.items.append(item)

    def calculateWorry(self, item):
        old = item
        return eval(self.operation)

    def play(self):
        for item in self.items:
            current = self.calculateWorry(item) % self.modulo
            current = int(current / self.reduce)

            self.send(current, (current % self.test == 0))
            self.count += 1
        self.items = []


def partOne(filename, worryDecrease, roundsCount):
    with open(filename) as f:
        neibours = {}
        data = {}
        for line in f:
            if len(line.strip()) < 1:
                continue

            nline = line
            number = int(nline.replace(':', '').split()[-1].strip())
            nline = next(f)
            startitems = [int(item) for item in nline.strip().split(':')[-1].split(', ')]
            nline = next(f)
            operation = nline.split('=')[-1].strip()
            nline = next(f)
            test = int(nline.strip().split()[-1])
            nline = next(f)
            neibours[number] = [int(nline.strip().split()[-1]), ]
            nline = next(f)
            neibours[number].append(int(nline.strip().split()[-1]))

            data[number] = Monkey(
                num=number,
                items=startitems,
                operation=operation,
                test=test,
                lr=neibours[number],
                reduce=worryDecrease,
            )

    modulo = 1

    for k, v in data.items():
        v.setNeighbour(data[v.lr[0]], data[v.lr[1]])
        modulo *= v.test

    for v in data.values():
        v.modulo = modulo

    for _ in range(roundsCount):
        for k, v in data.items():
            v.play()

    rez = []
    for k, v in data.items():
        rez.append(v.count)
        print(k, ':', v.count)

    rez.sort(reverse=True)
    print(rez[0] * rez[1])


if __name__ == '__main__':
    partOne('input.txt', 3, 20)
    partOne('input.txt', 1, 10000)
