import PyPDF2
from PyPDF2 import pdf
from tabulate import tabulate


#Abrindo arquivo em modo leitura e lendo o binario
pdf_file = open('nbr15280.pdf','rb')
#Após pegar binário, pegamos os dados de PDF desse binário
pdf_dados = PyPDF2.PdfFileReader(pdf_file)

print('|||||||||||||||| Retorno de pdf_dados')
print("path is: ", pdf_dados)

print('Números de páginas é igual a:' + str(pdf_dados.numPages))
#Sertando a variavel pagina1 com o objeto pagina1
pagina1 = pdf_dados.getPage(15)
#pegando texto extraido da pagina 1
txt_pg1 = pagina1.extractText()
print('|||||||||||||||| Retorno de print(pagina1)')
print(pagina1)
print('|||||||||||||||| Retorno de print(txt_pg1)')
print(txt_pg1)

a = pdf_dados.getDocumentInfo()

print('|||||||||||||||| Retorno do método getDocumentInfo()')
print(a)


b = pdf_dados.getPageLayout()

print('|||||||||||||||| Retorno do método getPageLayout()')
print(b)


c = pdf_dados.getPageMode()

print('|||||||||||||||| Retorno do método getPageMode()')
print(c)

d = pdf_dados.getNamedDestinations()
print('|||||||||||||||| Retorno do método getNamedDestinations()')
print(d)


e = pdf_dados.getOutlines()

print('|||||||||||||||| Retorno do método getOutlines()')
print(e)

f = pdf_dados.getFields(txt_pg1)

print('|||||||||||||||| Retorno do método getFields()')
print(f)

g = pdf_dados.getXmpMetadata()

print('|||||||||||||||| Retorno do método getXmpMetadata()')
print(g)

h = pdf_dados.getFormTextFields

print('|||||||||||||||| Retorno do método getFormTextFields()')
print(h)

i = pdf_dados.getOutlines()

print('|||||||||||||||| Retorno do método getOutlines()')
print(i)







