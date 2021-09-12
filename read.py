import PyPDF2
from PyPDF2 import pdf
from tabulate import tabulate
import time


#Abrindo arquivo em modo leitura e lendo o binario
#pdf_file = open('crono.pdf','rb')
#Após pegar binário, pegamos os dados de PDF desse binário
pdf_dados = PyPDF2.PdfFileReader(open('boleto_413819.pdf','rb'))


print('|||||||||||||||| Retorno de PyPDF2.PdfFileReader(pdf_file) ||||||||||||||||')
print(pdf_dados)

print('|||||||||||||||| Números de páginas a partir de str(pdf_dados.numPages): ', str(pdf_dados.numPages),'||||||||||||||||')
#Sertando a variavel pagina1 com o objeto pagina1
pagina1 = pdf_dados.getPage(0)
#pegando texto extraido da pagina 1
txt_pg1 = pagina1.extractText()

print('|||||||||||||||| Retorno de print(pagina1) ||||||||||||||||')
print(pagina1)


a = pdf_dados.getDocumentInfo()

print('|||||||||||||||| Retorno do método getDocumentInfo() ||||||||||||||||')
print(a)
print('|||||||||||||||| Retorno do método a.author ||||||||||||||||')
print(a.author)
print('|||||||||||||||| Retorno do método a.author_raw ||||||||||||||||')
print(a.author_raw)
print('|||||||||||||||| Retorno do método a.creator ||||||||||||||||')
print(a.creator)
print('|||||||||||||||| Retorno do método a.creator_raw ||||||||||||||||')
print(a.creator_raw)
print('|||||||||||||||| Retorno do método a.producer ||||||||||||||||')
print(a.producer)
print('|||||||||||||||| Retorno do método a.producer_raw ||||||||||||||||')
print(a.producer_raw)
print('|||||||||||||||| Retorno do método a.subject ||||||||||||||||')
print(a.subject)
print('|||||||||||||||| Retorno do método a.subject_raw ||||||||||||||||')
print(a.subject_raw)
print('|||||||||||||||| Retorno do método a.title ||||||||||||||||')
print(a.title)
print('|||||||||||||||| Retorno do método a.title_raw ||||||||||||||||')
print(a.title_raw)




b = pdf_dados.getPageLayout()

print('|||||||||||||||| Retorno do método getPageLayout() ||||||||||||||||')
print(b)


c = pdf_dados.getPageMode()

print('|||||||||||||||| Retorno do método getPageMode() ||||||||||||||||')
print(c)

d = pdf_dados.getNamedDestinations()
print('|||||||||||||||| Retorno do método getNamedDestinations() ||||||||||||||||')
print(d)


e = pdf_dados.getOutlines()

print('|||||||||||||||| Retorno do método getOutlines() ||||||||||||||||')
print(e)

f = pdf_dados.getFields()

print('|||||||||||||||| Retorno do método getFields() ||||||||||||||||')
print(f)


g = pdf_dados.getXmpMetadata()

print('|||||||||||||||| Retorno do método getXmpMetadata() ||||||||||||||||')
print(g)


h = pdf_dados.getFormTextFields

print('|||||||||||||||| Retorno do método getFormTextFields ||||||||||||||||')
print(h)

i = pdf_dados.getOutlines()

print('|||||||||||||||| Retorno do método getOutlines() ||||||||||||||||')
print(i)

j = pdf_dados.isEncrypted

print('|||||||||||||||| Retorno do método isEncrypted ||||||||||||||||')
print(j)

print('|||||||||||||||| Retorno de print(txt_pg1) ||||||||||||||||')
print(txt_pg1)

#k = pdf_dados.getContents()

#print('|||||||||||||||| Retorno do método getContents() ||||||||||||||||')
#print(k)
print("Variable Type a getDocumentInfo(): ", type(a))
print("Variable Type b getPageLayout(): ", type(b))
print("Variable Type c getPageMode(): ", type(c))
print("Variable Type d getNamedDestinations(): ", type(d))
print("Variable Type e getOutlines(): ", type(e))
print("Variable Type f getFields(): ", type(f))
print("Variable Type g getXmpMetadata(): ", type(g))
print("Variable Type h getFormTextFields: ", type(h))
print("Variable Type i getOutlines(): ", type(i))
print("Variable Type j isEncrypted: ", type(j))
print("Variable Type pdf_dados: ", type(pdf_dados))
print("Variable Type pagina1: ", type(pagina1))
print("Variable Type txt_pg1: ", type(txt_pg1))





