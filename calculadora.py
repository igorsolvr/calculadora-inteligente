print ("Bem-vindo(a) à calculadora inteligente EBAC!")

while True:
	print ("Escolha uma operação:\n")
	print ("1 - Soma")
	print ("2 - Subtração")
	print ("3 - Multiplicação")
	print ("4 - Divisão")
	print ("\n5 - SAIR")
	operacao = int(input(""))

	if operacao in (1,2,3,4):
		
		n1 = float(input("Digite o primeiro número: "))
		n2 = float(input("Digite o segungo número: "))
 
	if operacao == 1:
		print ("\nO resultado da soma é: ", n1 + n2)
	elif operacao == 2:
		print ("\nO resultado da subtração é: ", n1 - n2)
	elif operacao == 3:
		print ("\nO resultado da multiplicação é: ", n1 * n2)
	elif operacao == 4:
		print ("\nO resultado da divisão é: ", n1 / n2)
	elif operacao == 5:
		print ("Obrigado por utilizar a nossa calculadora!")
		break
	else:
		print ("Não foi possível realizar a operação, tente novamente.")
