#Python3
#ARGUMENTS: absolute path of folder from which you want all PDFs combined
#               OR
#           PDFs user wishes to combine
#OUTPUT:    one PDF with all pages from all PDFs

import PyPDF2, sys, os

#if first arg is a path, combine all PDFs in that folder
#if first arg is not a path, assume all args are PDFs to combine
name = sys.argv[1]
files = []
extension_position = name.find('.pdf')
if(extension_position == -1):   #if path
    if(os.path.exists(sys.argv[1]) == False):
        print("Invalid path. Need to enter an absolute path")
        sys.exit()
    for filename in os.listdir(name):
        #avoid output.pdf because that is the output file
        if filename.endswith('.pdf') and filename != 'output.pdf':
            files.append(filename)
    files.sort(key=str.lower)
else:
    files = [0] * (len(sys.argv)-1)
    for i in range(len(files)):
        files[i] = sys.argv[i+1]

pdf_arr = [0] * (len(files))
in_arr = [0] * (len(files))
writer = PyPDF2.PdfFileWriter()

for i in range(len(in_arr)):
    pdf_arr[i] = open(files[i], 'rb')
    in_arr[i] = PyPDF2.PdfFileReader(pdf_arr[i])
    #add each pg in the pdf to the writer
    for pgNum in range(in_arr[i].numPages):
        pg = in_arr[i].getPage(pgNum)
        writer.addPage(pg)

out = open('output.pdf', 'wb')
writer.write(out)
out.close()
for i in range(len(pdf_arr)):
    pdf_arr[i].close()
