# EGN321 Module 3 - Valve Selection Tool

## Assignment 3.1

This project replaces difficult-to-read spreadsheet lookup logic with a readable Python valve selection tool.

The program uses two inputs:

- Valve family
- Operating temperature in degrees Celsius

The tool selects the correct engineering table for the requested valve family and returns the appropriate valve coefficient.

## Supported Valve Families

The tool supports the following valve families:

- VX-100
- VX-200
- VX-300

## Supported Temperature Ranges

- VX-100: 20°C to 100°C
- VX-200: 10°C to 90°C
- VX-300: 25°C to 125°C

## Selection Behavior

If the requested temperature exactly matches a value in the engineering table, the exact coefficient is returned.

If the temperature falls between two supported table values, linear interpolation is used to calculate the coefficient.

If the requested temperature is below the minimum or above the maximum supported temperature for the selected valve family, the program raises a ValueError instead of extrapolating.

An unsupported valve family also raises a ValueError.

## Engineering Data Source

The lookup values are based on the Engineering Tables sheet in the provided VALVE_SELECTION_rev3.xlsx workbook.

## Linear Interpolation

The program uses the following formula:

y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)

Where:

- x = requested temperature
- x1 = lower table temperature
- x2 = upper table temperature
- y1 = coefficient at the lower temperature
- y2 = coefficient at the upper temperature

## Testing

Automated tests will verify:

- Exact table lookups
- Linear interpolation
- Minimum temperature boundary
- Maximum temperature boundary
- Below-range refusal
- Above-range refusal
- Unsupported valve family refusal

## Assumptions and Limitations

The program only uses the engineering data supplied for this assignment.

The tool does not extrapolate beyond the documented temperature ranges.

Results between known table values are calculated using linear interpolation.

## AI Disclosure

AI assistance was used to help organize the repository, explain the assignment requirements, review Python code, and assist with testing and documentation. All generated work was reviewed and verified against the course-provided engineering data.
