file_path = 'input.txt'
with open(file_path, 'r') as file:
    txt = file.read().strip()
def hash_str(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

def part_1():
    res = 0
    for string in txt.split(','):
        res += hash_str(string)
    print(res)
#part_1()

def part_2():
    hash_map = {i: [] for i in range(256)}
    res = 0
    for string in txt.split(','):
        if '-' in string:
            label_to_remove = string[:-1]
            box_id = hash_str(label_to_remove)

            for i, lens in enumerate(hash_map[box_id]):
                if label_to_remove == lens[0]:
                    hash_map[box_id].pop(i)
                    break
        else:
            label_to_add, focal = string.split('=')
            box_id = hash_str(label_to_add)

            found = False
            for i, lens in enumerate(hash_map[box_id]):
                if label_to_add == lens[0]:
                    hash_map[box_id][i][1] = focal
                    found = True
                    break
            if not found:
                hash_map[box_id].append([label_to_add, focal])

    res = 0
    for box_number, box in hash_map.items():
        for slot, lens in enumerate(box, 1):
            focal_length = lens[1]
            focusing_power = 1 * (box_number + 1) * slot * int(focal_length)
            res += focusing_power
    print(res)
part_2()
