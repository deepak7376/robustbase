from robustbase.robustbase import Sn, Qn, iqr, mad

def test_robustbase():
	x1 = [x for x in range(1, 201)]
	outlier = [x for x in range(501, 516)]
	x2 = x1 + outlier

	# Sn tests
	assert Sn(x2, finite_corr=True) == 73.05440915460065
	assert Sn(x2, finite_corr=False) == 72.7486
	assert Sn(x2, constant=1, finite_corr=True) == 61.25642223260159
	assert Sn(x2, constant=1, finite_corr=False) == 61.0

	# Qn tests
	assert Qn(x2, finite_corr=True) == 68.287735
	assert Qn(x2, finite_corr=False) == 68.79334
	assert Qn(x2, constant=1, finite_corr=True) == 30.772162
	assert Qn(x2, constant=1, finite_corr=False) == 31

	# IQR test
	assert iqr(x2) == (161.5, 54.5)

	# MAD tests
	assert mad(x2, center = None, constant = 1.4826, na = False, low = False, high = False) == 80.0604
	assert mad(x2, center = 1.5, constant = 1.4826, na = False, low = False, high = False) == 157.8969
	assert mad(x2, center = None, constant = 1.4826, na = False, low = True, high = False) == 80.0604
	assert mad(x2, center = None, constant = 1.4826, na = False, low = False, high = True) == 80.0604



if __name__ == "__main__":
	test_robustbase()
	print("All tests passed!!!")




	
