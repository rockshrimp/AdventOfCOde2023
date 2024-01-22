from heapq import heappop, heappush

file_path = 'input.txt'
with open(file_path, 'r') as file:
    lines = list(map(lambda line: [int(c) for c in line], file.read().splitlines()))

height = len(lines)
width = len(lines[0])


def bounds_check(cell_coord):
    x, y = cell_coord
    return True if 0 <= x < height and 0 <= y < width else False


def add_coordinates(a, b):
    return a[0] + b[0], a[1] + b[1]


def get_neighbours(cell):
    neigbours = []
    current_position, current_direction, count = cell
    coordinates_dic = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}
    direction_to_neighbours = {'u': 'lur', 'd': 'ldr', 'r': 'urd', 'l': 'uld'}

    neighbours_directions = direction_to_neighbours[current_direction]
    for direction in neighbours_directions:
        step = coordinates_dic[direction]
        neighbour_coord = add_coordinates(current_position, step)
        if bounds_check(neighbour_coord):
            if direction == current_direction:
                if count + 1 < 4:
                    neigbours.append((neighbour_coord, direction, count + 1))
            else:
                neigbours.append((neighbour_coord, direction, 1))
    return neigbours


def get_heat_loss():
    x_start, y_start = 0, 0
    starting_cell = ((x_start, y_start), 'd', 0)
    heat_loss = 0
    cells_dict = {starting_cell: heat_loss}
    cells_queue = [(heat_loss, starting_cell)]
    end_cell_coordinates = (height - 1, width - 1)

    while cells_queue:
        current_heat_loss, current_cell = heappop(cells_queue)
        neighbours = get_neighbours(current_cell)

        for neighbour in neighbours:
            coordinates, direction, count = neighbour
            x, y = coordinates

            if coordinates == end_cell_coordinates:
                return lines[x][y] + current_heat_loss

            heat_loss = lines[x][y] + current_heat_loss
            if heat_loss < cells_dict.get(neighbour, float('inf')):
                heappush(cells_queue, (heat_loss, neighbour))
                cells_dict[neighbour] = heat_loss

def part_1():
    print(get_heat_loss())

part_1()
