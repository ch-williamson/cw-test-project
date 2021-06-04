# File: getters/occupations_skills.py
"""Data getters for the occupations/skills datasets.

Data source: email correspondence
"""

import pandas as pd
import json


def get_occupations() -> pd.DataFrame:
    """Load occupation table.

    Returns: DataFrame with information about occupations
    and their associated ISCO codes.
    """

    return pd.read_csv("./inputs/data/occupations_en.csv")


def get_skills() -> pd.DataFrame:
    """Load skill table.

    Returns: DataFrame with information about skills.
    """

    return pd.read_csv("./inputs/data/skills_en.csv")


def get_mapping() -> dict:
    """Load map of occupations to skills.

    Returns: Dictionary with occupations as indexes.
    Associated information includes skills.
    """

    with open("./inputs/data/ESCO_occup_skills.json") as json_file:
        return json.load(json_file)


# TESTING
# test_data = get_occupations()
# print(test_data.head())
