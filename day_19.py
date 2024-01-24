import re

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
            print(current_workflow, current_list)
            for key, val in current_list:
                if val == '-1':
                    current_workflow = key
                    break
                else:
                    part_value = part_dic[key]
                    criteria, destination = val.split(':')
                    if '<' in criteria:
                        print(part_value, criteria, destination)
                        if part_value < int(criteria[1:]):
                            current_workflow = destination
                            break
                    elif '>' in criteria:
                        print(part_value, criteria, destination)
                        if part_value > int(criteria[1:]):
                            current_workflow = destination
                            break
        print(current_workflow, '\n')

        if current_workflow == 'A':
            score += sum(part_dic.values())
    return score

def part_1():
    print(get_score())
part_1()