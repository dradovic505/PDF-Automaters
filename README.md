#PDF Combiner:

This program takes PDFs (no other file type is supported) and combines them all into one PDF.

To run it:

Install PyPDF2 using pip install PyPDF2.
Run the program in the command line. 
The arguments can be either the absolute path of a folder from which you want all PDFs 
in that folder to be cominbed into one, or it can the a list of the PDFs you want to combine within the current working
directory.

example 1:
        python3 combine_pdf.py /Users/Home/Desktop/My_Folder
    
In example 1, the files will be appended in ascending alphanumerical order and output.txt will be stored in My_Folder.

example 2:
        python3 combine_pdf.py file1.pdf file2.pdf file3.pdf
    
In example 2, the files will be appended in the order they are written in the command line and stored in the current working directory.

#PDF Splitter:

This program takes a single PDF (no other file type is supported) and splits it into separate PDFs, one PDF for each page.

To run it:

Install PyPDF2 using pip install PyPDF2.
Run the program in the command line.
The argument is the name of the PDF you wish to split, with or with the absolute path. If the absolute path is not included,
the program will search for the file within the current working directory.
The output PDFs will contain one page each and will be named [input PDF's name]_[page_number].pdf

example 1:
    python3 combine_pdf.py file1.pdf

In example 1, the output files will be stored in the current working directory.

example 2:
    python3 combine_pdf.py /Users/Home/Desktop/My_Folder/file1.pdf

In example 2, the output files will be stored in My_Folder.
