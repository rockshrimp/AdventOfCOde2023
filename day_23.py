from copy import deepcopy
from collections import defaultdict
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

def find_steps(start_cell, end_cell):
    steps_list = []
    visited = set()
    queue = [start_cell]
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



        '''
        grid = []
        if len(visited) - 1 > 150:
            for i, line in enumerate(lines):
                grid.append([])
                for j in range(len(line)):
                    grid[i].append('O' if (i,j) in visited else lines[i][j])
            for row in grid:
                #print(''.join(row))
          '''

        if end_cell in visited:
            #print('visited = ', len(visited) - 1)
            steps_list.append(len(visited) - 1)
    return steps_list


def part_1():
    start_cell = (0, 1)
    end_cell = (height - 1, width - 2)
    print('part_1', max(find_steps(start_cell, end_cell)))
part_1()

def get_neighbours(cell):
    neighbours = []
    for dir, coord in dir_to_coord.items():
        new_coord = add_coordinates(cell, coord)
        if is_not_in(new_coord):
            continue
        new_x, new_y = new_coord

        if lines[new_x][new_y] in '.^v<>':
            neighbours.append(new_coord)
    return neighbours

def get_vertices(start_cell, end_cell):
    vertices = []
    for x in range(height):
        for y in range(width):
            neighbours_count = 0
            if lines[x][y] == '#':
                continue
            for dir, coord in dir_to_coord.items():
                new_coord = add_coordinates((x, y), coord)
                new_x, new_y = new_coord

                if is_not_in(new_coord) or lines[new_x][new_y] == '#':
                    continue

                if lines[new_x][new_y] in '.^v<>':
                    neighbours_count += 1
            if neighbours_count > 2:
                vertices.append((x, y))
    return [start_cell, end_cell] + vertices

def dfs(start_cell, end_cell, total_distance, vertices_connections, visited):
    if start_cell == end_cell:
        yield total_distance

    for vertex, distance in vertices_connections[start_cell]:
        if vertex not in visited:
            visited.add(vertex)
            yield from dfs(vertex, end_cell, total_distance + distance, vertices_connections, visited)
            visited.remove(vertex)

def part_2():
    start_cell = (0, 1)
    end_cell = (height - 1, width - 2)

    vertices = get_vertices(start_cell, end_cell)
    vertices_connections = defaultdict(list)
    for vertex in vertices:
        for neighbour in get_neighbours(vertex):
            previous_cell, current_cell = vertex, neighbour
            distance = 1
            while current_cell not in vertices:
                temp = previous_cell
                previous_cell = current_cell
                current_cell = [neighbour for neighbour in get_neighbours(current_cell) if neighbour != temp][0]
                distance += 1
            vertices_connections[vertex].append((current_cell, distance))
    print(max(dfs(start_cell, end_cell, 0, vertices_connections, {start_cell})))
part_2()

