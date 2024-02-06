import re
from copy import deepcopy

file_path = 'input.txt'
with open(file_path, 'r') as file:
    lines = file.read().splitlines()

workflows = []
while lines:
    line = lines.pop(0)
    if not line:
        break
    else:
        workflows.append(line)
parts = lines

def build_workflows_dic(workflows):
    workflows_dic = {}
    for workflow in workflows:
        name, rules_str = workflow[:-1].split('{')
        rules = rules_str.split(',')
        workflow_list = []
        for rule in rules:
            if '>' in rule or '<' in rule:
                category_name, criteria = re.split('<|>', rule)
                workflow_list.append((category_name, rule[len(category_name)] + criteria))
            else:
                workflow_list.append((rule, '-1'))
        workflows_dic[name] = workflow_list
    return workflows_dic

def build_part_dic(part):
    part_dic = {}
    for rating in part[1:-1].split(','):
        name, val = rating.split('=')
        part_dic[name] = int(val)
    return part_dic

def get_score():
    workflows_dic = build_workflows_dic(workflows)

    score = 0
    for part in parts:
        part_dic = build_part_dic(part)
        current_workflow = 'in'

        while current_workflow != 'A' and current_workflow != 'R':
            current_list = workflows_dic[current_workflow]
            for key, val in current_list:
                if val == '-1':
                    current_workflow = key
                    break
                else:
                    part_value = part_dic[key]
                    criteria, destination = val.split(':')
                    if '<' in criteria:
                        if part_value < int(criteria[1:]):
                            current_workflow = destination
                            break
                    elif '>' in criteria:
                        if part_value > int(criteria[1:]):
                            current_workflow = destination
                            break

        if current_workflow == 'A':
            score += sum(part_dic.values())
    return score

def part_1():
    print(get_score())
#part_1()


def get_combinations():
    workflows_dic = build_workflows_dic(workflows)
    possible_values = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    current_workflow = 'in'
    path_queue = [(current_workflow, possible_values)]
    valid_paths = []
    while path_queue:
        workflow_name, possible_values = path_queue.pop(0)
        for key, val in workflows_dic[workflow_name]:
            if val == '-1':
                if key == 'A':
                    valid_paths.append(deepcopy(possible_values))
                    break
                elif key != 'R':
                    path_queue.append((key, deepcopy(possible_values)))
            else:
                criteria, destination = val.split(':')
                if '<' in criteria:
                    valid_criteria_values = deepcopy(possible_values)
                    valid_criteria_values[key][1] = int(criteria[1:]) - 1
                    possible_values[key][0] = int(criteria[1:])

                    if destination == 'A':
                        valid_paths.append(valid_criteria_values)
                    elif destination != 'R':
                        possible_values[key][0] = int(criteria[1:])
                        path_queue.append((destination, valid_criteria_values))

                elif '>' in criteria:
                    valid_criteria_values = deepcopy(possible_values)
                    valid_criteria_values[key][0] = int(criteria[1:]) + 1
                    possible_values[key][1] = int(criteria[1:])
                    if destination == 'A':
                        valid_paths.append(valid_criteria_values)
                    elif destination != 'R':
                        path_queue.append((destination, deepcopy(valid_criteria_values)))
    return get_score(valid_paths)


def get_score(valid_paths):
    total = 0
    for path in valid_paths:
        combinations = 1
        for min_val, max_val in path.values():
            print(min_val, max_val)
            combinations *= max_val - min_val + 1
        total += combinations
    return total


def part_2():
    print(get_combinations())

part_2()