# Calculadora em Python

# Definindo funções da calculadora
def soma(a,b):
	return a + b

def subtracao(a,b):
	return a - b

def multiplicacao(a,b):
	return a*b

def divisao(a,b):
	return a/b

# Criando layout da calculadora
print("\n")
print('******************* Python Calculator *******************')
print('\n')
print("Selecione a operação desejada:\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("\n")

# Recebendo a opção de escolha do usuário
op = int(input("Digite sua opção (1/2/3/4): "))

# Recebendo os números do usuário 
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número "))

if (op == 1):
	# Chamando a função soma
	print( num1, "+", num2, "=", soma(num1, num2))
elif (op == 2):
	# Chamando a função subtracao
	print( num1, "-", num2, "=", subtracao(num1, num2))
elif (op == 3):
	# Chamando a função multiplicacao
	print( num1, "*", num2, "=", multiplicacao(num1, num2))
elif (op == 4):
	print( num1, "/", num2, "=", divisao(num1, num2))
else:
	print("Opção inválida!")