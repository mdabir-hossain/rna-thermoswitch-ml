"""
train_model.py

Placeholder script for training a Gradient Boosting model on
RNA thermoswitch features and generating prediction files.

The full training pipeline is implemented in:
- notebooks/01_thermoswitch_pipeline.ipynb
"""

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier  # type: ignore


def train_model(features_csv: str, predictions_csv: str) -> None:
    """
    Placeholder function for model training and prediction.

    Parameters
    ----------
    features_csv : str
        Path to CSV containing engineered features.
    predictions_csv : str
        Path where model predictions (e.g. ml_predictions.csv) will be saved.

    Notes
    -----
    In the notebook, this step:
    - Trains GradientBoostingClassifier
    - Evaluates ROC-AUC / PR-AUC
    - Generates ml_predictions.csv for ranking and Top-K selection.
    """
    # TODO: Move the real training code here from the notebook.
    raise NotImplementedError(
        "Model training is implemented in notebooks/01_thermoswitch_pipeline.ipynb"
    )


if __name__ == "__main__":
    print(
        "train_model.py is a placeholder. "
        "See notebooks/01_thermoswitch_pipeline.ipynb for the full ML pipeline."
    )
