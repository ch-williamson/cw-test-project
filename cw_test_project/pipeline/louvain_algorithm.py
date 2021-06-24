# File: utils/louvain_algorithm.py
"""Functions applying the Louvain algorithm to an occupation graph
to generate a dictionary categorising the nodes of the graph.

"""

from networkx.algorithms import community
from community import community_louvain

from cw_test_project.utils.invert_dictionary import invert_dictionary


def apply_louvain(graph) -> dict:
    """Apply Louvain to a graph and form a dictionary from categories to values.

    Returns: A dictionary where the keys are the labels of the Louvain clusters
    and the values are the nodes in each cluster.
    """
    partition = community_louvain.best_partition(graph)
    return invert_dictionary(partition)


def split_deeper(graph, dictionary, k=1) -> dict:
    """Given a graph and a dictionary, for each key, apply Louvain to the subgraph induced
    by the values of that key with respect to the graph. Repeat k times.

    Returns: A dictionary classifying occupations into a hierarchy with k+1 levels.
    """
    split_dictionary = {}
    for i in dictionary.keys():
        subgraph = graph.subgraph(dictionary[i])  # the induced subgraph
        split_dictionary[i] = apply_louvain(subgraph)
        if k > 1:
            split_dictionary[i] = split_deeper(graph, split_dictionary[i], k - 1)
    return split_dictionary
