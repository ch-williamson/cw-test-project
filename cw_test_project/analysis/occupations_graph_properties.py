# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     comment_magics: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from networkx.algorithms import components
import matplotlib.pyplot as plt

from cw_test_project.pipeline.occupation_graph import make_graph

full_graph = make_graph()

# %% [markdown]
# full_graph is a weighted graph in which the nodes are occupations and edges exist between nodes if their occupations have skills in common. The weight of each edge is the proportion of skills that are shared between the two occupations.
#
# The graph consists of one large component and four singleton components:

# %%
cpt_sizes = [
    len(component) for component in list(components.connected_components(full_graph))
]

print(cpt_sizes)

# %% [markdown]
# The singleton components are as follows:

# %%
isolated_occs = [occ for occ in full_graph.nodes() if full_graph.degree(occ) == 0]

print(isolated_occs)

# %% [markdown]
# The following is a plot of the degrees of the graph:

# %%
degrees = [full_graph.degree(occ) for occ in full_graph.nodes()]

plt.hist(degrees)
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degrees of nodes of occupation graph")
plt.savefig("../../outputs/node_degrees.png")

# %% [markdown]
# We can see that some nodes have degrees over 1000, corresponding to occupations that share skills with over 1000 other occupations.
