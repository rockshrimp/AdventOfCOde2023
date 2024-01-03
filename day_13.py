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

def get_score(matrix, inversed: bool):
    for i in range(1, len(matrix) // 2 + 1):
        if matrix[:i] == matrix[i: 2 * i][::-1]:
            return (len(matrix) - i) if inversed else i
    return 0

def part_1():
    separators = [0]
    for idx, line in enumerate(lines):
        if line == '':
            separators.append(idx)
            separators.append(idx + 1)
    separators.append(len(lines))

    h_mirrors, v_mirrors = 0, 0
    while separators:
        start = separators.pop(0)
        end = separators.pop(0)

        figure = lines[start:end]

        columns = []
        for i in range(len(figure[0])):
            column = []
            for j in range(len(figure)):
                column.append(figure[j][i])
            columns.append(column)

        #Horizontal
        h_mirrors += get_score(figure, inversed =False) * 100
        h_mirrors += get_score(figure[::-1], inversed=True) * 100

        #Vertical
        v_mirrors += get_score(columns, inversed=False)
        v_mirrors += get_score(columns[::-1], inversed=True)

    total = h_mirrors + v_mirrors
    print(total)
part_1()

def find_smudge(matrix):
    for i in range(1, len(matrix)):
        up, down = matrix[i:], matrix[:i][::-1]
        diff_nb = 0
        for line_1, line_2 in zip(up, down):
            for x, y in zip(line_1, line_2):
                if x != y:
                    diff_nb += 1
        if diff_nb == 1:
            return i
    return 0


def part_2():
    separators = [0]
    for idx, line in enumerate(lines):
        if line == '':
            separators.append(idx)
            separators.append(idx + 1)
    separators.append(len(lines))

    total = 0
    while separators:
        start = separators.pop( 0)
        end = separators.pop(0)

        figure = lines[start:end]
        columns = []
        for i in range(len(figure[0])):
            column = []
            for j in range(len(figure)):
                column.append(figure[j][i])
            columns.append(column)

        total += 100 * find_smudge(figure) + find_smudge(columns)

    print(total)
part_2()
