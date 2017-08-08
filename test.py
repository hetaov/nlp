# encode=utf-8

from PyPDF2 import PdfFileWriter, PdfFileReader
import io

#output = PdfFileWriter()

#pdf = PdfFileReader(open('medcine.pdf', 'rb'))

file_r = io.open('medcine.pdf', 'r', encoding='gb18030')
'''
for i in xrange(pdf.getNumPages()):
    page = pdf.getPage(i)
    #print page
'''

for line in file_r.read():
    print line
