# 📘 RNA Thermoswitch Design using Machine Learning & NUPACK
MSc Data Science Project — University of Aberdeen (Distinction)
Author: Md Abir Hossain (mdabir-hossain)

## 🔬 Project Overview

This project explores the computational design of RNA thermoswitches that activate near 70°C using a combination of:

Machine Learning (Python, scikit-learn)

Thermodynamic simulation (NUPACK)

Feature engineering (k-mers, GC content, structural parameters)

Ranking and calibration pipelines

The goal was to design RNA sequences with favourable ON/OFF conformations at different temperatures, with a reproducible computational pipeline.

## 🧪 Key Results

Engineered 700+ synthetic RNA sequences using Python-based search.

Extracted thermodynamic features using NUPACK 4.0.

Trained Gradient Boosting Classifier achieving:

ROC-AUC: 0.951

PR-AUC: 0.875

Applied:

Isotonic calibration

Guard-banding filters

QC checks

3-mer Jaccard diversification

Produced a Top-20 final shortlist of candidate thermoswitches for synthesis.

## 🧰 Tech Stack

Programming: Python, NumPy, pandas

ML: scikit-learn (GradientBoostingClassifier)

Simulation: NUPACK

Tools: Jupyter Notebook, Matplotlib

## 📂 Repository Structure
rna-thermoswitch-ml/
│
├── data/
│   ├── sample_sequences.csv
│   ├── sample_features.csv
│
├── notebooks/
│   ├── 01_feature_extraction.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_calibration_ranking.ipynb
│
├── scripts/
│   ├── generate_sequences.py
│   ├── extract_features.py
│   ├── train_model.py
│
├── figures/
│   ├── roc_curve.png
│   ├── pr_curve.png
│   ├── correlation_heatmap.png
│
├── results/
│   ├── top20_candidates.csv
│
└── README.md

## 📄 Thesis PDF

Your full MSc project report is available here:

(Upload your PDF here — instructions below)

## 🚀 How to Reproduce

Install dependencies

Run NUPACK simulations

Extract features

Train model

Apply calibration + ranking

View final shortlist

## 🔖 Status

✔ Completed
✔ MSc Project
✔ Reproducible pipeline
✔ Future expansions planned
