#Python3
import PyPDF2, sys

pdf1 = open(sys.argv[1], 'rb')
pdf2 = open(sys.argv[2], 'rb')
in1 = PyPDF2.PdfFileReader(pdf1)
in2 = PyPDF2.PdfFileReader(pdf2)
writer = PyPDF2.PdfFileWriter()

for pgNum in range(in1.numPages):
    pg = in1.getPage(pgNum)
    writer.addPage(pg)

for pgNum in range(in2.numPages):
    pg = in2.getPage(pgNum)
    writer.addPage(pg)

out = open(sys.argv[3], 'wb')
writer.write(out)
out.close()
pdf1.close()
pdf2.close()
