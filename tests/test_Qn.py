from robustbase.stats.Qn import Qn

def test_Qn():
    x1 = [x for x in range(1, 201)]
    outlier = [x for x in range(501, 516)]
    x2 = x1 + outlier

    assert Qn(x2, finite_corr=True) == 68.28773488650255
    assert Qn(x2, finite_corr=False) == 68.79334
    assert Qn(x2, constant=1, finite_corr=True) == 30.772161687186276
    assert Qn(x2, constant=1, finite_corr=False) == 31

if __name__ == "__main__":
    test_Qn()
    print("Qn tests passed!!!")
