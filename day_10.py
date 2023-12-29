def part_1():
    file_path = 'input.txt'
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    y_pos, x_pos = 0, 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                y_pos, x_pos = i, j

    valid_pipes = {'up': '|F7', 'down': '|LJ', 'left': '-FL', 'right': '-7J'}
    i = 0
    next_cells = [(y_pos, x_pos, 0)]
    explored = [[0] * len(lines[0]) for _ in range(len(lines))]
    explored[y_pos][x_pos] = 1

    while True:
        y_pos, x_pos, distance = next_cells.pop(0)
        explored[y_pos][x_pos] = 1
        if y_pos - 1 >= 0 and explored[y_pos - 1][x_pos] == 0:
            up = lines[y_pos - 1][x_pos]
            if up in valid_pipes['up']:
                next_cells.append((y_pos - 1, x_pos, distance + 1))
        if y_pos + 1 < len(lines) and explored[y_pos + 1][x_pos] == 0:
            down = lines[y_pos + 1][x_pos]
            if down in valid_pipes['down']:
                next_cells.append((y_pos + 1, x_pos, distance + 1))
        if x_pos - 1 >= 0 and explored[y_pos][x_pos - 1] == 0:
            left = lines[y_pos][x_pos - 1]
            if left in valid_pipes['left']:
                next_cells.append((y_pos, x_pos - 1, distance + 1))
        if x_pos + 1 < len(lines[0]) and explored[y_pos][x_pos + 1] == 0:
            right = lines[y_pos][x_pos + 1]
            if right in valid_pipes['right']:
                next_cells.append((y_pos, x_pos + 1, distance + 1))
        if len(next_cells) == 0:
            print('found furthest cell at distance', distance)
            break
#part_1()

def part_2():
    file_path = 'input.txt'
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    y_pos, x_pos = 0, 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                y_pos, x_pos = i, j

    valid_pipes = {'up': '|F7', 'down': '|LJ', 'left': '-FL', 'right': '-7J'}

    start_cell_directions = []
    if y_pos - 1 >= 0:
        if lines[y_pos - 1][x_pos] in valid_pipes['up']:
            start_cell_directions.append('down')
    if y_pos + 1 < len(lines):
        if lines[y_pos + 1][x_pos] in valid_pipes['down']:
            start_cell_directions.append('up')
    if x_pos - 1 >= 0:
        if lines[y_pos][x_pos - 1] in valid_pipes['left']:
            start_cell_directions.append('right')
    if x_pos + 1 < len(lines[0]):
        if lines[y_pos][x_pos + 1] in valid_pipes['right']:
            start_cell_directions.append('left')

    # Replacing the S character for the corresponding pipe
    for c in valid_pipes[start_cell_directions[0]]:
        if c in valid_pipes[start_cell_directions[1]]:
            temp = list(lines[y_pos])
            temp[x_pos] = c
            lines[y_pos] = temp
            break
    i = 0
    next_cells = [(y_pos, x_pos)]
    explored = [[0] * len(lines[0]) for _ in range(len(lines))]
    explored[y_pos][x_pos] = 1

    while True:
        y_pos, x_pos = next_cells.pop(0)
        current_cell = lines[y_pos][x_pos]
        explored[y_pos][x_pos] = 1
        if y_pos - 1 >= 0 and explored[y_pos - 1][x_pos] == 0:
            up = lines[y_pos - 1][x_pos]
            if up in valid_pipes['up'] and current_cell in valid_pipes['down']:
                next_cells.append((y_pos - 1, x_pos))
        if y_pos + 1 < len(lines) and explored[y_pos + 1][x_pos] == 0:
            down = lines[y_pos + 1][x_pos]
            if down in valid_pipes['down'] and current_cell in valid_pipes['up']:
                next_cells.append((y_pos + 1, x_pos))
        if x_pos - 1 >= 0 and explored[y_pos][x_pos - 1] == 0:
            left = lines[y_pos][x_pos - 1]
            if left in valid_pipes['left'] and current_cell in valid_pipes['right']:
                next_cells.append((y_pos, x_pos - 1))
        if x_pos + 1 < len(lines[0]) and explored[y_pos][x_pos + 1] == 0:
            right = lines[y_pos][x_pos + 1]
            if right in valid_pipes['right'] and current_cell in valid_pipes['left']:
                next_cells.append((y_pos, x_pos + 1))
        if len(next_cells) == 0:
            break
        i += 1

    # To know if a cell is inside the loop, we check how many time we
    # cross the loop along the line on the right side of the cell.
    # If we cross the loop an even number of times, we're inside the loop.
    inside_cells_count = 0
    for i, line in enumerate(explored):
        number_of_pipes = 0
        for j, cell in enumerate(line):
            if cell == 1:
                number_of_pipes += 1
            else:
                edge_count = 0
                for k, c in enumerate(lines[i][j+1:], j+1):
                    if explored[i][k] == 1:
                        if c in '|F7':
                            edge_count += 1
                if edge_count % 2:
                    inside_cells_count += 1
    print(inside_cells_count)

part_2()