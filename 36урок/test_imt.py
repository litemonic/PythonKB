from imt_calculator.imt_calc import calculate_imt, isTrue

def test_imt_calculator():
    assert calculate_imt(70, 1.75) == 22.8571428571
    assert calculate_imt(0, 1.75) == 0.0

def test_isTrue():
    assert isTrue(24.9) is False
    assert isTrue(25.0) is True
    assert isTrue(30.0) is True
    assert isTrue(24.0) is False
    assert isTrue(5.6) is False