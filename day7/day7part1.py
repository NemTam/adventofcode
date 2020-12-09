import matplotlib
import networkx as nx
import matplotlib.pyplot as plt

from pprint import pprint

with open('day7_input', 'r') as f:
    G = nx.DiGraph()
    for line in f:
        if line == "\n":
            break
        parent_bag = line.partition("bags")[0].strip()
        if "contain no other bags" in line:
            G.add_node(parent_bag)
            continue
        child_bags = line.strip().partition("bags")[-1].strip().replace('contain', '').replace('bags', '').replace(
            '.', '').replace('bag', '').split(',')
        # Removing the number for first excercise:
        child_bags = {i.strip().partition(' ')[-1] for i in child_bags}
        G.add_edges_from([(parent_bag, node) for node in child_bags])


    gold_parents= ((list(nx.edge_dfs(G, 'shiny gold', orientation='reverse'))))
    result = {node[0] for node in gold_parents}
    pprint(result)
    print(len(result))
    nx.draw(G, with_labels=True)
    # print(G.nodes)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(20, 20, forward=True)
    fig.savefig('test2png.png', dpi=100)
    plt.show()

