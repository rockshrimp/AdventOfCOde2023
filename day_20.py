from copy import deepcopy
from math import lcm

file_path = 'input.txt'

def get_predecessors(module):
    pred = []
    for source, destinations in signals_dic.items():
        if module in destinations[1]:
            pred.append(source)
    return pred

with open(file_path, 'r') as file:
    lines = file.read().splitlines()

signals_dic = {}
initial_state_dic = {'flip_flops': {}, 'conjunctions': {}}
for line in lines:
    source, dest = line.split(' -> ')
    dest_modules = dest.split(', ')
    if source == 'broadcaster':
        signals_dic[source] = (source, dest_modules)
    else:
        signals_dic[source[1:]] = (source[0], dest_modules)
        if source[0] == '%':
            initial_state_dic['flip_flops'][source[1:]] = 0
        else:
            initial_state_dic['conjunctions'][source[1:]] = {}

non_sending_modules = []
for module_name, dest in signals_dic.items():
    module_type, destinations = dest
    for destination in destinations:
        if destination in initial_state_dic['conjunctions']:
            initial_state_dic['conjunctions'][destination][module_name] = 0
        if destination not in signals_dic:
            non_sending_modules.append(destination)

print('initial_state_dic', initial_state_dic)
print('signals_dic', signals_dic)

for source, destinations in signals_dic.items():
    for dest in destinations[1]:
        if dest in initial_state_dic['conjunctions']:
            sorted(initial_state_dic['conjunctions'][dest]).append((source, 0))


def run_module_conf(signals_dic, flip_flops_state, conjunctions_state):
    low_pulses_count, high_pulses_count = 0, 0
    signals_queue = [('broadcaster', 0)]

    while signals_queue:
        source, pulse_value = signals_queue.pop(0)
        if source in non_sending_modules:
            continue
        if source == 'broadcaster':
            for dest in signals_dic[source][1]:
                signals_queue.append((dest, pulse_value))
                if dest in conjunctions_state:
                    conjunctions_state[dest][source] = pulse_value
                if pulse_value:
                    high_pulses_count += 1
                else:
                    low_pulses_count += 1
        elif signals_dic[source][0] == '%':
            if pulse_value == 0:
                flip_flops_state[source] ^= 1
                pulse_value = flip_flops_state[source]
                for dest in signals_dic[source][1]:
                    signals_queue.append((dest, pulse_value))
                    if dest in conjunctions_state:
                        conjunctions_state[dest][source] = pulse_value
                    if pulse_value:
                        high_pulses_count += 1
                    else:
                        low_pulses_count += 1
        elif signals_dic[source][0] == '&':
            connected_inputs = conjunctions_state[source]
            pulse_value = 0 if all(connected_inputs.values()) else 1
            for dest in signals_dic[source][1]:
                signals_queue.append((dest, pulse_value))
                if dest in conjunctions_state:
                    conjunctions_state[dest][source] = pulse_value
                if pulse_value:
                    high_pulses_count += 1
                else:
                    low_pulses_count += 1
    return low_pulses_count, high_pulses_count, flip_flops_state, conjunctions_state

def part_1():
    state_dic = deepcopy(initial_state_dic)
    flip_flops_state, conjunctions_state = state_dic['flip_flops'], state_dic['conjunctions']
    low_pulses_total, high_pulses_total = 0, 0
    for i in range(1000):
        low_pulses_count, high_pulses_count, flip_flops_state, conjunctions_state = run_module_conf(signals_dic, flip_flops_state, conjunctions_state)
        low_pulses_total += low_pulses_count + 1
        high_pulses_total += high_pulses_count
    print('Part 1', high_pulses_total * low_pulses_total)
part_1()


def run_module_conf(predecessor, flip_flops_state, conjunctions_state, signals_queue):
    signals_queue = [('broadcaster', 0)]
    while signals_queue:
        source, pulse_value = signals_queue.pop(0)
        if source in non_sending_modules:
            continue
        if source == 'broadcaster':
            for dest in signals_dic[source][1]:
                signals_queue.append((dest, pulse_value))
                if dest in conjunctions_state:
                    conjunctions_state[dest][source] = pulse_value
        elif signals_dic[source][0] == '%':
            if pulse_value == 0:
                flip_flops_state[source] ^= 1
                pulse_value = flip_flops_state[source]
                for dest in signals_dic[source][1]:
                    signals_queue.append((dest, pulse_value))
                    if dest in conjunctions_state:
                        conjunctions_state[dest][source] = pulse_value
        elif signals_dic[source][0] == '&':
            connected_inputs = conjunctions_state[source]
            pulse_value = 0 if all(connected_inputs.values()) else 1
            if source == predecessor and pulse_value == 1:
                return True, flip_flops_state, conjunctions_state
            for dest in signals_dic[source][1]:
                signals_queue.append((dest, pulse_value))
                if dest in conjunctions_state:
                    conjunctions_state[dest][source] = pulse_value
    return False, flip_flops_state, conjunctions_state


def part_2():
    rx_predecessors = get_predecessors('rx')
    predecessors_count = []
    for predecessor in get_predecessors(*rx_predecessors):
        counter = 0
        signals_queue = [('broadcaster', 0)]
        state_dic = deepcopy(initial_state_dic)
        flip_flops_state, conjunctions_state = state_dic['flip_flops'], state_dic['conjunctions']

        while True:
            counter += 1
            found, flip_flops_state, conjunctions_state = run_module_conf(predecessor, flip_flops_state, conjunctions_state, signals_queue)
            if found:
                predecessors_count.append(counter)
                break
    print(lcm(*predecessors_count))
part_2()