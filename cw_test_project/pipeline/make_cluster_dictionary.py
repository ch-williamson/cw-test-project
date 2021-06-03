# make_cluster_dictionary.py

# for a given list of occupations,
# perform a louvain cluster on the subgraph induced by that list
# return a dictionary of categories to occupations

from networkx.algorithms import community
from community import community_louvain

from cw_test_project.pipeline.make_graph import make_graph
from cw_test_project.utils.invert_dictionary import invert_dictionary


full_graph = make_graph()


def apply_louvain(graph) -> dict:
    """Apply Louvain to a graph and form a dictionary from categories to values.

    Returns: A dictionary where the keys are the labels of the Louvain clusters
    and the values are the nodes in each cluster.
    """
    partition = community_louvain.best_partition(graph, randomize=False, random_state=0)
    return invert_dictionary(partition)


split_1level = apply_louvain(full_graph)


def split_deeper(dictionary, k=1) -> dict:
    """Given a dictionary, for each key, apply Louvain to the subgraph induced
    by the values of that key with respect to the full graph. Repeat k times.

    Returns: A dictionary classifying occupations into a hierarchy with k+1 levels.
    """
    split_dictionary = {}

    for i in dictionary.keys():
        subgraph = full_graph.subgraph(dictionary[i])  # the induced subgraph
        split_dictionary[i] = apply_louvain(subgraph)
        if k > 1:
            split_dictionary[i] = split_deeper(split_dictionary[i], k - 1)

    return split_dictionary


split_4levels = split_deeper(split_1level, k=3)

# test change

# TESTING
# print(split_4levels[0])
# print(split_4levels[5][0][0][0])
