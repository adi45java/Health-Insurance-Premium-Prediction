import streamlit as st
import pickle

st.set_page_config(page_title="💡 Health Insurance Premium Prediction", page_icon="💡", layout="centered")

st.markdown("<h2 style='text-align:center; color:#2E86C1;'>💡 Health Insurance Premium Prediction</h2>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input('🧑 Age:', min_value=0, step=1)
    bmi = st.number_input('⚖️ BMI:')
    children = st.number_input('👶 Number of Children:', min_value=0, step=1)

with col2:
    gender = st.radio("⚤ Gender:", ["Male", "Female"])
    smoker = st.radio("🚬 Do you smoke?", ["Yes", "No"])

model = pickle.load(open('model.pkl', 'rb'))

if st.button('🔮 Predict Premium', use_container_width=True):
    gender_enc = 1 if gender == "Female" else 0
    smoker_enc = 0 if smoker.upper() == 'NO' else 1

   
    X_test = [[age, bmi, children, gender_enc, smoker_enc]]
    yp = round(model.predict(X_test)[0], 2)

    # Output box neat look
    st.markdown(
        f"""
        <div style="padding:15px; background:linear-gradient(90deg, #89f7fe, #66a6ff);
                    border-radius:12px; text-align:center; margin-top:15px;
                    font-size:20px; color:#1B2631; font-weight:bold;">
            💰 Your Predicted Premium: <span style="color:#C0392B;">₹ {yp:,.2f}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

