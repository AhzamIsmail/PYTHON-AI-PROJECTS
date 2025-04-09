# import streamlit as st # type: ignore

# #functionality

# def distance_convertor(value, from_unit, to_unit):
#     units = {
#        "m": 1,
#        "cm": 100,
#        "mm": 1000,
#        "km": 0.001,
#        }
#     result = value * units[from_unit] / units[to_unit]
#     return result
        

# def temperature_convertor(value, from_unit, to_unit):
#     if from_unit == "Celsius" and to_unit == "Fahrenheit":
#         return value * 9/5 + 32
    
#     elif from_unit == "Fahrenheit" and to_unit == "Celsius":
#         return (value - 32) * 5/9
#     else:
#         return value
    
# def volume_convertor(value, from_unit, to_unit):
#     units = {
#         "Litre": 1,
#         "ml": 1000,
#         "cm3": 1000,
#         "m3": 0.001,
#     }
#     result = value * units[from_unit] / units[to_unit]
#     return result 

# def weight_convertor(value, from_unit, to_unit):
#     units = {
#         "kilogram": 1,
#         "gram": 1000,
#         "pound": 2.20462,
#         "ounce": 35.274,
#     }
#     result = value * units[from_unit] / units[to_unit]
#     return result  
        


# #UI

# st.title("Unit Coverter")

# #select category
# category = st.selectbox("Select Category", ["Length", "Temperature", "Volume", "Weight"])

# if category == "Length":
#     from_unit = st.selectbox("From", ["m", "cm", "mm", "km"])
#     to_unit = st.selectbox("To", ["m", "cm", "mm", "km"])
#     value = st.number_input("Enter Value")

#     if st.button("Convert" , key = "length_convertor"):
#         result = distance_convertor(value, from_unit, to_unit)
#         st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")


# elif category == "Temperature":
#     from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
#     to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
#     value = st.number_input("Enter Value")

#     if st.button("Convert" , key = "temp_convertor"):
#         result = temperature_convertor(value, from_unit, to_unit)
#         st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

    
    
#     elif category == "Volume":
#      from_unit = st.selectbox("From", ["Litre", "ml", "cm3", "m3"])
#      to_unit = st.selectbox("To", ["Litre", "ml", "cm3", "m3"])
#      value = st.number_input("Enter Value")

#     if st.button("Convert" , key = "volume_convertor"):
#         result = volume_convertor(value, from_unit, to_unit)
#         st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

# elif category == "Weight":
#     from_unit = st.selectbox("From", ["kilogram", "gram", "pound", "ounce"])
#     to_unit = st.selectbox("To", ["kilogram", "gram", "pound", "ounce"])
#     value = st.number_input("Enter Value")

# if st.button("Convert" , key = "weight_convertor"):
#         result = weight_convertor(value, from_unit, to_unit)
#         st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")
    

import streamlit as st

# Functionality

def distance_convertor(value, from_unit, to_unit):
    units = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return value * 9/5 + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    else:
        return value

def volume_convertor(value, from_unit, to_unit):
    units = {
        "Litre": 1,
        "ml": 1000,
        "cm3": 1000,
        "m3": 0.001,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def weight_convertor(value, from_unit, to_unit):
    units = {
        "kilogram": 1,
        "gram": 1000,
        "pound": 2.20462,
        "ounce": 35.274,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# UI

st.title("Unit Converter")

# Select category
category = st.selectbox("Select Category", ["Length", "Temperature", "Volume", "Weight"])

if category == "Length":
    from_unit = st.selectbox("From", ["m", "cm", "mm", "km"])
    to_unit = st.selectbox("To", ["m", "cm", "mm", "km"])
    value = st.number_input("Enter Value")

    if st.button("Convert", key="length_convert"):
        result = distance_convertor(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value")

    if st.button("Convert", key="temp_convert"):
        result = temperature_convertor(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Volume":
    from_unit = st.selectbox("From", ["Litre", "ml", "cm3", "m3"])
    to_unit = st.selectbox("To", ["Litre", "ml", "cm3", "m3"])
    value = st.number_input("Enter Value")

    if st.button("Convert", key="volume_convert"):
        result = volume_convertor(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["kilogram", "gram", "pound", "ounce"])
    to_unit = st.selectbox("To", ["kilogram", "gram", "pound", "ounce"])
    value = st.number_input("Enter Value")

    if st.button("Convert", key="weight_convert"):
        result = weight_convertor(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")