from functools import reduce

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
        valid_games = []
        max_cubes = {'green': 13, 'red': 12, 'blue': 14}
        for line in lines:
                game_str, results = line.split(':')
                id = game_str.split(' ')[1]
                sets = results.split(';')
                valid_game = True
                for set_str in sets:
                    colors_str = set_str.split(',')
                    print(colors_str)
                    for color_str in colors_str:
                        number, color = color_str.lstrip().split(' ')

                        if max_cubes[color] < int(number):
                            valid_game = False
                            break

                if valid_game:
                    valid_games.append(int(id))
        print(sum(valid_games))

    #part_1()

    def part_2():
        power_sum = 0
        for line in lines:
            max_cubes = {'green': 0, 'red': 0, 'blue': 0}
            game_str, results = line.split(':')
            id = game_str.split(' ')[1]
            sets = results.split(';')
            for set_str in sets:
                colors_str = set_str.split(',')
                for color_str in colors_str:
                    number, color = color_str.lstrip().split(' ')

                    if max_cubes[color] < int(number):
                        max_cubes[color] = int(number)
            print(max_cubes.values())
            power_sum += reduce(lambda a, b: a*b, max_cubes.values())

        print(power_sum)
    part_2()
