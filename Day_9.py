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

    predictions_sum = 0
    for line in lines:
        sequence = [int(val) for val in line.split()]
        diff_list = [sequence]
        while not all([increment == 0 for increment in diff_list[-1]]):
            sequence_diff = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
            diff_list.append(sequence_diff)
            sequence = sequence_diff

        diff_list[-1].append(0)
        for i in range(len(diff_list) - 1, 0, -1):
            diff_list[i-1].append(diff_list[i-1][-1] + diff_list[i][-1])
        print(diff_list)
        predictions_sum += diff_list[0][-1]
    print(predictions_sum)
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

    predictions_sum = 0
    for line in lines:
        sequence = [int(val) for val in line.split()]
        diff_list = [sequence]
        while not all([increment == 0 for increment in diff_list[-1]]):
            sequence_diff = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
            diff_list.append(sequence_diff)
            sequence = sequence_diff

        diff_list[-1].append(0)
        for i in range(len(diff_list) - 1, 0, -1):
            diff_list[i-1].insert(0, diff_list[i-1][0] - diff_list[i][0])

        predictions_sum += diff_list[0][0]
    print(predictions_sum)
part_2()