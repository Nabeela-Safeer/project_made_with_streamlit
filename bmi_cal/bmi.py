import streamlit as st

st.title('BMI Calculator')

# Weight

status = st.radio('select your weight status :', ('kg', 'pounds'))
if (status == 'kg'):
    weight = st.number_input('Enter your weight (in kg)')
elif (status == 'pounds'):
    weight = st.number_input('Enter your weight (in pounds)')
    try:
        weight = weight / 2.20462
    except:
        st.text("Enter some value of weight")
else:
    weight = None


# Height

status = st.radio('Select your height status:', ('cms', 'meters', 'feet'))

if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
 
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
elif(status == 'meter'):
    # take height input in meters
    height = st.number_input('meter')
 
    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")
else:
    # take height input in feet
    height = st.number_input('Feet')
 
    # 1 meter = 3.28084
    try:
        bmi = weight / (((height/3.28084))**2)
    except:
        st.text("Enter some value of height")

if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
 
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")





