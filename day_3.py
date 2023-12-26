if __name__ == '__main__':
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
        res = 0
        height = len(lines)
        width = len(lines[0])
        visited_digits = [[0 for j in range(width)] for i in range(height)]
        for pos_y in range(height):
            for pos_x in range(width):
                c = lines[pos_y][pos_x]
                if c != '.' and not c.isdigit():

                    #Look at surrounding cells
                    for y in range(pos_y - 1, pos_y + 2):
                        if y < 0 or y >= height:
                            continue
                        for x in range(pos_x - 1, pos_x + 2):
                            if x < 0 or x >= width:
                                continue
                            elif lines[y][x].isdigit() and visited_digits[y][x] != 1:
                                part_number = []
                                left_cell = x - 1
                                while left_cell >= 0 and lines[y][left_cell].isdigit():
                                    part_number.append(lines[y][left_cell])
                                    visited_digits[y][left_cell] = 1
                                    left_cell -= 1
                                part_number = part_number[::-1]
                                right_cell = x
                                while right_cell < width and lines[y][right_cell].isdigit():
                                    part_number.append(lines[y][right_cell])
                                    visited_digits[y][right_cell] = 1
                                    right_cell += 1
                                res += int(''.join(part_number))

        print(res)

    def part_2():
        res = 0
        height = len(lines)
        width = len(lines[0])
        visited_digits = [[0 for j in range(width)] for i in range(height)]
        for pos_y in range(height):
            for pos_x in range(width):
                c = lines[pos_y][pos_x]
                if c != '.' and not c.isdigit():
                    number_of_adjacent_parts = 0
                    adjacent_parts_values = []
                    #Look at surrounding cells
                    for y in range(pos_y - 1, pos_y + 2):
                        if y < 0 or y >= height:
                            continue
                        for x in range(pos_x - 1, pos_x + 2):
                            if x < 0 or x >= width:
                                continue
                            elif lines[y][x].isdigit() and visited_digits[y][x] != 1:
                                number_of_adjacent_parts += 1
                                part_number = []
                                left_cell = x - 1
                                while left_cell >= 0 and lines[y][left_cell].isdigit():
                                    part_number.append(lines[y][left_cell])
                                    visited_digits[y][left_cell] = 1
                                    left_cell -= 1
                                part_number = part_number[::-1]
                                right_cell = x
                                while right_cell < width and lines[y][right_cell].isdigit():
                                    part_number.append(lines[y][right_cell])
                                    visited_digits[y][right_cell] = 1
                                    right_cell += 1
                                adjacent_parts_values.append(int(''.join(part_number)))
                    if number_of_adjacent_parts == 2:
                        res += adjacent_parts_values[0]*adjacent_parts_values[1]
        print(res)

    part_2()