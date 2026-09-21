import pytest

from src.selection_tool import select_coefficient


def test_exact_lookup_vx100():
    result = select_coefficient("VX-100", 60)

    assert result["coefficient"] == pytest.approx(0.990)
    assert result["method"] == "exact"


def test_exact_lookup_vx300():
    result = select_coefficient("VX-300", 100)

    assert result["coefficient"] == pytest.approx(1.900)
    assert result["method"] == "exact"


def test_interpolation_vx200():
    result = select_coefficient("VX-200", 65)

    assert result["coefficient"] == pytest.approx(1.360)
    assert result["method"] == "interpolation"
    assert result["lower_point"] == (50, 1.270)
    assert result["upper_point"] == (70, 1.390)


def test_interpolation_vx100():
    result = select_coefficient("VX-100", 50)

    assert result["coefficient"] == pytest.approx(0.960)
    assert result["method"] == "interpolation"


def test_lower_boundary():
    result = select_coefficient("VX-200", 10)

    assert result["coefficient"] == pytest.approx(1.100)
    assert result["method"] == "exact"


def test_upper_boundary():
    result = select_coefficient("VX-200", 90)

    assert result["coefficient"] == pytest.approx(1.540)
    assert result["method"] == "exact"


def test_below_range_refused():
    with pytest.raises(ValueError, match="supported minimum"):
        select_coefficient("VX-200", 5)


def test_above_range_refused():
    with pytest.raises(ValueError, match="supported maximum"):
        select_coefficient("VX-200", 95)


def test_unknown_family_refused():
    with pytest.raises(ValueError, match="Unsupported valve_family"):
        select_coefficient("VX-999", 50)
