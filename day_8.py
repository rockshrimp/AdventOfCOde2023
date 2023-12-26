from typing import List
import math
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

    instructions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        node_name, children_str = lines[i].split(' = (')
        children = children_str[:-1].split(', ')
        print(children)
        nodes[node_name] = children

    current_node = 'AAA'
    i = 0
    while current_node != 'ZZZ':
        instruction = instructions[i % len(instructions)]
        current_node = nodes[current_node][1 if instruction == 'R' else 0]
        i += 1

    print(i)
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

    class Node:
        left = None

    instructions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        node_name, children_str = lines[i].split(' = (')
        children = children_str[:-1].split(', ')
        nodes[node_name] = children

    current_nodes = [node for node in list(nodes.keys()) if node[-1] == 'A']
    looping_indexes: List[int] = []
    for current_node in current_nodes:
        i = 0
        while True:
            instruction = instructions[i % len(instructions)]
            current_node = nodes[current_node][1 if instruction == 'R' else 0]

            if current_node[-1] == 'Z':
                looping_indexes.append(i + 1)
                break
            i += 1
    print(math.lcm(*looping_indexes))
part_2()
