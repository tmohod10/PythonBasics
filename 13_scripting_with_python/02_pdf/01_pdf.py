import PyPDF2

# to read the binary of the PDF file
# we use mode = "rb"

# we are using PyPDF2 -version 1.26.0
# the method PdfFileReader() is not available in Python 3.0 or
# higher versions

with open("dummy.pdf", mode="rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    # print the total number of pages
    print(reader.numPages)

    # to get the page
    print(reader.getPage(0))

    # to rotate the page
    page = reader.getPage(0)
    print(page.rotateCounterClockwise(90))

    # to make this change permanent in the file
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf", mode="wb") as new_file:
        writer.write(new_file)
