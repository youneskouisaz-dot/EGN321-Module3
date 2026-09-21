def linear_interpolate(x, x1, y1, x2, y2):
    """
    Perform linear interpolation between two known points.

    Parameters:
        x (float): Requested temperature.
        x1 (float): Lower known temperature.
        y1 (float): Coefficient at lower temperature.
        x2 (float): Upper known temperature.
        y2 (float): Coefficient at upper temperature.

    Returns:
        float: Interpolated coefficient.
    """

    return y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
