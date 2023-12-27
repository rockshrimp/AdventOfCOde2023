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
            exit()
        i += 1
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
    print(y_pos, x_pos)

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
            exit()
        print(next_cells)
        i += 1

#part_2()