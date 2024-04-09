from robustbase.stats.Sn import Sn

def test_Sn():
    x1 = [x for x in range(1, 201)]
    outlier = [x for x in range(501, 516)]
    x2 = x1 + outlier

    assert Sn(x2, finite_corr=True) == 73.05440915460066  # 73.05440915460065
    assert Sn(x2, finite_corr=False) == 72.74860000000001 # 72.7486
    assert Sn(x2, constant=1, finite_corr=True) == 61.25642223260159
    assert Sn(x2, constant=1, finite_corr=False) == 61.0

if __name__ == "__main__":
    test_Sn()
    print("Sn tests passed!!!")
