file_path = 'input.txt'
with open(file_path, 'r') as file:
    lines = list(map(lambda line: line.split(), file.read().splitlines()))

dir_to_coord = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def add_coordinates(a, b, number):
    return a[0] + b[0] * number, a[1] + b[1] * number


def get_lava_count(lines):
    vertices = []
    x, y = 0, 0
    last_vertex = (x, y)
    perimeter = 0
    for line in lines:
        direction, number, color = line
        number = int(number)
        perimeter += number
        next_vertex = add_coordinates(last_vertex, dir_to_coord[direction], number)
        vertices.append(next_vertex)
        last_vertex = next_vertex
    print(vertices)

    total = 0
    for i in range(len(vertices) - 1):
        x_1, y_1 = vertices[i]
        x_2, y_2 = vertices[i + 1]
        total += 1/2 * (x_1 * y_2 - x_2 * y_1)
    return abs(total) + perimeter / 2 + 1

def part_1():
    print(get_lava_count(lines))
#part_1()

def part_2():
    new_lines = []
    for line in lines:
        direction, number, color = line
        hex_number = color[2:-2:]
        direction = int(color[-2])
        int_to_dir = 'RDLU'
        new_lines.append([int_to_dir[direction], int(hex_number, 16), color])
    print(get_lava_count(new_lines))
part_2()