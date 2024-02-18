from collections import defaultdict
from random import choice
from math import prod
from copy import deepcopy
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

components = defaultdict(list)
for line in lines:
    component, connexions = line.split(': ')
    for connexion in connexions.split(' '):
        components[component].append(connexion)
        components[connexion].append(component)

components = {k: [v, {k}] for k, v in components.items()}


def contract():
    subgraph_number = 2
    for i in range(100):
        graph = deepcopy(components)

        while len(graph) > subgraph_number:
            vertex = choice(list(graph.keys()))
            contract_vertex(graph, vertex)

        # Only three cuts made
        if len(list(graph.values())[0][0]) == 3:
            break
    print(prod([len(v[1]) for k, v in graph.items()]))

def contract_vertex(graph, vertex):
    vertex_2 = choice(graph[vertex][0])
    graph[vertex_2][0] = [v for v in graph[vertex_2][0] if v != vertex] + [v for v in graph[vertex][0] if v != vertex_2]

    for v in graph[vertex][0]:
        if v == vertex_2:
            continue
        graph[v][0].append(vertex_2)
        graph[v][0].remove(vertex)

    graph[vertex_2][1] = graph[vertex][1] | graph[vertex_2][1]
    del graph[vertex]

def part_1():
    contract()
part_1()
