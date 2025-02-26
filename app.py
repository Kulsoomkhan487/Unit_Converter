from flet import *

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
        'Us fluid ounce': 2.95735e-5,
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
        'Centimeter /SecondSquare': 0.01,
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
        'Milivolt': 1e-3,
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

def convert_quantity(quantity, value, from_unit, to_unit):
    if quantity == 'Temperature':  # Fixed case sensitivity
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return round(value * 9 / 5 + 32, 3)
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return round((value - 32) * 5 / 9, 3)  # Fixed incorrect parenthesis
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return round(value + 273.15, 3)
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return round(value - 273.15, 3)  # Fixed incorrect parenthesis
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            return round((value * 9 / 5) - 459.67, 3)
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            return round((value + 459.67) * 5 / 9, 3)
    else:
        return value * units[quantity][from_unit] / units[quantity][to_unit]


def submit(e):
   ...
def swap_units(e): # function to swap input and output units
   ...

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_width = 500
    page.window_height = 610
    page.window_min_width = 500
    page.window_min_height = 610
    page.padding = 20
    page.bgcolor = 'green50'

    # Create a Container with a Stack and Cards
    main = Container(
        content=Stack(
            [
                Card(
                    width=420,
                    height=95,
                    color='green100',
                    margin=Margin(top=11, left=14, right=0, bottom=0),
                ),
                Card(
                    width=420,
                    height=170,
                    color='green100',
                    margin=Margin(top=109, left=14, right=0, bottom=0),
                ),
                Card(
                    width=420,
                    height=175,
                    color='green100',
                    margin=Margin(top=282, left=14, right=0, bottom=0),
                ),
                Container(
                    content=Dropdown(
                        options=[dropdown.Option(u) for u in units.keys()],
                        label='Select Quantity',
                        label_style=TextStyle(color='black'),
                        dense=True,
                        scale=1.2,
                        width=180,
                        focused_border_color='black',
                        value='Length',
                    ),
                    top=34,
                    left=53,
                ),
                FloatingActionButton(
                    content=Text(
                        'convert',
                        size=20,
                    ),
                    top=28.8,
                    left=265,
                    bgcolor='green300',
                    width=150,
                    height=58.5,
                    shape=RoundedRectangleBorder(radius=6),
                    on_click=submit,
                ),

                 Container(
                    content=Dropdown(
                        options=[dropdown.Option(u) for u in units['Length'].keys()],
                        label='Input Unit',
                        label_style=TextStyle(color='black'),
                        dense=True,
                        scale=1.2,
                        width=280,
                        focused_border_color='black',
                        value='Meter',
                    ),
                    top=206,
                    left=63,
                ),

                    Container(
                    content=Dropdown(
                        options=[dropdown.Option(u) for u in units['Length'].keys()],
                        label='Input Unit',
                        label_style=TextStyle(color='black'),
                        dense=True,
                        scale=1.2,
                        width=280,
                        focused_border_color='black',
                        value='Meter',
                    ),
                    top=136,
                    left=63,
                ),
                IconButton(
                    icon=icons.SWAP_VERT,
                    icon_size=35,
                    icon_color='black',
                    top=166,
                    left=373,
                    on_click=swap_units,
                ),
                Container(TextField(
                    label= 'Input Value',
                    label_style=TextStyle(color='black'),
                    width=310,
                    scale=1.2,
                    dense=True,
                    focused_border_color='black',
                    cursor_color='black',
                    text_align='center',
                    on_submit=submit,
                ), top=309 , left=68),

                Container(TextField(
                    label= 'Input Value',
                    value='---',
                    label_style=TextStyle(color='black'),
                    width=310,
                    scale=1.2,
                    dense=True,
                    focused_border_color='black',
                    cursor_color='black',
                    text_align='center',
                    read_only=True,
                    on_submit=submit,
                ), top=382, left=68),
            ]
        ),
        width=450,
        height=472,
        bgcolor='green50',
        border_radius=15,
        shadow=BoxShadow(spread_radius=2, blur_radius=9, color='bluegrey300'),
    )

    # Add the Container to the page
    page.add(main)


# Run the app in a browser
app(target=main, view=WEB_BROWSER)