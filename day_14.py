file_path = 'input.txt'
with open(file_path, 'r') as file:
    lines = file.read().splitlines()


def day_1():
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
day_1()
