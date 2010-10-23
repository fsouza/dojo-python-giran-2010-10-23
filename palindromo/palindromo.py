def is_palindromo(number):
	aux = str(number)
	reverse = aux[::-1]
	return aux == reverse

def encontrar_palindromo():
	maior = 999
	lista_numeros = range(999)
	lista_numeros.reverse()
	lista_palindromos = [x * 999 for x in lista_numeros if is_palindromo(x * 999)]
	return lista_palindromos[0]

print encontrar_palindromo()