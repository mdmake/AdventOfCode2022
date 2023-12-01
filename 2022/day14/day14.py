lines = [x.split() for x in open("input.txt")]
field = set()
start = (500, 0)


def draw_line(start_p, end_p):
    shape = list(zip([int(x) for x in start_p], [int(x) for x in end_p]))
    x_sorted = sorted([shape[0][0], shape[0][1]])
    y_sorted = sorted([shape[1][0], shape[1][1]])

    for x in range(x_sorted[0], x_sorted[1] + 1):
        for y in range(y_sorted[0], y_sorted[1] + 1):
            field.add((x, y))


for l in lines:
    points = [x for x in l if x != '->']
    for i in range(1, len(points)):
        p1, p2 = points[i - 1].split(','), points[i].split(',')
        draw_line(p1, p2)
lowest = sorted(field, key=lambda a: a[1])[-1][1]
floor = lowest + 2


def test_collision_down(point, mode):
    obstacles = [x for x in field if x[0] == point[0] and x[1] > point[1]]
    nearest = sorted(obstacles, key=lambda a: a[1])
    if nearest:
        return nearest[0]
    else:
        if mode:
            return (point[0], floor)
        else:
            return []


def test_collision_diag(point, mode):
    if mode:
        res = point[1] < floor and point not in field
        return res
    else:
        return point not in field


def simulate_sand(s, mode):
    rest = False
    while not rest:
        obst_d = test_collision_down(s, mode)
        if obst_d:
            s = (s[0], obst_d[1] - 1)
        else:
            return (-1, -1)
        attempt_l, attempt_r = (s[0] - 1, s[1] + 1), (s[0] + 1, s[1] + 1)
        if test_collision_diag(attempt_l, mode):
            s = attempt_l
            continue
        elif test_collision_diag(attempt_r, mode):
            s = attempt_r
            continue
        else:
            return s


def run_sim(mode):
    sand_count = 0
    while True:
        res = simulate_sand(start, mode)
        if res == (-1, -1):
            print(f'part{mode + 1}: {sand_count}')
            break
        else:
            if res in field:
                print(f'part{mode + 1}: {sand_count}')
                break
            elif res == start:
                print(f'part{mode + 1}: {sand_count + 1}')
                break
            field.add(res)
            sand_count += 1
            print(f'{res[1] * "o"}')


# run_sim(0)
run_sim(1)
