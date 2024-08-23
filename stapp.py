import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# # Load the trained model
 with open('model.pkl', 'rb') as file:
     model = pickle.load(file)

# Load the dataset -- model developement --
data = pd.read_csv('cleandata.csv')
y=data["price"]
X=data.drop(["price","ID"],axis=1)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
trans=ColumnTransformer([("trf1",OneHotEncoder(drop="first"),
                         ['make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style',
       'drive-wheels', 'engine-location', 'engine-type', 'num-of-cylinders',
       'fuel-system'])],
                        remainder="passthrough")
# encoding
X_train=trans.fit_transform(X_train)
X_test=trans.transform(X_test)
model=RandomForestRegressor()
model.fit(X_train,y_train)
model.predict(X_test)
pickle.dump(model,open("my_model.pkl","wb"))
#------- model developement complete
st.title("Used Car Price Prediction")

# Get user input
st.subheader("Enter the car details:")
year = st.number_input("Year", min_value=1990, max_value=2023, value=2020, step=1)
mileage = st.number_input("Mileage (in km)", min_value=0, value=50000, step=1000)
engine = st.number_input("Engine (in cc)", min_value=800, max_value=6000, value=1500, step=100)
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Previous Owners", ["First", "Second", "Third", "Fourth & Above"])
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

# Create a new data point from user input
new_data = pd.DataFrame({
    'Year': [year],
    'Mileage': [mileage],
    'Engine': [engine],
    'Transmission': [transmission],
    'Owner': [owner],
    'Fuel_Type': [fuel]
})

# Make prediction
if st.button("Predict Price"):
    prediction = model.predict(new_data)[0]
    st.write(f"The predicted price of the car is: ₹{prediction:.2f}")
