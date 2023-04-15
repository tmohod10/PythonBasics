import PyPDF2
from sys import argv


# we are using PyPDF2 -version 1.26.0


def add_watermark(pdf_file, watermark_pdf):
    # wm_instance = PyPDF2.PdfFileReader(watermark_pdf)
    wm_instance = PyPDF2.PdfFileReader(open(watermark_pdf, "rb"))
    wm_page = wm_instance.getPage(0)

    # pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, "rb"))
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_number in range(pdf_reader.getNumPages()):
        new_page = pdf_reader.getPage(page_number)
        new_page.mergePage(wm_page)
        pdf_writer.addPage(new_page)

        with open("super_watermarked.pdf", mode="wb") as file:
            pdf_writer.write(file)


if __name__ == "__main__":
    inputs = argv[1]
    watermarked_pdf = argv[2]
    add_watermark(inputs, watermarked_pdf)
