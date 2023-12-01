def part_1():
    result = 0
    with open('input.txt') as f:
        for line in f.readlines():
            number = ""
            i = 0
            while i < len(line) - 1:
                if line[i].isdigit():
                    number += line[i]
                    break
                i += 1

            j = len(line) - 1

            while j >= i:
                if line[j].isdigit():
                    number += line[j]
                    break
                j -= 1

            result += int(number)

    return result


def part_2():
    forward = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
        "nine": "9"
    }

    result = 0
    with open('input.txt') as f:
        for line in f.readlines():
            number = ""
            i = 0
            while i < len(line) - 1:

                for k, v in forward.items():
                    lk = len(k)
                    if line[i:i + lk] == k:
                        number += v
                        break

                if number:
                    break

                if line[i].isdigit():
                    number += line[i]
                    break
                i += 1
            result += int(number) * 10

            number = ""
            j = len(line) - 1
            while j >= 0:

                for k, v in forward.items():
                    lk = len(k)
                    if line[j - lk + 1:j + 1] == k:
                        number += v
                        break

                if number:
                    break

                if line[j].isdigit():
                    number += line[j]
                    break
                j -= 1

            result += int(number)

    return result


if __name__ == "__main__":
    print(part_1())
    print(part_2())
