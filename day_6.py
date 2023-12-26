if __name__ == '__main__':
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

        times, distances = [], []
        for line in lines:
            if 'Time' in line:
                times = [int(val) for val in line.split()[1:]]
            elif 'Distance' in line:
                distances = [int(val) for val in line.split()[1:]]
        print(times)
        print(distances)

        winning_product = 1
        for time, distance in list(zip(times, distances)):
            number_of_winning_times = 0
            for charging_time in range(time):
                if charging_time*(time - charging_time) > distance:
                    number_of_winning_times += 1
            winning_product *= number_of_winning_times
        print(winning_product)
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

        time, distance = 0, 0
        for line in lines:
            if 'Time' in line:
                time = int(''.join(line.split()[1:]))
            elif 'Distance' in line:
                distance = int(''.join(line.split()[1:]))

        number_of_winning_times = 0
        for charging_time in range(time):
            if charging_time*(time - charging_time) > distance:
                number_of_winning_times += 1

        print(number_of_winning_times)
    part_2()