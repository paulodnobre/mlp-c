import networkx as nx
import random

def generate_random_graph(n, m):
    """
    Generate a random graph with `n` vertices and `m` edges using the `networkx` library.

    Input:
    -----------
    n : int = The number of vertices to generate.
    m : int = The number of edges to generate.

    Output:
    --------
    nx.Graph = The generated graph object.

    """
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    edges = set()
    while len(edges) < m:
        a, b = random.sample(range(n), 2)
        if a != b:
            edges.add((min(a,b), max(a,b)))
    G.add_edges_from(list(edges))
    return G

def test_separation_degree(G):
    """
    Test the average separation degree between two vertices in a given graph object using the `networkx` library.

    Input:
    -----------
    G : nx.Graph = The graph object to test.

    Output:
    --------
    float = The average separation degree between two randomly sampled vertices in the graph.

    """
    degrees = []
    for i in range(100):
        a, b = random.sample(G.nodes(), 2)
        try:
            degree = nx.shortest_path_length(G, a, b)
            degrees.append(degree)
        except:
            pass
    return sum(degrees)/len(degrees)


G = generate_random_graph(10000, 20000000)
degree = test_separation_degree(G)
print(degree)

