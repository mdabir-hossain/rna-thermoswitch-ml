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
├── data/
│   ├── library_100.csv
│   ├── library2_100.csv
│   ├── library3_200.csv
│   ├── library4_300.csv
│   ├── library_combined.csv
│   ├── ml_predictions.csv
│   ├── ml_topK_diverse.csv
│   ├── ml_topK_diverse_clean.csv
│   ├── ml_topK_summary.csv
│   └── ml_order_sheet.csv
│
├── notebooks/
│   └── 01_thermoswitch_pipeline.ipynb
│
├── scripts/
│   └── (placeholder — add Python scripts later if needed)
│
├── figures/
│   └── Supplementary Figures.pdf
│
├── results/
│   └── (placeholder — add topK export later if needed)
│
├── Data Science Project_Md Abir Hossain_29 August.pdf
└── README.md

### File Descriptions
- library_100.csv — First generated thermoswitch library (100 sequences)
- library_combined.csv — Merged library used for ML training
- ml_predictions.csv — Model predictions on all candidate sequences
- ml_topK_diverse.csv — Diversified Top-K candidates
- Supplementary Figures.pdf — Full supplementary visual analysis

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
