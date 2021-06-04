# occupation hierarchy properties
# /analysis

import numpy as np
import pandas as pd

from cw_test_project.pipeline.make_cluster_dictionary import split_4levels
from cw_test_project.getters.occupations_skills import get_occupations


# flat_dict = pd.json_normalize(split_4levels, max_level=4, sep=", ")

flat_dict = {}

for i in split_4levels.keys():
    for j in split_4levels[i].keys():
        for k in split_4levels[i][j].keys():
            for l in split_4levels[i][j][k].keys():
                flat_dict[(i, j, k, l)] = split_4levels[i][j][k][l]


occupations = get_occupations()

isco_dict = {}

for group in set(occupations["iscoGroup"]):
    isco_dict[group] = occupations["preferredLabel"][occupations["iscoGroup"] == group]


new_sizes = [len(flat_dict[i]) for i in flat_dict.keys()]
isco_sizes = [len(isco_dict[i]) for i in isco_dict.keys()]

print("Number of new clusters:", len(new_sizes))
print("Number of ISCO clusters:", len(isco_sizes), "\n")

print("Mean size of new clusters:", np.mean(new_sizes))
print("Mean size of ISCO clusters:", np.mean(isco_sizes), "\n")

print("Standard deviation of new clusters:", np.std(new_sizes))
print("Standard deviation of ISCO clusters:", np.std(isco_sizes), "\n")

print("Number of new clusters of size 1:", len([i for i in new_sizes if i == 1]))
print("Number of ISCO clusters of size 1:", len([i for i in isco_sizes if i == 1]))
