import os
from PyPDF2 import PdfMerger


def get_pdf_files(folder_path):
    """
    Retrieve all PDF files in the specified folder.

    Args:
        folder_path (str): Path to the folder containing PDF files.

    Returns:
        list: Sorted list of PDF file paths.
    """
    pdf_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ]
    return sorted(pdf_files)


def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        pdf_files (list): List of PDF file paths to merge.
        output_path (str): Path for the merged output PDF.
    """
    merger = PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved as: {output_path}")


def main():
    """
    Main function to merge PDFs from a folder into one PDF.
    """
    folder_path = input("Enter the folder path containing PDFs: ").strip()
    output_path = input("Enter the output file name (e.g., merged.pdf): ").strip()

    if not os.path.exists(folder_path):
        print("Error: Folder path does not exist.")
        return

    pdf_files = get_pdf_files(folder_path)
    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    merge_pdfs(pdf_files, output_path)


if __name__ == "__main__":
    main()
