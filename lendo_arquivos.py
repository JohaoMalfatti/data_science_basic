arq1 = open('arquivos/arq1.txt','r') #abre o arquivo
print (arq1.read()) #le o arquivo 
print (arq1.tell()) #conta os caracteres 
print (arq1.seek(0.0))#abre em um detrimando ponto do arquivo
print (arq1.read(10))#le x numeros de caracteres

arq2 = open('arquivos/arq2.txt', 'w')
arq2.write('Testanto a gravação de arquivos')
arq2.close()

arq2 = open('arquivos/arq2.txt', 'r')
print (arq2.read()) #le o arquivo de txt


