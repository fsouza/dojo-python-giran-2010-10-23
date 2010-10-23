import string

def is_primo(numero):
	divisoes = 0
	for divisor in range(2, numero + 1):
		if numero % divisor == 0:
			divisoes += 1
	return divisoes == 1

def is_palavra_prima(palavra):
	soma = 0
	for letra in palavra:
		soma += string.letters.find(letra) + 1
	
	return is_primo(soma)