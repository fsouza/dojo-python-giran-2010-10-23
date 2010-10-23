from nose.tools import *
from palavra_prima import *

def test_1_num_eh_primo():
	assert_false(is_primo(1))
	
def test_17_eh_primo():
	assert_true(is_primo(17))
	
def test_4_num_eh_primo():
	assert_false(is_primo(4))
	
def test_523_eh_primo():
	assert_true(is_primo(523))
	
def test_13_eh_primo():
	assert_true(is_primo(13))

def test_UFRN_eh_palavra_prima():
	assert_true(is_palavra_prima("UFRN"))

def test_contest_num_eh_palavra_prima():
	assert_false(is_palavra_prima("contest"))
	
	
def test_AcM_num_eh_palavra_prima():
	assert_false(is_palavra_prima("AcM"))
	
def test_baiano_num_eh_palavra_prima():
	assert_false(is_palavra_prima("baiano"))

def test_makoto_num_eh_palavra_prima():
	assert_false(is_palavra_prima("makoto"))
	
def test_XXXXXXXXXXw_eh_palavra_prima():
	assert_true(is_palavra_prima("XXXXXXXXXXw"))