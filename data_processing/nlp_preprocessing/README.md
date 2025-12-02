# Oil & Gas Engineering Dataset Processing (NLP Preprocessing)

This project provides a **data processing and NLP preprocessing pipeline** for the Oil & Gas Engineering dataset from HuggingFace. It includes dataset loading, cleaning, normalization, basic EDA, and text preprocessing for downstream NLP tasks.

📂 **Project Path:**
`python-mini-projects/data_processing/nlp_preprocessing/nlp_preprocessing.ipynb`

🔗 **GitHub Repository:**
[https://github.com/sobhankohanpour/python-mini-projects](https://github.com/sobhankohanpour/python-mini-projects.git)


## Features

* Load the HuggingFace Oil & Gas Engineering dataset
* Convert dataset to **pandas DataFrame**
* Normalize column names
* Clean and preprocess text data
* Handle missing or empty rows
* Basic **Exploratory Data Analysis (EDA)**:

  * Label distribution
  * Text length statistics
  * Random sample preview
* Save cleaned dataset to **Excel**
* Prepare text for NLP models (lowercasing, punctuation removal, whitespace normalization)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sobhankohanpour/python-mini-projects.git
cd python-mini-projects/data_processing/nlp_preprocessing
```

2. Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```


## Usage

1. Open the Jupyter Notebook:

```bash
jupyter notebook nlp_preprocessing.ipynb
```

2. Run cells sequentially
