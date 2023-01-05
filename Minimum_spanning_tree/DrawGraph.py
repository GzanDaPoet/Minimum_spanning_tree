import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(listEdge, url):
    G = nx.Graph()
    plt.clf()
    for u, ver, weightVar in listEdge:
        G.add_edge(u , ver , weight=weightVar)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 4]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 4]

    pos = nx.spring_layout(G, seed=10)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(url)
