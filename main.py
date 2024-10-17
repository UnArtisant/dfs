'''
Jorge Rodrigo Colín Rubio           | A01662960
Raphaël Marc Joseph Barriet	 	    | A01763686
Nicole Kapellmann Lepine		    | A01664563
'''

import re

def read_edges_from_file(filename):
    edges = []
    with open(filename, 'r') as file:
        content = file.read()
        matches = re.findall(r'\((\d+),(\d+)\)', content)
        for match in matches:
            u, v = map(int, match)
            edges.append((u, v))
    return edges

def create_graph(edges):
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


file_path = 'dfs.txt'
graph = read_edges_from_file(file_path)

# Perform DFS starting from node 1 (or any other node)
dfs(graph, 1)
