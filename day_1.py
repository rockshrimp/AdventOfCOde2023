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
    res = 0

    letters = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for line in lines:
        numbers = []
        for i in range(len(line)):
            c = line[i]
            if c.isdecimal():
                numbers.append(int(c))
            else:
                for letter in list(letters.keys()):
                    if line[i:i + len(letter)] == letter:
                        numbers.append(letters[letter])
        res += 10 * numbers[0] + numbers[-1]
    print(res)
