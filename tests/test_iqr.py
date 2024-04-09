from robustbase.stats.iqr import iqr

def test_iqr():
    x1 = [x for x in range(1, 201)]
    outlier = [x for x in range(501, 516)]
    x2 = x1 + outlier

    assert iqr(x2) == (161.5, 54.5)

if __name__ == "__main__":
    test_iqr()
    print("IQR test passed!!!")
