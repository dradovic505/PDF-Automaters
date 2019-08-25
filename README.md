# PDF-Automaters

PDF Combiner:

This program takes PDFs (no other file type is supported) and combines them all into one PDF.

To run it:

Install PyPDF2 using pip install PyPDF2
Run the program in the command line. 
The arguments can be either the absolute path of a folder from which you want all PDFs 
in that folder to be cominbed into one, or it can the a list of the PDFs you want to combine.
The output PDF will be named output.pdf.
The output PDF will be in the current working directory.

example 1:
    python3 combine_pdf.py /Users/daniloradovic/Desktop/My_Folder
    
In example 1, the files will be appended in ascending alphanumerical order.

example 2:
    python3 combine_pdf.py file1.pdf file2.pdf file3.pdf
    
In example 2, the files will be appended in the order they are written in the command line.

PDF Splitter:

This program takes a single PDF (no other file type is supported) and splits it into separate PDFs, one PDF for each page.

To run it:

Install PyPDF2 using pip install PyPDF2
Run the program in the command line. combine_pdf.py must be in the current working directory of the input file.
The argument is the name of the PDF you wish to split.
The output PDFs will contain one page each and will be named [input PDF's name]_[page_number].pdf
The output PDF will be in the current working directory.

example:
  python3 combine_pdf.py file1.pdf
