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

def get_plot_count(number_of_steps):
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
    return len(plots_by_step[number_of_steps])

def part_1(number_of_steps):
    print(get_plot_count(number_of_steps))
part_1(64)


def get_steps_by_plot_dic(number_of_steps):
    visited_plots = {}
    visited_plots[start] = 0
    visited_plots_queue = [start]
    for i in range(number_of_steps + 1):
        new_neighbours = set()
        for plot in visited_plots_queue:
            visited_plots[plot] = i
            for dir in dir_to_coord.values():
                neighbour = add_coordinates(plot, dir)
                x, y = neighbour
                if lines[x % height][y % width] != '#' and neighbour not in visited_plots:
                    new_neighbours.add(neighbour)
        visited_plots_queue = new_neighbours
    return visited_plots


def get_plots_for_steps(max_steps):
    dist = get_steps_by_plot_dic(max_steps)
    return len([x for x in dist if dist[x] <= max_steps and dist[x] % 2 == max_steps % 2])


def part_2():
    r1 = get_plots_for_steps(65)
    r2 = get_plots_for_steps(131 + 65)
    r3 = get_plots_for_steps(65 + 2 * 131)
    a0 = r1
    a1 = (4 * r2 - r3 - 3 * a0) // 2
    a2 = r2 - (a0 + a1)

    n = 26501365 // 131
    print('Part 2 :', a0 + a1 * n + a2 * n ** 2)
part_2()