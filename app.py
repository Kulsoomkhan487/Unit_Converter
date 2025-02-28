import streamlit as st

# Define the units dictionary (same as before)
units = {
    # Length Conversion Units
    'Length': {
        'Meter': 1,
        'Kilometer': 1000,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Micrometer': 0.000001,
        'Nanometer': 0.000000001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254,
        'NauticalMile': 1852,
        'AstronomicalUnit': 1.49597870700,
        'LightYear': 9.460730472580800,
        'Parsec': 30856775814671900,
    },

    # Area Conversion Units
    'Area': {
        'Square Meter': 1,
        'Square Kilometer': 1000000,
        'Square Centimeter': 0.0001,
        'Square Millimeter': 0.000001,
        'Square Micrometer': 0.000000000001,
        'Square Inch': 0.00064516,
        'Square Foot': 0.09290304,
        'Square Yard': 0.83612736,
        'Hectare': 10000,
        'Acre': 4046.8564224,
    },

    # Volume Conversion Units
    'Volume': {
        'Cubic Meter': 1,
        'Cubic Kilometer': 1000000000,
        'Cubic Centimeter': 0.000001,
        'Cubic Millimeter': 0.000000001,
        'Litre': 0.001,
        'Millilitre': 1e-6,
        'Cubic Inch': 0.0000163871,
        'Cubic Foot': 0.0283168466,
        'US Gallon': 0.00378541,
        'US Quart': 0.000946353,
        'US Pint': 0.000473176,
        'US Fluid Ounce': 2.95735e-5,
    },

    # Mass Conversion Units
    'Mass': {
        'Kilogram': 1,
        'Gram': 0.001,
        'Milligram': 1e-6,
        'Microgram': 1e-9,
        'MetricTon': 1000,
        'Tonne': 1000,
        'Pound': 0.453592,
        'Ounce': 0.0283495,
        'Carat': 0.0002,
        'Stone': 6.35029,
    },

    # Time Conversion Units
    'Time': {
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Month': 2628000,
        'Year': 31536000,
    },

    # Speed Conversion Units
    'Speed': {
        'Meter/Second': 1,
        'Kilometer/Hour': 0.277778,
        'Mile/Hour': 0.44704,
        'Foot/Second': 0.3048,
        'Knot': 0.514444,
    },

    # Acceleration Conversion Units
    'Acceleration': {
        'Meter/SecondSquare': 1,
        'Kilometer/HourSquare': 0.0000771605,
        'Centimeter/SecondSquare': 0.01,
        'Foot/SecondSquare': 0.3048,
        'Gravity': 9.80665,
    },

    # Pressure Conversion Units
    'Pressure': {
        'Pascal': 1,
        'Kilopascal': 1000,
        'Megapascal': 1000000,
        'Bar': 100000,
        'Millibar': 100,
        'MillimeterOfMercury': 133.322,
        'Atmosphere': 101325,
        'Torr': 133.322,
        'Psi': 6894.76,
    },

    # Temperature Conversion Units
    'Temperature': {
        'Celsius': [1, 0],
        'Fahrenheit': [1.8, 32],
        'Kelvin': [1, 273.15],
    },

    # Energy Conversion Units
    'Energy': {
        'Joule': 1,
        'Kilojoule': 1000,
        'Megajoule': 1000000,
        'Calorie': 4.184,
        'GramCalorie': 4.184,
        'Kilocalorie': 4184,
        'Electronvolt': 1.602176634e-19,
        'WattHour': 3600,
        'KilowattHour': 3600000,
    },

    # Power Conversion Units
    'Power': {
        'Watt': 1,
        'Kilowatt': 1000,
        'Megawatt': 1000000,
        'Gigawatt': 1000000000,
        'Horsepower': 745.7,
    },

    # Voltage Conversion Units
    'Voltage': {
        'Volt': 1,
        'Kilovolt': 1000,
        'Millivolt': 1e-3,
    },

    # Data Conversion Units
    'Data': {
        'Bit': 1,
        'Byte': 8,
        'Kilobit': 1024,
        'Kilobyte': 8192,
        'Megabit': 1e6,
        'Megabyte': 8e6,
        'Gigabit': 1e9,
        'Gigabyte': 8e9,
        'Terabit': 1e12,
        'Terabyte': 8e12,
        'Petabit': 1e15,
        'Petabyte': 8e15,
        'Exabit': 1e18,
        'Exabyte': 8e18,
    },
}

# Function to perform unit conversion (same as before)
def convert_quantity(quantity, value, from_unit, to_unit):
    if quantity == 'Temperature':
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return round(value * 9 / 5 + 32, 3)
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return round((value - 32) * 5 / 9, 3)
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return round(value + 273.15, 3)
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return round(value - 273.15, 3)
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            return round((value * 9 / 5) - 459.67, 3)
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            return round((value + 459.67) * 5 / 9, 3)
    else:
        return round(value * units[quantity][from_unit] / units[quantity][to_unit], 6)

# Streamlit App
def main():
    st.title("Unit Converter")
    st.write("Convert between different units of measurement.")

    # Dropdown to select quantity
    quantity = st.selectbox("Select Quantity", list(units.keys()))

    # Dropdowns to select input and output units
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", list(units[quantity].keys()))
    with col2:
        to_unit = st.selectbox("To Unit", list(units[quantity].keys()))

    # Input field for value
    input_value = st.number_input("Enter Value", value=1.0)

    # Button to perform conversion
    if st.button("Convert"):
        output_value = convert_quantity(quantity, input_value, from_unit, to_unit)
        st.success(f"Converted Value: {output_value}")

    # Button to swap units
    if st.button("Swap Units"):
        from_unit, to_unit = to_unit, from_unit
        st.experimental_rerun()

# Run the Streamlit app
if __name__ == "__main__":
    main()