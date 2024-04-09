from robustbase.stats.mad import mad

def test_mad():
    x1 = [x for x in range(1, 201)]
    outlier = [x for x in range(501, 516)]
    x2 = x1 + outlier

    assert mad(x2, center=None, constant=1.4826, na=False, low=False, high=False) == 80.0604
    assert mad(x2, center=1.5, constant=1.4826, na=False, low=False, high=False) == 157.8969
    assert mad(x2, center=None, constant=1.4826, na=False, low=True, high=False) == 80.0604
    assert mad(x2, center=None, constant=1.4826, na=False, low=False, high=True) == 80.0604

if __name__ == "__main__":
    test_mad()
    print("MAD tests passed!!!")
