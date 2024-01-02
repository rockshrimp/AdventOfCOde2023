from functools import cache

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

records = []
for line in lines :
    springs, groups = line.split(' ')
    groups = [int(c) for c in groups.split(',')]
    records.append((springs, groups))


@cache
def is_valid(springs, groups):
    if len(groups) == 0:
        return '#' not in springs

    if len(springs) == 0 and len(groups) == 0:
        return 1

    group_len = groups[0]
    min_length = sum(groups) + len(groups) - 1
    if len(springs) < min_length:
        return 0

    arrangements = 0
    if springs[0] == '.':
        return is_valid(springs[1:], groups)

    if '.' not in springs[:group_len]:
        if len(springs) == group_len or len(springs) > group_len and springs[group_len] != "#":
            arrangements += is_valid(springs[group_len + 1:], groups[1:])

    if springs[0] == '?':
        arrangements += is_valid(springs[1:], groups)

    return arrangements

def part_1():
    total = 0
    for record in records:
        springs, groups = record
        total += is_valid(tuple(springs), tuple(groups))
    print(total)
part_1()


def part_2():
    total = 0
    for record in records:
        springs, groups = record
        total += is_valid(tuple('?'.join([springs for _ in range(5)])), tuple(groups*5))
    print(total)
part_2()