# Computational Design of RNA Thermoswitches for High-Temperature Genetic Control in *Bacillus subtilis*

**MSc Thesis Project — University of Aberdeen (Distinction)**  
**Author:** Md Abir Hossain

This repository presents an MSc research project focused on the computational design of RNA thermoswitches that remain functionally controlled at high temperatures in *Bacillus subtilis*. The work combines **thermodynamic sequence design using NUPACK** with **feature-based machine learning workflows** to identify and prioritise promising candidate switches for downstream experimental validation.

---

## Project Overview

RNA thermoswitches are regulatory RNA elements whose structure changes with temperature, enabling temperature-responsive gene control. Most existing systems are designed for moderate temperatures, while this project focuses on **high-temperature genetic control above 70°C**.

The workflow was designed to:
- generate candidate RNA thermoswitch sequences computationally
- simulate structural behaviour across multiple temperatures
- extract thermodynamic and sequence-derived features
- rank candidates using machine learning-assisted prioritisation
- reduce a large design space into a shortlist suitable for synthesis and testing

This project brings together **computational biology**, **thermodynamic modelling**, and **data-driven candidate ranking** in a reproducible research pipeline.

---

## Key Contributions

- Designed and screened **700+ RNA thermoswitch candidates** using Python-based computational workflows
- Simulated RNA secondary structure behaviour using **NUPACK 4.0**
- Engineered thermodynamic and sequence-derived features for candidate evaluation
- Trained a candidate-screening classifier and assessed ranking performance
- Applied calibration and shortlist selection workflows to improve prioritisation quality
- Reduced the candidate pool to a **final shortlist of 20 thermoswitches** for potential synthesis and experimental validation

---

## Technical Approach

The project combines:

- **Thermodynamic modelling:** RNA structure prediction and ensemble behaviour analysis across multiple temperatures
- **Feature engineering:** GC content, structural descriptors, motif-based and sequence-derived properties
- **Machine learning:** candidate prioritisation and ranking based on extracted features
- **Decision support:** shortlist generation for downstream experimental follow-up

---

## Selected Results

- Candidate screening classifier developed for shortlist prioritisation
- Example evaluation metrics:
  - **ROC-AUC:** 0.61
  - **PR-AUC:** 0.275
- Final synthesis-oriented shortlist produced from a larger computational candidate space

> These results should be interpreted as part of a research-stage prioritisation workflow rather than a standalone biological validation outcome.

---

## Tech Stack

- **Programming:** Python, NumPy, pandas
- **Machine Learning:** scikit-learn
- **Simulation / Modelling:** NUPACK 4.0
- **Workflow / Analysis:** Jupyter Notebook, Matplotlib

---

## Repository Structure

```text
rna-thermoswitch/
├── data/                  # Input, intermediate, and processed data
├── library_100/           # Candidate library generation and design outputs
├── library_700/           # Expanded candidate pool and screening files
├── notebooks/             # Main analysis and modelling notebooks
├── results/               # Model outputs, rankings, and selected candidates
├── supplementary_figures/ # Additional project figures and visual summaries
└── README.md
