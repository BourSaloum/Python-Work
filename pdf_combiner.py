from PyPDF2 import PdfFileWriter, PdfFileReader

contenu_sortie = PdfFileWriter()
fichier_pdf_presentation = open("presentation.pdf", "rb")
fichier_pdf_recap = open("recap.pdf", "rb")

reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

print(f"Nombre de pages : {reader_recap.getNumPages()}")

contenu_sortie.addPage(reader_presentation.getPage(0))
for i in range (reader_recap.getNumPages()):
    contenu_sortie.addPage(reader_recap.getPage(i))

fichier_sortie = open("fichier_sortie.pdf", "wb")
contenu_sortie.write(fichier_sortie)

fichier_sortie.close()
fichier_pdf_presentation.close()
fichier_pdf_recap.close()