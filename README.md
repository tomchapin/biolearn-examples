# Biolearn Examples

This repository contains the code examples from
https://bio-learn.github.io/auto_examples/index.html

The code examples have been cleaned up according to the python style guide,
and have been configured in a standard python project that specifies a
python version (in the .python-version file), as well as all required
dependencies (in the requirements.txt file).

## Installation

1. Ensure that you have python 3.11.5 installed, and that it is active.
   To verify your python version, run `python --version`

2. Install dependencies via pip, by running `pip install `

## Generating Plots (Standard Python)

For plotting epigenetic clocks on geo:

```
cd 00_epigenetic_biomarkers
python plot_epigenetic_clocks_on_geo.py
open outputs/epigenetic_clocks_on_geo.png
``

For generating composite biomarkers with nhanes:

```
cd 01_composite_biomarkers
python plot_nhanes.py
open phenotypic_age_vs_chronological_age.png
open survival_by_phenotypic_age.png
``

## Jupyter Notebooks

Each of the folders also contains a corresponding Jupyter notebook,
if you would prefer to generate the plots that way.

To start Jupyter, run:

`jupyter notebook`

Then open the .ipynb file in the relevant folder, and hit the play button.