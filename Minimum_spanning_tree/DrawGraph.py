import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()


G.add_edge("0", "1", weight=1)
G.add_edge("0", "4", weight=4)
G.add_edge("0", "5", weight=5)
G.add_edge("1", "0", weight=1)
G.add_edge("1", "2", weight=1)
G.add_edge("1", "3", weight=2)
G.add_edge("2", "1", weight=1)
G.add_edge("2", "3", weight=5)
G.add_edge("2", "7", weight=7)
G.add_edge("3", "0", weight=4)
G.add_edge("0", "3", weight=5)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed")
# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
# ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
