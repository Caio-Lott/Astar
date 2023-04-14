import pytest
from A_estrela import astar

@pytest.fixture
def graph():
    graph_data = []
    with open('Grafo.txt', 'r') as f:
        for line in f:
            a, b, weight = line.strip().split(';')
            graph_data.append((a, b, int(weight)))
    return graph_data

@pytest.fixture
def heuristic():
    heuristic_data = {}
    with open('Heuristica.txt', 'r') as f:
        for line in f:
            node, h = line.strip().split(';')
            heuristic_data[node] = int(h)
    return heuristic_data

def test_astar(graph, heuristic):
    def neighbors_fn(node):
        neighbors = []
        for a, b, _ in graph:
            if a == node:
                neighbors.append(b)
            elif b == node:
                neighbors.append(a)
        return neighbors

    assert astar('Arad', 'Bucareste', neighbors_fn, heuristic.get) == ['Arad', 'Sibiu', 'Fagaras', 'Bucareste']
