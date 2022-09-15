from itertools import count
from posixpath import split


f = open('arquivos/salarios.csv','r')
data = f.read()
rows = data.split('\n')#quebra a linha no enter
full_data =[]
for row in rows:
    split_row = row.split(',')#estou aplicando em cada linha no carater virgula
    full_data.append(split_row)
#contado de linhas     
count = 0 
for row in full_data: #percore as linhas e granva na lista fulldata
    count += 1 #incrementa +1 a cada linha
 
#contado de colunas     
for row in rows:#percore as linhas 
    split_row = row.split(",") #valida os separadores das linhas 
    full_data.append(split_row)# adiciona na lista full data a cada linha 
    first_row = full_data[0]#inicia do ponto 0 ou seja primeira linha
countc = 0
for colun in first_row: #percore as colunas do obejto 0 
    countc = countc +1 # incrementa +1 a cada coluna
    
print(full_data)
print(f'total de linhas {count}')
print(f'total de colunas {countc}')

