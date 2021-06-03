# occupations graph properties
# /analysis

from networkx.algorithms import components
import matplotlib.pyplot as plt

from cw_test_project.pipeline.make_graph import make_graph

full_graph = make_graph()


# sizes of connected components:

cpt_sizes = [
    len(component) for component in list(components.connected_components(full_graph))
]

print(cpt_sizes)


# isolated occupations:

isolated_occs = [occ for occ in full_graph.nodes() if full_graph.degree(occ) == 0]

print(isolated_occs)


# histogram of node degrees:

degrees = [full_graph.degree(occ) for occ in full_graph.nodes()]

plt.hist(degrees)
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degrees of nodes of occupation graph")
plt.savefig("../../outputs/node_degrees.png")
