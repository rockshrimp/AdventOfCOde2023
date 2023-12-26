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
        points = 0
        for line in lines:
            numbers = line.split(': ')[1]
            winning_numbers, my_numbers = numbers.split(' | ')
            winning_numbers = set(winning_numbers.split(' '))
            if '' in winning_numbers:
                winning_numbers.remove('')
            my_numbers = set(my_numbers.split(' '))
            if '' in my_numbers:
                my_numbers.remove('')

            number_of_matches = len(winning_numbers.intersection(my_numbers))
            if number_of_matches > 0:
                points += 2 ** (number_of_matches - 1)
        print(points)
    #part_1()

    def part_2():
        cards_ids = [1] * len(lines)
        for i in range(len(lines)):
            card, numbers = lines[i].split(': ')
            card_id = int(card.split(' ')[-1])
            winning_numbers, my_numbers = numbers.split(' | ')
            winning_numbers = set(winning_numbers.split(' '))
            if '' in winning_numbers:
                winning_numbers.remove('')
            my_numbers = set(my_numbers.split(' '))
            if '' in my_numbers:
                my_numbers.remove('')

            number_of_matches = len(winning_numbers.intersection(my_numbers))
            for i in range(card_id, card_id + number_of_matches):
                cards_ids[i] += cards_ids[card_id - 1]

        print(sum(cards_ids))
    part_2()

