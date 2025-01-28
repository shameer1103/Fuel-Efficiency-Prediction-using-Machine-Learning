'''Streamlit Interface Code'''

# Importing necessary packages

import pickle
import streamlit as st

# Loading the Pickle file

with open("C:/Users/Shameer/Documents/Luminar files/ML Project/fuel_2.csv/fuel.pkl","rb") as file:
    fuel = pickle.load(file)

# Page title

st.set_page_config(
    page_title="Fuel Efficiency Prediction",
    page_icon="🚗"
)

st.title('Fuel Efficiency Predcition Model')
st.write('Algorithm model used: RandomForestRegressor')

# Defining Column Layout

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Encoded values of Object columns mapped into a dictionary

class_options = ['Minicompact Cars',
 'Two Seaters',
 'Special Purpose Vehicle 2WD',
 'Special Purpose Vehicle 4WD',
 'Subcompact Cars',
 'Midsize Cars',
 'Midsize Station Wagons',
 'Compact Cars',
 'Midsize-Large Station Wagons',
 'Large Cars',
 'Small Station Wagons',
 'Standard Pickup Trucks 2WD',
 'Vans, Passenger Type',
 'Vans, Cargo Type',
 'Standard Pickup Trucks 4WD',
 'Special Purpose Vehicles',
 'Small Pickup Trucks 2WD',
 'Small Pickup Trucks 4WD',
 'Vans',
 'Standard Pickup Trucks',
 'Small Pickup Trucks',
 'Vans Passenger',
 'Standard Pickup Trucks/2wd',
 'Special Purpose Vehicles/2wd',
 'Special Purpose Vehicles/4wd',
 'Sport Utility Vehicle - 4WD',
 'Sport Utility Vehicle - 2WD',
 'Minivan - 2WD',
 'Minivan - 4WD',
 'Special Purpose Vehicle']

class_labels = {'Minicompact Cars': 5,
 'Two Seaters': 25,
 'Special Purpose Vehicle 2WD': 13,
 'Special Purpose Vehicle 4WD': 14,
 'Subcompact Cars': 24,
 'Midsize Cars': 2,
 'Midsize Station Wagons': 3,
 'Compact Cars': 0,
 'Midsize-Large Station Wagons': 4,
 'Large Cars': 1,
 'Small Station Wagons': 11,
 'Standard Pickup Trucks 2WD': 21,
 'Vans, Passenger Type': 29,
 'Vans, Cargo Type': 28,
 'Standard Pickup Trucks 4WD': 22,
 'Special Purpose Vehicles': 15,
 'Small Pickup Trucks 2WD': 9,
 'Small Pickup Trucks 4WD': 10,
 'Vans': 26,
 'Standard Pickup Trucks': 20,
 'Small Pickup Trucks': 8,
 'Vans Passenger': 27,
 'Standard Pickup Trucks/2wd': 23,
 'Special Purpose Vehicles/2wd': 16,
 'Special Purpose Vehicles/4wd': 17,
 'Sport Utility Vehicle - 4WD': 19,
 'Sport Utility Vehicle - 2WD': 18,
 'Minivan - 2WD': 6,
 'Minivan - 4WD': 7,
 'Special Purpose Vehicle': 12}

drive_options = ['Front-Wheel Drive',
 '2-Wheel Drive',
 '4-Wheel or All-Wheel Drive',
 'Rear-Wheel Drive',
 '4-Wheel Drive',
 'All-Wheel Drive',
 'Part-time 4-Wheel Drive']

transmission_options = ['Manual 5-Speed',
 'Automatic 3-Speed',
 'Manual 4-Speed',
 'Automatic 4-Speed',
 'Manual 3-Speed',
 'Manual 4-Speed Doubled',
 'Automatic (S4)',
 'Manual 5 Speed',
 'Manual 6-Speed',
 'Automatic 5-Speed',
 'Automatic (variable gear ratios)',
 'Automatic (S5)',
 'Auto(L4)',
 'Auto(L3)',
 'Automatic 6-Speed',
 'Automatic (S6)',
 'Automatic 7-Speed',
 'Automatic (S7)',
 'Automatic (S8)',
 'Automatic (AV)',
 'Auto(AM7)',
 'Auto(AM6)',
 'Automatic (AM6)',
 'Automatic (A6)',
 'Auto (AV-S6)',
 'Auto (AV-S8)',
 'Automatic (AV-S6)',
 'Auto(AV-S6)',
 'Auto(AV-S8)',
 'Automatic 8-Speed',
 'Auto(AM-S6)',
 'Auto(AM-S7)',
 'Manual 7-Speed']

transmission_labels = {'Manual 5-Speed': 30,
 'Automatic 3-Speed': 20,
 'Manual 4-Speed': 27,
 'Automatic 4-Speed': 21,
 'Manual 3-Speed': 26,
 'Manual 4-Speed Doubled': 28,
 'Automatic (S4)': 14,
 'Manual 5 Speed': 29,
 'Manual 6-Speed': 31,
 'Automatic 5-Speed': 22,
 'Automatic (variable gear ratios)': 19,
 'Automatic (S5)': 15,
 'Auto(L4)': 9,
 'Auto(L3)': 8,
 'Automatic 6-Speed': 23,
 'Automatic (S6)': 16,
 'Automatic 7-Speed': 24,
 'Automatic (S7)': 17,
 'Automatic (S8)': 18,
 'Automatic (AV)': 12,
 'Auto(AM7)': 5,
 'Auto(AM6)': 4,
 'Automatic (AM6)': 11,
 'Automatic (A6)': 10,
 'Auto (AV-S6)': 0,
 'Auto (AV-S8)': 1,
 'Automatic (AV-S6)': 13,
 'Auto(AV-S6)': 6,
 'Auto(AV-S8)': 7,
 'Automatic 8-Speed': 25,
 'Auto(AM-S6)': 2,
 'Auto(AM-S7)': 3,
 'Manual 7-Speed': 32}

# Creating Boxes and Sliders for Input Features

class_type = col1.selectbox("Select the class of the vehicle: ", class_options)

fuel_option = ['Regular Gasoline', 'Diesel', 'Premium Gasoline', 'Midgrade Gasoline']

fuel_type = col2.selectbox("Select the Fuel type: ", fuel_option)

drive_type = col3.selectbox('Select drive type: ', drive_options)

transmission_type = col4.selectbox('Select transmission type: ', transmission_options)

engine_cylinder = st.slider("Engine Cylinders: ", min_value=2, max_value=8, value=5, step=1)

engine_displacement = st.slider("Engine displacement: ", min_value=1.0, max_value=7.0, value=4.0, step=0.1)

pred_ans = [class_labels[class_type], transmission_labels[transmission_type], engine_cylinder, engine_displacement, 0, 0, 0, 0, 0, 0, 0, 0, 0]

if drive_type == '4-Wheel Drive':
    pred_ans[4] = 1
elif drive_type == '4-Wheel or All-Wheel Drive':
    pred_ans[5] = 1
elif drive_type == 'All-Wheel Drive':
    pred_ans[6] = 1
elif drive_type == 'Front-Wheel Drive':
    pred_ans[7] = 1
elif drive_type == 'Part-time 4-Wheel Drive':
    pred_ans[8] = 1
elif drive_type == 'Rear-Wheel Drive':
    pred_ans[9] = 1
else:
    pass

if fuel_type == 'Midgrade Gasoline':
    pred_ans[10] = 1
elif fuel_type == 'Premium Gasoline':
    pred_ans[11] = 1
elif fuel_type == 'Regular Gasoline':
    pred_ans[12] = 1
else:
    pass

# Code to execute if "Predict" button is clicked

if st.button("Predict Fuel Efficieny"):
    answer = fuel.predict([pred_ans])
    st.write('Miles Per Gallon: ',answer[0])

    print(pred_ans)
    print(answer)