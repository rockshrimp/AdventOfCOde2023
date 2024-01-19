file_path = 'input.txt'
with open(file_path, 'r') as file:
    lines = file.read().splitlines()


def bounds_check(current_cell, direction, width, height):
    x, y = current_cell
    if direction == 'right':
        if y + 1 >= width:
            return False
    if direction == 'left':
        if y - 1 < 0:
            return False
    if direction == 'up':
        if x - 1 < 0:
            return False
    if direction == 'down':
        if x + 1 >= height:
            return False
    return True


def get_next_cell(current_cell, direction, width, height):
    x, y = current_cell
    next_x, next_y = None, None
    if direction == 'right':
        if bounds_check(current_cell, 'right', width, height):
            next_x, next_y = x, y + 1
    elif direction == 'left':
        if bounds_check(current_cell, 'left', width, height):
            next_x, next_y = x, y - 1
    elif direction == 'up':
        if bounds_check(current_cell, 'up', width, height):
            next_x, next_y = x - 1, y
    elif direction == 'down':
        if bounds_check(current_cell, 'down', width, height):
            next_x, next_y = x + 1, y
    return (next_x, next_y)

def part_1():
    height = len(lines)
    width = len(lines[0])

    direction = 'right'
    start = (0, 0)
    cells_to_explore = [(start, direction)]
    explored_cells = set()
    while cells_to_explore:
        current_cell, direction = cells_to_explore.pop()

        if (current_cell, direction) in explored_cells:
            continue
        else:
            explored_cells.add((current_cell, direction))
        x, y = current_cell
        current_cell_char = lines[x][y]

        #print('current_cell:', current_cell_char, current_cell, direction)

        if current_cell_char == '.':
            if bounds_check(current_cell, direction, width, height):
                next_cell = get_next_cell(current_cell, direction, width, height)
                cells_to_explore.append((next_cell, direction))
        elif current_cell_char == '-':
            if direction in ['right', 'left']:
                if bounds_check(current_cell, direction, width, height):
                    next_cell = get_next_cell(current_cell, direction, width, height)
                    cells_to_explore.append((next_cell, direction))
            else:
                next_cell_left = (x, y - 1)
                next_cell_right = (x, y + 1)
                if bounds_check(current_cell, 'left', width, height):
                    cells_to_explore.append((next_cell_left, 'left'))
                if bounds_check(current_cell, 'right', width, height):
                    cells_to_explore.append((next_cell_right, 'right'))
        elif current_cell_char == '|':
            if direction in ['down', 'up']:
                if bounds_check(current_cell, direction, width, height):
                    next_cell = get_next_cell(current_cell, direction, width, height)
                    cells_to_explore.append((next_cell, direction))
            else:
                next_cell_up = (x - 1, y)
                next_cell_down = (x + 1, y)
                if bounds_check(current_cell, 'up', width, height):
                    cells_to_explore.append((next_cell_up, 'up'))
                if bounds_check(current_cell, 'down', width, height):
                    cells_to_explore.append((next_cell_down, 'down'))
        elif current_cell_char == '/':
            new_direction = {'right': 'up', 'left': 'down', 'up': 'right', 'down': 'left'}[direction]
            if bounds_check(current_cell, new_direction, width, height):
                next_cell = get_next_cell(current_cell, new_direction, width, height)
                cells_to_explore.append((next_cell, new_direction))
        elif current_cell_char == '\\':
            new_direction = {'right': 'down', 'left': 'up', 'up': 'left', 'down': 'right'}[direction]

            if bounds_check(current_cell, new_direction, width, height):
                next_cell = get_next_cell(current_cell, new_direction, width, height)
                cells_to_explore.append((next_cell, new_direction))

    print(len(set([cell[0] for cell in explored_cells])))

    grid = []
    for i in range(height):
        grid.append(['.' for i in range(width)])

    for cell in set([cell[0] for cell in explored_cells]):
        x, y = cell
        grid[x][y] = '#'

    for row in grid:
        print(''.join(row))
part_1()