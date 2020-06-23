import PyPDF2

input_file = PyPDF2.PdfFileReader(open('pdf_files\\Merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('pdf_files\\wtr.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()

for i in range(input_file.getNumPages()):
    page = input_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)

    with open('pdf_files\\WaterMarked.pdf', 'wb') as output_file:
        writer.write(output_file)
