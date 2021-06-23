# File: pipeline/make_cluster_dictionary.py
"""Takes the graph built in pipeline/make_graph.py and applies
the Louvain clustering algorithm to obtain a hierarchy of occupations.
"""

from cw_test_project.pipeline.occupation_graph import make_graph
from cw_test_project.pipeline.louvain_algorithm import apply_louvain, split_deeper


def generate_4level_dict():
    full_graph = make_graph()
    dict_1level = apply_louvain(full_graph)
    dict_4levels = split_deeper(full_graph, dict_1level, k=3)
    return dict_4levels
