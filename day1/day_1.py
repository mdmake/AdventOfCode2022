def partOne(filename):
    calories = 0
    current_elf_calories = 0
    with open(filename) as f:
        for line in f:
            if line.strip() == '':
                if current_elf_calories > calories:
                    calories = current_elf_calories
                current_elf_calories = 0
            else:
                current_elf_calories += int(line.strip())

    if current_elf_calories > calories:
        calories = current_elf_calories

    return calories


def partTwoSimple(filename):
    calories = [0, 0, 0]
    current_elf_calories = 0
    with open(filename) as f:
        for line in f:
            if line.strip() == '':
                if current_elf_calories > calories[0]:
                    calories[0] = current_elf_calories
                elif current_elf_calories > calories[1]:
                    calories[1] = current_elf_calories
                elif current_elf_calories > calories[2]:
                    calories[2] = current_elf_calories

                current_elf_calories = 0
            else:
                current_elf_calories += int(line.strip())

    if current_elf_calories > calories[0]:
        calories[0] = current_elf_calories
    elif current_elf_calories > calories[1]:
        calories[1] = current_elf_calories
    elif current_elf_calories > calories[2]:
        calories[2] = current_elf_calories

    return sum(calories)


if __name__ == "__main__":
    print(partOne('input.txt'))
    print(partTwoSimple('input.txt'))
