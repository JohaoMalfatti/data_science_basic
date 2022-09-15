from fileinput import filename


filename = input('Digite o nome do arquivo:')
file = open(f'arquivos/{filename}.txt','w+') #faz a criação do arquivo txt
