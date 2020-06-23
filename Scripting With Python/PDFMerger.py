import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf_file in pdf_list:
        merger.append(pdf_file)
    merger.write('pdf_files\\Merged.pdf')


pdf_merger(inputs)
