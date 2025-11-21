"""
extract_features.py

Placeholder script for extracting thermodynamic and sequence features
from RNA thermoswitch libraries using NUPACK.

The full working implementation is in:
- notebooks/01_thermoswitch_pipeline.ipynb
"""

import pandas as pd


def extract_features(input_csv: str, output_csv: str) -> None:
    """
    Placeholder function for feature extraction.

    Parameters
    ----------
    input_csv : str
        Path to input CSV with RNA sequences.
    output_csv : str
        Path to output CSV where features will be stored.

    Notes
    -----
    In the notebook, this step:
    - Calls NUPACK to compute thermodynamic properties
    - Builds k-mer and GC-based features
    - Writes features for downstream ML.
    """
    # TODO: Move the real feature extraction code here from the notebook.
    raise NotImplementedError(
        "Feature extraction is implemented in notebooks/01_thermoswitch_pipeline.ipynb"
    )


if __name__ == "__main__":
    print(
        "extract_features.py is a placeholder. "
        "See notebooks/01_thermoswitch_pipeline.ipynb for details."
    )
