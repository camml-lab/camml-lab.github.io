---
title: "tensorial"
summary: "Machine learning on physical tensors: equivariant graph neural networks and machine-learned interatomic potentials in JAX."
weight: 10
tags: ["JAX", "e3nn-jax", "Equivariant NNs", "MLIPs"]
install: "pip install tensorial"
license: "AGPL-3.0"
links:
  docs: "https://tensorial.readthedocs.io/en/latest/"
  github: "https://github.com/camml-lab/tensorial"
  pypi: "https://pypi.org/project/tensorial/"
  website: ""
---

tensorial is an open-source Python library for machine learning on physical tensors. It combines JAX-based numerical tooling with geometric and equivariant model components, with a focus on atomistic and materials applications.

It is built for tensor-valued representations and symmetry-aware learning, which makes it well suited to molecular and materials modelling, graph-based neural networks and other physics-informed machine-learning workflows.

Highlights:

- **`tensorial.gcnn`**: building blocks for equivariant graph neural networks
- **`tensorial.mlip`**: tools for building and training machine-learned interatomic potentials
- Built on [JAX](https://github.com/jax-ml/jax), [e3nn-jax](https://github.com/e3nn/e3nn-jax) and [Flax](https://github.com/google/flax)
