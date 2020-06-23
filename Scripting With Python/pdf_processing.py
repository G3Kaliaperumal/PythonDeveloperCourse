import PyPDF2

# rb -> Read file in binary mode
with open('pdf_files\\dummy.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0).rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdf_files\\rotated.pdf', 'wb') as new_file:
        writer.write(new_file)
