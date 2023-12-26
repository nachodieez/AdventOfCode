from collections import defaultdict
import networkx as nx

with open("../data/day25.in") as f:
    ll = f.read().strip().split("\n")

# nacho!! no omites 3 nodos!! omites 3 conexiones!!
# BOBO!!!!
def graph(data, omit = []):
    g = defaultdict(list)
    for line in data:
        r, l = line.split(":")
        if r in omit:
            continue
        for node in l.strip().split(" "):
            if node in omit:
                continue
            g[r].append(node)
            # Each connection between two components is represented only once,
            # so some components might only ever appear on the left or right side of a colon.
            g[node].append(r)
    return g

def connection(data):
    g = []
    for line in data:
        r, l = line.split(":")
        for node in l.strip().split(" "):
            g.append((r, node))
    return g

connections = connection(ll)
print(f"Number of edges = {len(connections)}")

G = nx.Graph()

for line in ll:
    r, l = line.split(":")
    for node in l.strip().split(" "):
        G.add_edge(r, node, capacity=1.0)
        G.add_edge(node, r, capacity=1.0)

i = 0
for s in G.nodes:
    for t in G.nodes:
        if s != t:
            cut_value, partition = nx.minimum_cut(G, s, t)
            if cut_value == 3.0:
                break
    if cut_value == 3.0:
        break
print("Sol 1:", len(partition[0]) * len(partition[1]))
print("Sol 2:", ":(")



# for combination in combinations(connections, int(len(connections) - 3)):
#     G = nx.Graph(combination)
#     G.add_edges_from(combination)
#     d = list(nx.connected_components(G)) 

#     if len(d) == 2:
#         break

# print("Sol 1:", len(d[0]) * len(d[1]))


# obviusly, this only works with small data