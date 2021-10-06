#ARGUMENTS: absolute path of folder from which you want all PDFs combined
#               OR
#           PDFs user wishes to combine
#OUTPUT:    one PDF with all pages from all PDFs

import PyPDF2, os, sys, pdf_utils
from Context import Context

files = []

def combine_pdfs(pdf_arr, in_arr):
    writer = PyPDF2.PdfFileWriter()

    for i in range(len(in_arr)):
        pdf_arr[i] = open(files[i], 'rb')
        in_arr[i] = PyPDF2.PdfFileReader(pdf_arr[i])

        for pgNum in range(in_arr[i].numPages):
            pg = in_arr[i].getPage(pgNum)
            writer.addPage(pg)
    
    out = open(sys.argv[1] + 'output.pdf', 'wb')
    writer.write(out)
    out.close()
    for i in range(len(pdf_arr)):
        pdf_arr[i].close()


def main():
    fileOrDirectory = sys.argv[1]
    if not fileOrDirectory.endswith('/'):
        fileOrDirectory = fileOrDirectory + '/'
    
    extension_position = fileOrDirectory.find('.')

    # if first arg is a path, combine all PDFs in the top-level folder
    if extension_position == -1:
        pdf_utils.populate_files_for_path_arg(fileOrDirectory, files, Context.COMBINE_PDFS)
    # if first arg is not a path, assume the args are PDFs
    else:
        pdf_utils.populate_files_for_file_arg(fileOrDirectory)

    pdf_arr = [0] * (len(files))
    in_arr = [0] * (len(files))

    combine_pdfs(pdf_arr, in_arr)


if __name__ == '__main__':
    main()