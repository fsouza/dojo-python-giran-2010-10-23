from nose.tools import *
from telefone import *


def test_mylove_deve_ser_igual_69_5683():
	"""docstring for test_mylove_deve_ser_igual_69_5683"""
	assert_equals(decodifica_sequencia("MY LOVE"), "69 5683")

def test_mylove_nao_deve_ser_igual_a_666SATANREINA():
	"""docstring for test_mylove_nao_deve_ser_igual_a_666SATANREINA"""
	assert_not_equals(decodifica_sequencia("MY LOVE"), "666SATANREINA")
	
def test_makoto_deve_ser_igual_a_625686():
	"""docstring for test_makoto_deve_ser_igual_a_625686"""
	assert_equals(decodifica_sequencia("MAKOTO"),"625686")
	
def test_flavia_deve_ser_igual_a_352842():
	"""docstring for test_flavia_deve_ser_igual_352842"""
	assert_equals(decodifica_sequencia("FLAVIA"), "352842")
	
def test_geveaux_deve_ser_igual_a_4383289():
	"""docstring for test_geveaux_deve_ser_igual_"""
	assert_equals(decodifica_sequencia("GEVEAUX"), "4383289")
	
def test_astrogildo_filho_deve_ser_igual_a_2787644536_34546():
	"""docstring for test_astrogildo_filho"""
	assert_equals(decodifica_sequencia("ASTROGILDO FILHO"), "2787644536 34546")

def test_TOMAR_HIFEN_NO_deve_ser_igual_a_86627_HIFEN_66():
	"""docstring for test_MLN Z 90[ astrogildo_filho"""
	assert_equals(decodifica_sequencia("TOMAR-NO"), "86627-66")