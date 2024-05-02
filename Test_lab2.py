import lab2 as lab2

def test_find_min_max():
    result = []
    inputtemps = [5, 27, 29, 35, 60]
    expected = [5, 60]
    result = lab2.calc_min_max_temperature(inputtemps)
    assert (result == expected)

def test_calc_average():
    result = []
    inputtemps = [1, 2, 3, 4, 20]
    expected = 6
    result = lab2.calc_average_temperature(inputtemps)
    assert (result == expected)

def test_calc_median_temperature():
    result = []
    inputtemps = [11, 12, 34, 50, 88, 90, 98]
    expected = 50
    result = lab2.calc_median_temperature(inputtemps)
    assert (result == expected)