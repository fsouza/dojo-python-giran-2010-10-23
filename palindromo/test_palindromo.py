from nose.tools import assert_true, assert_false
from palindromo import *

def test_numero_1001_eh_palindromo():
	"Deve retornar true, quando for informado 1001"
	assert_true(is_palindromo(1001))

def test_numero_2222_eh_palindromo():
	"Deve retornar true, quando for informado 2222"
	assert_true(is_palindromo(2222))

def test_numero_123_num_eh_palindromo():
	"Deve retornar false, quando for informado 123"
	assert_false(is_palindromo(123))
	
def test_numero_1_eh_palindromo():
	"Deve retornar true, quando for informado 1"
	assert_true(is_palindromo(1))
	