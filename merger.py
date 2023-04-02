from PyPDF2 import PdfWriter, PdfReader
import sys
import os

if len(sys.argv) != 3:
    sys.exit("Invalid input!")

if os.path.splitext(sys.argv[1])[1] != ".pdf" or os.path.splitext(sys.argv[2])[1] != ".pdf":
    sys.exit("Invaid file type!")

try:
    front_pdf = open(sys.argv[1], "rb")
    back_pdf = open(sys.argv[2], "rb")
except FileNotFoundError:
    sys.exit("Files cannot be opened!")

reader1 = PdfReader(front_pdf)
reader2 = PdfReader(back_pdf)
numpages = len(reader1.pages)
if numpages != len(reader2.pages):
    front_pdf.close()
    back_pdf.close()
    sys.exit("The numbers of pages of two files are different!")

merger = PdfWriter()

for n in range(numpages):
    merger.append(fileobj=front_pdf, pages=[n])
    merger.append(fileobj=back_pdf, pages=[numpages - n - 1])

output = open("document-output.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()
front_pdf.close()
back_pdf.close()
