import streamlit as st
import pickle

# Title
st.title('Health Insurance Premium Prediction')

# Inputs
age = st.number_input('Age:', min_value=0, step=1)
bmi = st.number_input('BMI:')
children = st.number_input('Number of Children:', min_value=0, step=1)
gender = st.radio("Gender:", ["Male", "Female"])
smoker = st.radio("Do you smoke?", ["Yes", "No"])

# Load model
model = pickle.load(open('model.pkl','rb'))

# Predict button
if st.button('Predict'):
    # Encode categorical variables
    gender_enc = 1 if gender == "Female" else 0
    smoker_enc = 0 if smoker.upper() == 'NO' else 1

    # Prepare input and predict
    X_test = [[age, bmi, children, gender_enc, smoker_enc]]
    yp = round(model.predict(X_test)[0], 2)
    st.markdown(
        f"""<div style="padding:8px; background-color:#e0f7fa;
                        border-radius:5px; text-align:center; width:100%;">
                <strong>Your Predicted Premium:</strong> ₹ {yp:,.2f}
            </div>""",
        unsafe_allow_html=True
    )