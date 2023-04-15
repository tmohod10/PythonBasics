import PyPDF2
from sys import argv

# we are using PyPDF2 -version 1.26.0

inputs = argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write("super.pdf")


pdf_combiner(inputs)
