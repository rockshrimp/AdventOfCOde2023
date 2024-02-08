with open('input.txt', 'r') as file:
    lines = file.read().splitlines()


def bounds_check(cell_coord):
    x, y = cell_coord
    return True if 0 <= x < height and 0 <= y < width else False


dir_to_coord = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def add_coordinates(cell, step):
    return cell[0] + step[0], cell[1] + step[1]


height = len(lines)
width = len(lines[0])

start = (0, 0)
for i in range(height):
    for j in range(width):
        if lines[i][j] == 'S':
            start = (i, j)

def part_1(start, number_of_steps):
    plots_by_step = {i: set() for i in range(number_of_steps + 1)}
    plots_by_step[0].add(start)

    for i in range(number_of_steps):
        for plot in plots_by_step[i]:
            for dir in dir_to_coord.values():
                neighbour = add_coordinates(plot, dir)
                if bounds_check(neighbour):
                    x, y = neighbour
                    if lines[x][y] != '#':
                        plots_by_step[i + 1].add(neighbour)
    print(len(plots_by_step[number_of_steps]))
part_1(start, 64)
