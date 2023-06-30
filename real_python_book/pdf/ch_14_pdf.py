# In this chapter, you will learn how to:
# • Read text from a PDF
# • Extract pages and split a PDF into multiple files
# • Concatenate and Merge PDF files
# • Rotate and crop pages in a PDF file
# • Encrypt and Decrypt PDF files with passwords
# • Create a PDF file from scratch
# python3 -m pip install pypdf
# python3 -m pip show pypdf

from pathlib import Path

from ch14_pdf_chalenge1 import PdfFileSplitter
# Open a PDF File
from pypdf import PdfReader, PdfWriter

pdf_dir = (
    Path.cwd() / 'real_python' / 'python-basics-exercises-master' /
    'python-basics-exercises-master' / 'ch14-interact-with-pdf-files' /
    'practice_files'
)

pdf_path = pdf_dir / 'Pride_and_Prejudice.pdf'

reader = PdfReader(pdf_path)

# The PdfReader object does all of this for you, so you don’t need to
# worry about opening or closing the PDF file!
# the len(pdf.pages) atribute returns the number of pages
# contained in the PDF file:

print(len(reader.pages))
print(reader.metadata)
print(reader.metadata.title)

# The .metadata object contains the PDF metadata which is set
# when a PDF is created

# Extract Text From a Page
# There are two steps to extracting text from a single PDF page:
# 1. Get a PageObject with .pages property
# 2. Extract the text as a string with the PageObject instance’s
# .extractText() method.
# Pride_and_Prejudice.pdf has 243 pages. Each page has an index between
# 0 and 242. You can get an object representing a specific page by passing
# the page’s index to the PdfFileReader.getPage() method:
page = reader.pages[0]
print(page.extract_text())
print(type(page))

output_file = pdf_dir / 'pride_prejudice.txt'

with output_file.open(mode='w') as file:
    file.write(
        f'{reader.metadata.title}\n'
        f'Number of pages: {len(reader.pages)}\n\n'
    )

    for page in reader.pages[0:20]:
        file.write(page.extract_text())
# Extract Pages From a PDF
# The PdfFileWriter class is used to created a new PDF file.
writer = PdfWriter()
writer.add_blank_page(height=72, width=72)
# The width and height parameters are required and determine the width
# and height of the page in points. One point is equal to 1/72 inches.
# So the above code adds a one inch square blank page to pdf_writer.
new_pdf_file = pdf_dir / 'blank.pdf'
with new_pdf_file.open(mode='wb') as file:
    writer.write(file)
# PdfFileWriter objects can write to new PDF files, but they can’t create
# new content from scratch other than blank pages. This might seem
# like a big problem, but in many situations you don’t need to create
# new content. Often, you’ll work with pages extracted from PDF files
# that you’ve opened with a PdfFileReader instance.
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)
new_pdf_file = pdf_dir / 'first_page.pdf'
with new_pdf_file.open(mode='wb') as file:
    writer.write(file)

writer = PdfWriter()
for page in reader.pages[1:4]:
    writer.add_page(page)
print(len(writer.pages))
new_pdf_file = pdf_dir / 'cap_1.pdf'
with new_pdf_file.open(mode='wb') as file:
    writer.write(file)

# Review Exercises
# 1. Extract the last page from the Pride_and_Prejudice.pdf file and save
# it to a new file called last_page.pdf in your home directory.
pdf_path = pdf_dir / 'Pride_and_Prejudice.pdf'
reader = PdfReader(pdf_path)
last_page = reader.pages[-1]

writer = PdfWriter()
writer.add_page(last_page)

last_page_path = pdf_dir / 'last_page.pdf'
with last_page_path.open(mode="wb") as file:
    writer.write(file)
# 2. Extract all pages with even numbered indices from the Pride_-
# and_Prejudice.pdf and save them to a new file called every_other_-
# page.pdf in your home directory.
reader = PdfReader(pdf_path)

writer = PdfWriter()
for i in range(1, len(reader.pages), 2):
    page = reader.pages[i]
    writer.add_page(page)

every_other_path = pdf_dir / 'every_other_page.pdf'
with every_other_path.open(mode="wb") as file:
    writer.write(file)
# 3. Split the Pride_and_Prejudice.pdf file into two new PDF files. The
# first file should contain the first 150 pages, and the second file
# should contain the remaining pages. Save both files in your home
# directory as part_1.pdf and part_2.pdf.
reader = PdfReader(pdf_path)

writer = PdfWriter()
for i in range(150):
    page = reader.pages[i]
    writer.add_page(page)
part_1 = pdf_dir / 'part_1.pdf'
with part_1.open(mode="wb") as file:
    writer.write(file)

writer = PdfWriter()
for i in range(150, len(reader.pages)):
    page = reader.pages[i]
    writer.add_page(page)
part_2 = pdf_dir / 'part_2.pdf'
with part_2.open(mode="wb") as file:
    writer.write(file)
# Challenge: PdfFileSplitter Class
# Create a class called PdfFileSplitter that reads a PDF from an existing
# PdfFileReader instance and splits the PDF into two new PDFs.
# class PdfFileSplitter:
#     ...

# The class should be instantiated with a path string. For example,
# here’s how you would create a PdfFileSplitter instance from a PDF
# called mydoc.pdf in your current working directory:
# pdf_splitter = PdfFileSplitter("mydoc.pdf")
# class PdfFileSplitter:
#     def __init__(self, path) -> None:
#         self.path = Path(path)
# The PdfFileSplitter class should have two methods:
# 1. .split() that has a single parameter breakpoint that expects an
# integer representing the page number to split the PDF.
# After .split() is called, the PdfFileSplitter class should have
# an attribute .writer1 assigned to a PdfFileWriter instance containing
# all the pages in the original PDF up to but not including the
# breakpoint page, and .writer2 assigned to a PdfFileWriter instance
# containing the remaining pages in the original PDF.
# 2. .write() that has a single parameter filename that expects a path
# string.
# When .write() is called, two PDFs should be written to the
# specified path. The first one with the name filename + "_1.pdf"
# and the second with the name filename + "_2.pdf".
# For example, here’s how you would split the mydoc.pdf at page four:
# pdf_splitter.split(breakpoint=4)
# Then, to write two new PDFs in the current working directory as
# mydoc_split_1.pdf and mydoc_split_2.pdf, you would call .write() with
# the file name "mydoc_split":
# pdf_splitter.write("mydoc_split")
# Check that the splitter works by splitting the Pride_and_Prejudice.pdf
# file in the Chapter 14 Practice Files folder with the breakpoint at the
# 150th page.

file_path = 'real_python/python-basics-exercises-master/' \
    'python-basics-exercises-master/ch14-interact-with-pdf-files/' \
    'practice_files/Pride_and_Prejudice.pdf'

pdf_splitter = PdfFileSplitter(file_path)
pdf_splitter.split(100)
print(pdf_splitter.write('mydoc_split'))
