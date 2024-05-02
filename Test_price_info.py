import price_info as prinf

def test_total_cost_shopping():
    result = 0
    expected = 46.75
    result = prinf.total_cost_shopping()
    assert (result == expected)

def test_cost_of_fruit():
    result = 0
    inputf = "pear"
    inputq = 12
    expected = 10.8
    result = prinf.cost_of_fruits(inputf, inputq)
    assert (result == expected)