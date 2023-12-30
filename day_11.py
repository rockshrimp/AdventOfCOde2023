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

def part_1():
    expanded_lines = []
    for line in lines:
        expanded_lines.append(line)
        if line == '.' * len(line):
            expanded_lines.append(line)

    expanded_columns = []
    for i in range(len(expanded_lines[0])):
        column = ''.join([expanded_line[i] for expanded_line in expanded_lines])
        expanded_columns.append(column)
        if column == '.' * len(expanded_lines):
            expanded_columns.append(column)

    galaxies = []
    grid = [''] * len(expanded_lines)
    for i, column in enumerate(expanded_columns):
        for j, cell in enumerate(column):
            if cell == '#':
                galaxies.append((j, i))
            grid[j] += cell

    def get_distance(gal_1, gal_2):
        y_1, x_1 = gal_1
        y_2, x_2 = gal_2
        return max(x_1, x_2) - min(x_1, x_2) + max(y_1, y_2) - min(y_1, y_2)

    distance = 0
    while galaxies:
        current = galaxies.pop()
        for galaxy in galaxies:
            distance += get_distance(current, galaxy)
    print(distance)
#part_1()

def part_2():
    empty_lines = []
    for i, line in enumerate(lines):
        if line == '.' * len(line):
            empty_lines.append(i)

    empty_columns = []
    for j in range(len(lines[0])):
        column = ''.join([line[j] for line in lines])
        if column == '.' * len(lines):
            empty_columns.append(j)

    galaxies = []

    grid = [''] * len(lines)
    expansion_factor = 1000000 - 1
    for i, row in enumerate(lines):
        for j, cell in enumerate(row):
            if cell == '#':
                y_expansion = sum([expansion_factor for empty_line in empty_lines if empty_line < i])
                x_expansion = sum([expansion_factor for empty_column in empty_columns if empty_column < j])
                galaxies.append((i + y_expansion, j + x_expansion))


    def get_distance(gal_1, gal_2):
        y_1, x_1 = gal_1
        y_2, x_2 = gal_2
        return max(x_1, x_2) - min(x_1, x_2) + max(y_1, y_2) - min(y_1, y_2)

    distance = 0
    while galaxies:
        current = galaxies.pop()
        for galaxy in galaxies:
            distance += get_distance(current, galaxy)
    print(distance)
part_2()