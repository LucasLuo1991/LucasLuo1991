# A tool for merging front and back scans

## Description

My scanner does not support duplex scanning which means it can only scan either front sides or back sides of double-sided documents.

For example, I have a double-sided document which has page number 1 - 6. It scans page in the order of 1, 3 and 5 if I feed the doc to the printer with the front side upward. It scans page in the order of 6, 4 and 2 if it is back side upward. This tool is used to merge the two output files into a single one with pages in the order of 1-6.

## Environment

- Python 3
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## How to

1. Save the scan outputs as two PDF files e.g. `front.pdf` and `back.pdf`
2. Run the python script: `python merger.py front.pdf back.pdf`
3. The output file `document-output.pdf` can be found in the python script folder

> **Note**: `front.pdf` and `back.pdf` must have the same total number of pages. 
