from robustbase import Qn, Sn, mad, iqr



def test_Qn():

	x = [i for i in range(1,101)]
	assert Qn(x) == 29.960649
	assert Qn(x, finite_corr=False) == 31.06796

	x = [i for i in range(1,10)]
	assert Qn(x) == 3.876571
	assert Qn(x, finite_corr=False) == 4.43828

def test_mad():
	pass

def test_Sn():
	x = [i for i in range(1,251)]
	assert Sn(x, finite_corr=False) == 75.1338

def test_iqr():
	pass