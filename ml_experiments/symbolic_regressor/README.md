# Symbolic Regression with gplearn

This project demonstrates the use of `gplearn.genetic.SymbolicRegressor` for discovering underlying mathematical relationships in data. The code uses genetic programming to automatically generate a symbolic equation that best fits a dataset, making it a powerful tool for interpretable regression.


## Features

* Generate a synthetic dataset with a known non-linear relationship.
* Train a `SymbolicRegressor` model to find an analytical expression.
* Evaluate model performance using MSE and R² metrics.
* Visualize predictions versus actual values.


## Requirements

**Python Version:** 3.11

> ⚠️ Note: This project does **not** work with Python 3.13.

**Dependencies:**

```
numpy==1.24.4
scikit-learn==1.2.2
gplearn==0.4.2
pandas==2.3.3
openpyxl==3.1.5
matplotlib==3.7.2
```

You can install them using:

```bash
pip install -r requirements.txt
```


## Usage

1. Clone the repository.
2. Make sure you are using Python 3.11.
3. Install dependencies via `requirements.txt`.
4. Run the notebook or Python script to:

   * Generate the synthetic dataset.
   * Train the symbolic regression model.
   * Evaluate and visualize the results.


## Acknowledgements

* [`gplearn`](https://github.com/trevorstephens/gplearn) for symbolic regression with genetic programming.
* Python scientific computing libraries: `numpy`, `pandas`, `scikit-learn`, and `matplotlib`.
