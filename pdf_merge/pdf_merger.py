import PyPDF2
import sys
import os

def merge_pdfs(file1, file2, output_file):
    merger = PyPDF2.PdfMerger(strict=False)

   
    merger.append(file1)
    merger.append(file2)

    merger.write(output_file)

if __name__ == "__main__":
    # Replace 'file1.pdf', 'file2.pdf', and 'output.pdf' with your file names
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    out_file = sys.argv[3]
    merge_pdfs(file_1, file_2, out_file)
