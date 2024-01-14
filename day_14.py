file_path = 'input.txt'
with open(file_path, 'r') as file:
    lines = file.read().splitlines()


def part_1():
    cubes = {i: [] for i in range(len(lines[0]))}
    spheres = []
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[j][i] == 'O':
                spheres.append((i, j))
            elif lines[j][i] == '#':
                cubes[i].append(j)

    new_spheres_pos = {i: [] for i in range(len(lines[0]))}
    for sphere in spheres:
        x, y = sphere

        if len([val for val in cubes[x] if val < y]) == 0:
            if len(new_spheres_pos[x]) == 0:
                new_spheres_pos[x].append(0)
            else:
                new_pos = max([val for val in new_spheres_pos[x] if val < y]) + 1
                new_spheres_pos[x].append(new_pos)
        else:
            cube_pos = max([val for val in cubes[x] if val < y])

            if cube_pos + 1 not in new_spheres_pos[x]:
                new_spheres_pos[x].append(cube_pos + 1)
            else:
                new_spheres_pos[x].append(max([val for val in new_spheres_pos[x] if val < y]) + 1)

    total = 0
    for pos_list in new_spheres_pos.values():
        if pos_list:
            for val in pos_list:
                total += len(lines) - val
    print(total)
part_1()


def slide_north(cubes, spheres, width):
    new_spheres_pos = {i: [] for i in range(width)}
    for x in spheres:
        if len(spheres[x]) == 0:
            continue
        for y in sorted(spheres[x]):
            if len([val for val in cubes[x] if val < y]) == 0:
                if len(new_spheres_pos[x]) == 0:
                    new_spheres_pos[x].append(0)
                else:
                    new_pos = max([val for val in new_spheres_pos[x] if val < y]) + 1
                    new_spheres_pos[x].append(new_pos)
            else:
                cube_pos = max([val for val in cubes[x] if val < y])

                if cube_pos + 1 not in new_spheres_pos[x]:
                    new_spheres_pos[x].append(cube_pos + 1)
                else:
                    new_spheres_pos[x].append(max([val for val in new_spheres_pos[x] if val < y]) + 1)
    return new_spheres_pos


def left_rotate_coord(x, y, width):
    # counter clockwise
    #return y, height - 1 - x

    # clockwise
    return width - 1 - y, x


def rotate_dic(dic, width):
    rotated_dic = {i: [] for i in range(width)}
    for key, values in dic.items():
        for value in values:
            new_x, new_y = left_rotate_coord(key, value, width)
            rotated_dic[new_x].append(new_y)
    return rotated_dic


def display(cubes, spheres):
    grid = [['.' for i in range(10)] for i in range(10)]
    for x in cubes:
        if cubes[x]:
            for y in cubes[x]:
                grid[y][x] = '#'
    for x in spheres:
        if spheres[x]:
            for y in spheres[x]:
                grid[y][x] = '0'
    for row in grid:
        print(''.join(row))
    print('\n')


def part_2():
    cubes = {i: [] for i in range(len(lines[0]))}
    spheres = {i: [] for i in range(len(lines[0]))}
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[j][i] == 'O':
                spheres[i].append(j)
            elif lines[j][i] == '#':
                cubes[i].append(j)
    height, width = len(lines), len(lines[0])

    # Convert dict to list to store in set
    spheres_list = []
    for x in spheres:
        if spheres[x]:
            for y in spheres[x]:
                spheres_list.append((x, y))
    seen_configuration = {}
    found = False
    for i in range(1000000000):
        seen_configuration[i] = tuple(spheres_list)

        for j in range(4):
            new_spheres = slide_north(cubes, spheres, width)
            cubes = rotate_dic(cubes, width)
            spheres = rotate_dic(new_spheres, width)
            width, height = height, width

        spheres_list = []
        for x in spheres:
            if spheres[x]:
                for y in spheres[x]:
                    spheres_list.append((x, y))

        for k in range(len(seen_configuration)):  # period lookup
            if seen_configuration[k] == tuple(sorted(spheres_list)):
                found = True
                break
        if found:
            break

    period = i + 1 - k
    end_index = k + (1000000000 - k) % period
    spheres = seen_configuration[end_index]
    total = 0
    for pos in spheres:
        if pos:
            total += height - pos[1]
    print(total)
part_2()
