"""
generate_sequences.py

Placeholder script for generating synthetic RNA thermoswitch libraries.

The main implementation currently lives in:
- notebooks/01_thermoswitch_pipeline.ipynb

This module can be used in the future to:
- Generate sequence libraries under different design constraints
- Save libraries as CSV files (e.g. library_100.csv, library2_100.csv, etc.)
"""

import pandas as pd


def generate_library(output_path: str, n_sequences: int = 100) -> None:
    """
    Placeholder function for library generation.

    Parameters
    ----------
    output_path : str
        Path to the CSV file where the library will be saved.
    n_sequences : int, default=100
        Number of sequences to generate.

    Notes
    -----
    The real implementation is currently inside the Jupyter notebook.
    This function is here to show how the code could be modularised later.
    """
    # TODO: Move the actual generation code from the notebook into this function.
    raise NotImplementedError(
        "Library generation is implemented in notebooks/01_thermoswitch_pipeline.ipynb"
    )


if __name__ == "__main__":
    # Example usage (placeholder)
    print(
        "generate_sequences.py is a placeholder. "
        "See notebooks/01_thermoswitch_pipeline.ipynb for the full pipeline."
    )
