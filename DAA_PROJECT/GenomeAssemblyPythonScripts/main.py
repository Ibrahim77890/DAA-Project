from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def read_debruijn_graph(filename):
    graph = defaultdict(list)
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            source, *destinations = line.split()
            graph[source].extend(destinations)
    return graph

def gUI_Graph(graph):
    # Create an empty graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Plot the graph
    pos = nx.spring_layout(G)  # Layout for the nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
    plt.title("De Bruijn Graph")
    plt.show()

if __name__ == "__main__":
    # Read the De Bruijn graph from the exported file
    debruijn_graph_filename = "../CommonFiles/debruijn_graph.txt"
    debruijn_graph = read_debruijn_graph(debruijn_graph_filename)

    # Print the graph (optional)
    print(debruijn_graph)

    # Display the graph in GUI
    gUI_Graph(graph=debruijn_graph)
