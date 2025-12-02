# PDF Merger 🗂️

A simple Python automation project to **merge multiple PDF files into a single PDF**.
This mini project is part of the `python-mini-projects` repository.


## Features

* Merge multiple PDFs from a folder into one PDF.
* Automatically sorts PDFs alphabetically before merging.
* Easy to use command-line interface.
* Lightweight and PEP8-compliant code.


## Project Structure

```text
python-mini-projects/
└── automation/
    └── pdf_merger/
        ├── pdf_merger.py
        ├── PDFs/
        ├── README.md
        └── requirements.txt
```


## Installation

1. **Clone the repository** (if not already):

```bash
git clone https://github.com/sobhankohanpour/python-mini-projects.git
cd python-mini-projects
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line:

```bash
python automation/pdf_merger/pdf_merger.py
```

You will be prompted to:

1. Enter the folder path containing the PDF files.
2. Enter the output file name (e.g., `merged.pdf`).

Example:

```
Enter the folder path containing PDFs: ./pdfs_to_merge
Enter the output file name (e.g., merged.pdf): merged_output.pdf
Merged PDF saved as: merged_output.pdf
```

## Contributing

Feel free to fork this project and add features like:

* Drag-and-drop GUI
* Merge PDFs in custom order
* Progress indicator for large files

## Acknowledgements

Built using [PyPDF2](https://pypi.org/project/PyPDF2/), a powerful Python library for PDF manipulation.
