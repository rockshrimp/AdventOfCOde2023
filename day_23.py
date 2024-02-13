from copy import deepcopy
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

height = len(lines)
width = len(lines[0])

dir_to_coord = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def add_coordinates(a, b):
    return a[0] + b[0], a[1] + b[1]

def is_not_in(cell_coord):
    x, y = cell_coord
    return False if 0 <= x < height and 0 <= y < width else True

def bfs(starting_cell):
    steps_list = []
    visited = set()
    queue = [starting_cell]
    paths = [{'queue': queue, 'visited': visited}]
    while paths:
        path = paths.pop(0)
        #print('in path ', path)
        queue = path['queue']
        visited = path['visited']
        while(queue):
            current_cell = queue.pop(0)
            visited.add(current_cell)
            new_neighbours = []
            for dir, coord in dir_to_coord.items():
                new_coord = add_coordinates(current_cell, coord)
                if is_not_in(new_coord):
                    continue

                new_x, new_y = new_coord
                if lines[new_x][new_y] == '#' or new_coord in visited:
                    continue

                if lines[new_x][new_y] in '^v<>' and dir == 'UDLR'['^v<>'.index(lines[new_x][new_y])]:
                    #print('facing ', lines[new_x][new_y])
                    new_neighbours.append(new_coord)

                elif lines[new_x][new_y] == '.':
                    new_neighbours.append(new_coord)

            #print(current_cell, new_neighbours)
            if len(new_neighbours) == 1:
                queue.append(new_neighbours[0])
            elif len(new_neighbours) > 1:
                for new_neighbour in new_neighbours[1:]:
                    new_queue = deepcopy(queue)
                    new_queue.append(new_neighbour)
                    paths.append({'queue': new_queue, 'visited': deepcopy(visited)})
                queue.append(new_neighbours[0])

        grid = []
        for i, line in enumerate(lines):
            grid.append([])
            for j in range(len(line)):
                grid[i].append('O' if (i,j) in visited else lines[i][j])
        for row in grid:
            #print(''.join(row))
            pass
        print('visited = ', len(visited) - 1)
        steps_list.append(len(visited) - 1)
    return steps_list


def part_1():
    starting_cell = (0, 1)
    print(max(bfs(starting_cell)))
part_1()