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
        child_bags = [(i.strip().split(' ', 1)) for i in child_bags]
        G.add_weighted_edges_from([(parent_bag, node[1], node[0]) for node in child_bags])

    dfs_walk = nx.bfs_tree(G, 'shiny gold')
    sum = 0
    for node in dfs_walk:
        if node == 'shiny gold':
            continue
        paths = list(nx.all_simple_paths(G, 'shiny gold', node))
        for path in paths:
            if len(path) == 1:
                cur_weight = int(G.get_edge_data('shiny gold', path[0])['weight'])
                sum += cur_weight
            else:
                weight = 1
                for i in range(len(path) - 1):
                    cur_weight = int(G.get_edge_data(path[i], path[i + 1])['weight'])
                    weight *= cur_weight
                    # print(path)
                    # print(f'suly: {weight}')
                sum += weight

    print(sum)


    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # print(G.nodes)
    fig = matplotlib.pyplot.gcf()
    # fig.set_size_inches(15, 15, forward=True)
    fig.savefig('test2png.png', dpi=100)
    plt.show()
