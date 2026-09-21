import pytest

from src.interpolation import linear_interpolate


def test_midpoint_interpolation():
    result = linear_interpolate(
        x=25,
        x1=20,
        y1=100,
        x2=30,
        y2=140,
    )

    assert result == pytest.approx(120)


def test_valve_interpolation_example():
    result = linear_interpolate(
        x=65,
        x1=50,
        y1=1.270,
        x2=70,
        y2=1.390,
    )

    assert result == pytest.approx(1.360)
