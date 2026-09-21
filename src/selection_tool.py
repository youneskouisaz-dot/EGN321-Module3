from src.lookup_tables import LOOKUP_TABLES
from src.interpolation import linear_interpolate


def select_coefficient(valve_family, temperature_c):
    """
    Select a valve coefficient using exact lookup or interpolation.

    Parameters:
        valve_family (str): Valve family name.
        temperature_c (float): Operating temperature in degrees Celsius.

    Returns:
        dict: Structured result describing the selected coefficient.

    Raises:
        ValueError: If the valve family is unsupported or the temperature
        is outside the supported range.
    """

    # Validate valve family
    if valve_family not in LOOKUP_TABLES:
        raise ValueError(
            f"Unsupported valve_family: {valve_family}"
        )

    table = LOOKUP_TABLES[valve_family]

    minimum_temp = table[0][0]
    maximum_temp = table[-1][0]

    # Refuse extrapolation
    if temperature_c < minimum_temp:
        raise ValueError(
            f"temperature_c {temperature_c} is below "
            f"the supported minimum {minimum_temp}"
        )

    if temperature_c > maximum_temp:
        raise ValueError(
            f"temperature_c {temperature_c} exceeds "
            f"the supported maximum {maximum_temp}"
        )

    # Check for exact match
    for temp, coefficient in table:
        if temperature_c == temp:
            return {
                "valve_family": valve_family,
                "temperature_c": temperature_c,
                "coefficient": coefficient,
                "method": "exact",
                "lower_point": None,
                "upper_point": None,
                "supported_range": (minimum_temp, maximum_temp),
            }

    # Find surrounding rows and interpolate
    for i in range(len(table) - 1):
        lower_temp, lower_coefficient = table[i]
        upper_temp, upper_coefficient = table[i + 1]

        if lower_temp < temperature_c < upper_temp:
            coefficient = linear_interpolate(
                x=temperature_c,
                x1=lower_temp,
                y1=lower_coefficient,
                x2=upper_temp,
                y2=upper_coefficient,
            )

            return {
                "valve_family": valve_family,
                "temperature_c": temperature_c,
                "coefficient": coefficient,
                "method": "interpolation",
                "lower_point": (lower_temp, lower_coefficient),
                "upper_point": (upper_temp, upper_coefficient),
                "supported_range": (minimum_temp, maximum_temp),
            }
