# File: pipeline/isco_dictionary.py
"""Function to produce a dictionary from ISCO category labels
to groups of occupations with that label.
"""

from cw_test_project.getters.occupations_skills import get_occupations


def generate_isco_dict() -> dict:
    occupations = get_occupations()
    isco_dict = {}
    for group in set(occupations["iscoGroup"]):
        isco_dict[group] = occupations["preferredLabel"][
            occupations["iscoGroup"] == group
        ]
    return isco_dict
