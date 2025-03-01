import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversion = {
        "meters": {"feet": 3.28084, "kilometers": 0.001, "miles": 0.000621371, "centimeters": 100, "inches": 39.3701},
        "feet": {"meters": 0.3048, "kilometers": 0.0003048, "miles": 0.000189394, "centimeters": 30.48, "inches": 12},
        "kilometers": {"meters": 1000, "feet": 3280.84, "miles": 0.621371, "centimeters": 100000, "inches": 39370.1},
        "miles": {"meters": 1609.34, "feet": 5280, "kilometers": 1.60934, "centimeters": 160934, "inches": 63360},
        "centimeters": {"meters": 0.01, "feet": 0.0328084, "kilometers": 0.00001, "miles": 0.0000062137, "inches": 0.393701},
        "inches": {"meters": 0.0254, "feet": 0.0833333, "kilometers": 0.0000254, "miles": 0.000015783, "centimeters": 2.54},
    }
    return value * conversion[from_unit][to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion = {
        "kilograms": {"pounds": 2.20462, "grams": 1000, "ounces": 35.274},
        "pounds": {"kilograms": 0.453592, "grams": 453.592, "ounces": 16},
        "grams": {"kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
        "ounces": {"kilograms": 0.0283495, "pounds": 0.0625, "grams": 28.3495},
    }
    return value * conversion[from_unit][to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_area(value, from_unit, to_unit):
    conversion = {
        "square meters": {"square feet": 10.764, "square kilometers": 0.000001, "acres": 0.000247105, "hectares": 0.0001},
        "square feet": {"square meters": 0.092903, "square kilometers": 0.000000092903, "acres": 0.0000229568, "hectares": 0.0000092903},
        "square kilometers": {"square meters": 1000000, "square feet": 10763910.4, "acres": 247.105, "hectares": 100},
        "acres": {"square meters": 4046.86, "square feet": 43560, "square kilometers": 0.00404686, "hectares": 0.404686},
        "hectares": {"square meters": 10000, "square feet": 107639, "square kilometers": 0.01, "acres": 2.47105},
    }
    return value * conversion[from_unit][to_unit]

def convert_frequency(value, from_unit, to_unit):
    conversion = {"Hertz": {"kilohertz": 0.001, "megahertz": 0.000001, "gigahertz": 0.000000001},
                  "kilohertz": {"Hertz": 1000, "megahertz": 0.001, "gigahertz": 0.000001},
                  "megahertz": {"Hertz": 1000000, "kilohertz": 1000, "gigahertz": 0.001},
                  "gigahertz": {"Hertz": 1000000000, "kilohertz": 1000000, "megahertz": 1000}}
    return value * conversion[from_unit][to_unit]

def convert_volume(value, from_unit, to_unit):
    conversion = {"liters": {"milliliters": 1000, "gallons": 0.264172, "cubic meters": 0.001},
                  "milliliters": {"liters": 0.001, "gallons": 0.000264172, "cubic meters": 0.000001},
                  "gallons": {"liters": 3.78541, "milliliters": 3785.41, "cubic meters": 0.00378541},
                  "cubic meters": {"liters": 1000, "milliliters": 1000000, "gallons": 264.172}}
    return value * conversion[from_unit][to_unit]

def convert_time(value, from_unit, to_unit):
    conversion = {"seconds": {"minutes": 1/60, "hours": 1/3600, "days": 1/86400},
                  "minutes": {"seconds": 60, "hours": 1/60, "days": 1/1440},
                  "hours": {"seconds": 3600, "minutes": 60, "days": 1/24},
                  "days": {"seconds": 86400, "minutes": 1440, "hours": 24}}
    return value * conversion[from_unit][to_unit]

# Streamlit App
st.set_page_config(page_title="Unit Converter", page_icon="🔄")
st.title("🔄 Advanced Unit Converter App")

conversion_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature", "Area", "Frequency", "Volume", "Time"])

unit_mappings = {
    "Length": ["meters", "feet", "kilometers", "miles", "centimeters", "inches"],
    "Weight": ["kilograms", "pounds", "grams", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["square meters", "square feet", "square kilometers", "acres", "hectares"],
    "Frequency": ["Hertz", "kilohertz", "megahertz", "gigahertz"],
    "Volume": ["liters", "milliliters", "gallons", "cubic meters"],
    "Time": ["seconds", "minutes", "hours", "days"]
}

value = st.number_input("Enter value:")
from_unit = st.selectbox("From:", unit_mappings[conversion_type])
to_unit = st.selectbox("To:", [u for u in unit_mappings[conversion_type] if u != from_unit])

if st.button("Convert"):
    conversion_function = globals()[f"convert_{conversion_type.lower()}"]
    result = conversion_function(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

st.write("💡 Created with ❤️ using Streamlit")
