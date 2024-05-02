import bmi as bmi

def test_bmi_normal_weight():
    result = False
    inputbmi = 20
    expected = 0
    result = bmi.bmi_range(inputbmi)
    assert (result == expected)


def test_bmi_over_weight():
    result = False
    inputbmi = 26
    expected = 1
    result = bmi.bmi_range(inputbmi)
    assert (result == expected)

def test_bmi_under_weight():
    result = False
    inputbmi = 18
    expected = -1
    result = bmi.bmi_range(inputbmi)
    assert (result == expected)