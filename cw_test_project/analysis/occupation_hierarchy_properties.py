# File: occupation_hierarchy_properties.py
"""Generates statistics relating to the occupation hierarchy.
"""

import numpy as np
import json

from cw_test_project.pipeline.make_cluster_dictionary import generate_4level_dict
from cw_test_project.pipeline.isco_dictionary import generate_isco_dict


dict_4levels = generate_4level_dict()
isco_dict = generate_isco_dict()

# TESTING
# print(dict_4levels[0])
# print(dict_4levels[5][0][0][0])


# Write 4 level dict to file for manual inspection:
with open("./outputs/data/classification.json", "w") as file:
    json.dump(dict_4levels, file, indent=4)


# It will be useful to 'squash' the dictionary into a single level
# for the sake of analysis
# This is a bit messy:

flat_dict = {}

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
print("Mean size of new clusters:", np.mean(new_sizes))
print("Mean size of ISCO clusters:", np.mean(isco_sizes), "\n")

# Standard deviation of group sizes:
print("Standard deviation of new clusters:", np.std(new_sizes))
print("Standard deviation of ISCO clusters:", np.std(isco_sizes), "\n")

# Number of singleton groups:
print("Number of new clusters of size 1:", len([i for i in new_sizes if i == 1]))
print("Number of ISCO clusters of size 1:", len([i for i in isco_sizes if i == 1]))
