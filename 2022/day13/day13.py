def comparator(d1, d2):
    rezult = 0
    if isinstance(d1, int) and isinstance(d2, int):
        if d1 < d2:
            return 1
        elif d1 == d2:
            return 0
        return -1

    elif isinstance(d1, list) and isinstance(d2, list):
        for i in range(min(len(d1), len(d2))):
            v1 = d1[i]
            v2 = d2[i]

            if isinstance(v1, int) and isinstance(v2, int):
                if v1 > v2:
                    return -1
                elif v1 < v2:
                    return 1

            else:
                if isinstance(v1, int):
                    rezult = comparator([v1, ], v2)
                else:
                    rezult = comparator(v1, [v2, ])

                if rezult != 0:
                    return rezult

    else:
        if isinstance(d1, int):
            rezult = comparator([d1, ], d2)
        else:
            rezult = comparator(d1, [d2, ])

        if rezult != 0:
            return rezult

    if len(d1) > len(d2) and rezult == 0:
        return -1
    elif len(d1) < len(d2):
        return 1

    return 0


def partOne(filename):
    data = []
    rez = 0
    i = 1
    with open(filename) as f:
        for line in f:
            nline = line.strip()
            if nline == '':
                r = comparator(data[0], data[1])
                if r >= 0:
                    rez += i
                    print('right', data[0], data[1])
                else:
                    print('notright', data[0], data[1])
                data = []
                i += 1
            else:
                data.append(eval(nline))

    r = comparator(data[0], data[1])
    if r >= 0:
        rez += i
        print('right', data[0], data[1])
    else:
        print('notright', data[0], data[1])

    return rez


if __name__ == '__main__':
    print(partOne('input.txt'))

# import json
# from functools import cmp_to_key
#
#
# def compare_one_index(first, second):
#     if type(first) is int and type(second) is int:
#         comparison_result = (first - second) // abs(first - second) if (first - second) != 0 else 0
#         # print(f'{first} VS {second} ==> {comparison_result}')
#         return comparison_result
#     elif type(first) is list and type(second) is list:
#         if len(first) == 0 and len(second) == 0:
#             # print(f'{first} VS {second} ==> -1  Both sides ran out of items')
#             return 0
#         elif len(first) == 0:
#             # print(f'{first} VS {second} ==> -1  Left side ran out of items')
#             return -1
#         elif len(second) == 0:
#             # print(f'{first} VS {second} ==> 1 Right side ran out of items')
#             return 1
#         else:
#             # print(f'{first} VS {second} ==> compare_each_index({first}, {second})')
#             return compare_each_index(first, second)
#     elif type(first) is int:
#         # print(f'{first} VS {second} ==> compare_one_index({[first]}, {second})')
#
#         return compare_one_index([first], second)
#     elif type(second) is int:
#         # print(f'{first} VS {second} ==> compare_one_index({first}, {[second]})')
#         return compare_one_index(first, [second])
#
#
# def compare_each_index(list1, list2):
#     for i in range(min(len(list1), len(list2))):
#         result = compare_one_index(list1[i], list2[i])
#
#         if result != 0:
#             return result
#
#     if len(list1) < len(list2):
#         # print("Left side ran out of items")
#         return -1
#     elif len(list1) == len(list2):
#         # print("Same amount of items")
#         return 0
#     else:
#         # print("Right side ran out of items")
#         return 1
#
#
# def solve(part, use_example):
#     #filename = "exampleinput.txt" if use_example else "input.txt"
#     filename = "input.txt"
#
#     if part == 1:
#         score_part1 = 0
#         with open(filename) as openfileobject:
#             raw = openfileobject.read()
#
#         chunks = raw.split('\n\n')
#
#         for chunk_index in range(len(chunks)):
#             rows = [json.loads(r.strip()) for r in chunks[chunk_index].split()]
#
#             result = compare_each_index(rows[0], rows[1])
#             if result != 1:  # (-1 == left smaller, 0 == left and right equal, which is fine)
#                 score_part1 += chunk_index + 1
#                 #print(f"chunk {chunk_index + 1}: True  (score: {score_part1})")
#             # else:
#             #print(f"chunk {chunk_index + 1}: False  (score: {score_part1})")
#
#         return score_part1
#
#     with open(filename) as openfileobject:
#         packets = [json.loads(l.strip()) for l in openfileobject.readlines() if l != '\n']
#
#     packets.append([[2]])
#     packets.append([[6]])
#     packets.sort(key=cmp_to_key(compare_each_index))
#
#     decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
#
#     return decoder_key
#
#
# print(f'Part 1: {solve(1, False)}')
# print(f'Part 2: {solve(2, False)}')
#
# # Part 1: 5682
# # Part 2: 20304
