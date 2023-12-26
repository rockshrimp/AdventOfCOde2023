from collections import Counter

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

    hands = []
    values = '23456789TJQKA'

    for line in lines:
        hand, bet = line.split()

        card_count = sorted(list(Counter(hand).values()), reverse=True)
        hands.append((hand, bet, card_count))

    def compare_cards(cards):
        return [values.index(c) for c in cards]

    hands.sort(key=lambda hand: (hand[-1], compare_cards(hand[0])), reverse=True)

    hands = hands[::-1]
    winnings = [int(hands[i][1]) * (i + 1) for i in range(len(hands))]
    print(sum(winnings))
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

    hands = []
    values = 'J23456789TQKA'

    for line in lines:
        hand, bet = line.split()

        card_counter = Counter(hand)
        if 'J' in card_counter and hand != 'JJJJJ':
            J_count = card_counter['J']
            del(card_counter['J'])
            card_counter_list = []
            for tup in list(card_counter.items()):
                key, val = tup
                card_counter_list.append([key, int(val)])

            sorted_card_counter = sorted(card_counter_list, key=lambda val: val[1], reverse=True)
            sorted_card_counter[0][1] += J_count
        else:
            card_counter_list = []
            for key, val in Counter(hand).items():
                card_counter_list.append([key, int(val)])

            sorted_card_counter = sorted(card_counter_list, key=lambda val: val[1], reverse=True)
        hands.append((hand, bet, [val[1] for val in sorted_card_counter]))

    def compare_cards(cards):
        return [values.index(c) for c in cards]

    hands.sort(key=lambda hand: (hand[-1], compare_cards(hand[0])))
    winnings = [int(hands[i][1]) * (i + 1) for i in range(len(hands))]
    print(sum(winnings))
part_2()


