import  pandas as pd

file_name = 'arquivos/binary.csv'
df = pd.read_csv(file_name)
df.head()

file_name2 = 'arquivos/salarios.csv'
df2 = pd.read_csv