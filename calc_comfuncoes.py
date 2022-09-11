print("\n******************* Python Calculator *******************")

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

print("\nSelecione a operação desejada: \n")
print(" + Soma")
print(" - Subtração")
print(" * Multiplicação")
print(" / Divisão")

escolha = input("\nDigite sua opção (+ - * / ): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == '+':
	print("\n")
	print(num1, "+", num2, "=", add(num1, num2))
	print("\n")

elif escolha == '-':
	print("\n")
	print(num1, "-", num2, "=", subtract(num1, num2))
	print("\n")

elif escolha == '*':
	print("\n")
	print(num1, "*", num2, "=", multiply(num1, num2))
	print("\n")

elif escolha == '/':
	print("\n")
	print(num1, "/", num2, "=", divide(num1, num2))
	print("\n")

else:
	print("\nOpção Inválida!")