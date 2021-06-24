# cw-test-project

## Project overview

This project aims to construct a new classification for occupations based on their skill requirements.

A list of occupations and the skills they require is used (sourced from ESCO). These are used to form a weighted graph in which the nodes are occupations and edges exist between nodes if their corresponding occupations have skills in common; the weight of an edge is equal to the proportion of their combined skills that are shared. A clustering algorithm (the Louvain algorithm) is then applied to the graph to obtain a categorisation of occupations into clusters with a high density of shared skills. This is repeated to obtain a hierarchy 4 levels deep (similar to the ISCO hierarchy).

## Setup

- Meet the data science cookiecutter [requirements](http://nestauk.github.io/ds-cookiecutter), in brief:
  - Install: `git-crypt`
  - Have a Nesta AWS account configured with `awscli`
- Run `make install` to configure the development environment:
  - Setup the conda environment
  - Configure pre-commit
  - Configure metaflow to use AWS

## Contributor guidelines

[Technical and working style guidelines](https://github.com/nestauk/ds-cookiecutter/blob/master/GUIDELINES.md)

---

<small><p>Project based on <a target="_blank" href="https://github.com/nestauk/ds-cookiecutter">Nesta's data science project template</a>
(<a href="http://nestauk.github.io/ds-cookiecutter">Read the docs here</a>).
</small>
