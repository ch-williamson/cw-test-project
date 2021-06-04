# File: pipeline/generate_dictionary.py
"""Restructures and extracts useful data from the full datasets
obtained in getters/occupations_skills.py.
"""

from cw_test_project.getters.occupations_skills import get_occupations, get_mapping


def generate_dictionary() -> dict:
    """Generate a slimmed-down occupation-to-skill dictionary.

    Returns: Dictionary where keys are occupations
    and values are skills associated with each occupation.
    """

    occupation_df = get_occupations()
    full_dict = get_mapping()

    labels = occupation_df["preferredLabel"].tolist()

    skills_dict = {}

    # .get() avoids errors when an occupation has no associated skills
    # by returning an empty list/set if none exists
    for occupation in labels:
        associated_skills = [
            info.get("title", [])
            for info in full_dict[occupation]["_links"].get("hasEssentialSkill", {})
        ]

        skills_dict[occupation] = associated_skills

    return skills_dict


# TESTING
# test_dict = generate_dictionary()
# print(test_dict['technical director'])
# print(list(test_dict.keys())[5])
