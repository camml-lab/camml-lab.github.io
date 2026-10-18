---
title: "Research"
description: "Physics-informed machine learning for the discovery and inverse design of materials and molecules"
layout: "simple"
---

For most of history, new materials have been found the way Edison found his light-bulb filament: by trial and error. Each candidate is made or simulated, tested, and usually discarded, and the space of possible materials is far too vast to explore this way. The CAMML team develops computational methods that change this, combining atomistic simulation with machine learning so that we can predict what atoms will do, and then ask which arrangements of atoms will do what we want.

## Physics-informed, equivariant machine learning

Standard machine-learning models find patterns in data, but they know nothing of the laws of physics. We build models that do. The behaviour of atoms is governed by fundamental symmetries: a molecule's energy doesn't change when it is rotated or translated, and its forces rotate with it. By building these symmetries directly into the architecture of **equivariant neural networks**, we obtain models that are faster to train, need far less data, and remain faithful to the physical systems they describe.

We are active members of the [e3nn](https://e3nn.org/) community, which develops open-source tools for Euclidean-equivariant neural networks.

## Accelerating quantum-mechanical calculations

Quantum-mechanical methods such as density-functional theory are the workhorse of computational materials science, but their cost limits how many candidate materials can be studied. We use physics-informed machine learning to predict the results of these calculations at a fraction of the cost, from interatomic potentials to electronic properties. A current focus is the search for new **spin-crossover materials**: compounds that switch between magnetic states in response to temperature, pressure or light, with potential applications in sensors, displays and data storage.

## Generative models for inverse design

Rather than asking "what are the properties of this material?", inverse design asks "which material has the properties we need?". We develop **generative models** that learn the patterns underlying known structures and use them to propose entirely new atomic arrangements, both crystals and molecules, that are statistically likely to have the target properties. This turns materials discovery from a search through candidates into a guided design process.

## Materials for the green transition

Materials science is a quiet engine of the energy transition. Next-generation metal–air batteries, more efficient catalysts and many other technologies we need to tackle the climate crisis are limited by how quickly we can explore materials space. The methods we develop are aimed squarely at speeding up that exploration.

## Where we are

CAMML is based at the [SIMaP](https://simap.grenoble-inp.fr/) laboratory in Grenoble, in the French Alps, where Martin Uhrin holds a [MIAI](https://miai.univ-grenoble-alpes.fr/) chair, *From Edison's trial-and-error approach to the inverse design of materials and molecules*. Grenoble is also home to large-scale experimental facilities such as the ESRF and the ILL, giving us close links between theory, computation and real-world materials.

Interested in joining us or collaborating? Get in touch with [Martin](/members/martin-uhrin/).
