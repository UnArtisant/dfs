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
        if v not in graph:
            graph[v] = []  # For undirected graph, ensure both nodes are present
        graph[u].append(v)
        graph[v].append(u)  # Because it's undirected
    return graph


def print_graph(graph, visited, current_node, stack):
    print("\nGraph Traversal State:")
    for node in graph:
        status = "Visited" if node in visited else "Not Visited"
        current = " <- Current Node" if node == current_node else ""
        print(f"Node {node}: {status}{current}")

    print("\nCurrent Stack:", stack)
    print("Visited Nodes:", visited)
    print("-" * 40)


def dfs(graph, start):
    visited = set()  # To track visited nodes
    stack = [start]  # Stack to hold nodes for traversal

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited
            print(f"\nVisiting node: {current_node}")
            print_graph(graph, visited, current_node, stack)

            # Add neighbors to the stack if they haven't been visited yet
            for neighbor in sorted(graph[current_node], reverse=True):
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)  # Add unvisited neighbors to the stack



file_path = 'dfs.txt'
edges = read_edges_from_file(file_path)
graph = create_graph(edges)

# Perform DFS starting from node 1 (or any other node)
dfs(graph, 1)
