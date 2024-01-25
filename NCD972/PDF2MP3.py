from PyPDF2 import PdfReader
from PyPDF2 import PdfFileWriter
document = PdfReader(open("Memory_Plainte_Retour.pdf", 'rb'))
metadata = document.metadata()
print (metadata)
