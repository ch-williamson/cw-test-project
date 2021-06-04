# File: pipeline/make_graph.py
"""Takes the dictionary built in pipeline/generate_dictionary.py and forms
a graph to encode the similarities between skills required by occupations.
"""

import networkx as nx

from cw_test_project.pipeline.generate_dictionary import generate_dictionary


def make_graph() -> nx.Graph:
    """Make a graph from the dictionary of occupations to skills.

    Returns: A graph where the nodes are occupations,
    edges exist between nodes if the corresponding occupations share at least one skill,
    and edge weights are equal to the proportion of skills shared.
    """

    skills_dict = generate_dictionary()

    # the nodes of the graph are the occupations
    occupations = list(skills_dict.keys())

    # build the edge set
    edges = []

    number_of_occs = len(occupations)

    # consider each unique pair of occupations
    for i in range(0, number_of_occs - 1):
        for j in range(i + 1, number_of_occs):

            occupation_i = occupations[i]
            occupation_j = occupations[j]

            # get the skills associated with each occupation
            i_skills = set(skills_dict[occupation_i])
            j_skills = set(skills_dict[occupation_j])

            # find the proportion of shared skills
            intersection = i_skills & j_skills
            union = i_skills | j_skills

            proportion = len(intersection) / len(union)

            # if this proportion is nonzero, add an edge between these
            # occupations with weight equal to the proportion
            if proportion != 0:
                edges.append((occupation_i, occupation_j, {"weight": proportion}))

    # initialise an empty graph, then add nodes and edges as defined above
    occupations_graph = nx.Graph()

    occupations_graph.add_nodes_from(occupations)
    occupations_graph.add_edges_from(edges)

    return occupations_graph


# TESTING
# test_graph = make_graph()
# print(test_graph.degree('technical director'))
