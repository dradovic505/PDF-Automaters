#Python3
import PyPDF2, sys

pdf1 = open(sys.argv[1], 'rb')
in1 = PyPDF2.PdfFileReader(pdf1)
num_out = in1.numPages

#get pdf name without extension
pdfName = sys.argv[1]
extension_position = pdfName.find('.pdf')
if(extension_position != -1):
    pdfName = pdfName[0:pdfName.find('.pdf')]

#array of out files and writer
out_arr = [0] * num_out
writer_arr = [0] * num_out

#create new out file, get pg, write it to said file
for i in range(num_out):
    out_arr[i] = open(pdfName + '_' + str(i) + '.pdf', 'wb')
    pg = in1.getPage(i)
    writer_arr[i] = PyPDF2.PdfFileWriter()
    writer_arr[i].addPage(pg)
    writer_arr[i].write(out_arr[i])
    out_arr[i].close()

pdf1.close()
