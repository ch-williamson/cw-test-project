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
import numpy as np
import json

from cw_test_project.pipeline.make_cluster_dictionary import generate_4level_dict
from cw_test_project.pipeline.isco_dictionary import generate_isco_dict

dict_4levels = generate_4level_dict()
isco_dict = generate_isco_dict()

# %% [markdown]
# dict_4levels is a 4-level dictionary from categories to occupations. For instance, these are the occupations in the category (0, 0, 0, 0):

# %%
dict_4levels[0][0][0][0]

# %% [markdown]
# isco_dict is a dictionary from ISCO categories to the occupations within them. For instance, these are the occupations in ISCO category 1111:

# %%
isco_dict[1111]

# %% [markdown]
# We can analyse and compare the properties of both hierarchies:

# %%
flat_dict = {}

# First, 'squash' the dictionary into a single level
# This is a bit messy:

for i in dict_4levels.keys():
    for j in dict_4levels[i].keys():
        for k in dict_4levels[i][j].keys():
            for l in dict_4levels[i][j][k].keys():
                flat_dict[(i, j, k, l)] = dict_4levels[i][j][k][l]

# Something like this would be better, but I can't get it to work:
# flat_dict = pd.json_normalize(split_4levels, max_level=4, sep=", ")


new_sizes = [len(flat_dict[i]) for i in flat_dict.keys()]
isco_sizes = [len(isco_dict[i]) for i in isco_dict.keys()]

# Number of groups:
print("Number of new clusters:", len(new_sizes))
print("Number of ISCO clusters:", len(isco_sizes), "\n")

# Mean group size:
print("Mean size of new clusters:", round(np.mean(new_sizes), 2))
print("Mean size of ISCO clusters:", round(np.mean(isco_sizes), 2), "\n")

# Standard deviation of group sizes:
print("Standard deviation of new clusters:", round(np.std(new_sizes), 2))
print("Standard deviation of ISCO clusters:", round(np.std(isco_sizes), 2), "\n")

# Number of singleton groups:
print("Number of new clusters of size 1:", len([i for i in new_sizes if i == 1]))
print("Number of ISCO clusters of size 1:", len([i for i in isco_sizes if i == 1]))

# %% [markdown]
# We can see that the new hierarchy has fewer clusters which are larger on average than the ISCO hierarchy. Despite this, the clusters are more consistent sizes, as shown by the lower standard deviation. The new hierarchy also contains fewer singleton clusters than the ISCO hierarchy, which is beneficial as it means that more occupations in the new hierarchy have closely linked occupations.
