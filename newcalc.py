while True: 
    print()
    sair = input ('Deseja Continuar (S) Sim (N) Não')
    if sair == 'n':
        break 
    print()
    num1 =input('Digite um número')
    num2 = input('Digete outro número')

    operador =input('Digite a operação')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um número')
        continue
    num1 = float(num1)
    num2 = float(num2)

    if operador == '+':
        print (num1 +num2)
    elif operador == '-' :
        print(num1 - num2)
    elif operador == '*':
        print(num1*num2)
    elif operador =='/':
        print(num1/num2)
    else:
        print('Operador invalido')
