# app.py

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

base_path = os.path.dirname(os.path.abspath(__file__))

# Set the page configuration to wide layout
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Increase label font size */
    label[data-testid="stWidgetLabel"] > div {
        font-size: 30px !important;   /* adjust size */
        font-weight: bold !important; /* make bold */
        color: #F5F5DC !important;      /* label color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Function to load the machine learning model
@st.cache_resource(show_spinner=False)
def load_model(model_file):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, model_file)

    try:
        # Use a with statement to safely handle the file
        with open(full_path, "rb") as f:
            return joblib.load(f)
    except FileNotFoundError:
        st.error(f"Error: The model file '{model_file}' was not found. Please ensure it is in the 'models' directory.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        st.stop()

# Function to refresh all inputs to their default value
def refresh_page():
    st.session_state.age = 0
    st.session_state.bilirubin = 0.0
    st.session_state.alk_phosphate = 0
    st.session_state.sgot = 0
    st.session_state.albumin = 0.0
    st.session_state.protime = 0.0
    st.session_state.sex = "Male"
    st.session_state.steroid = "No"
    st.session_state.antivirals = "No"
    st.session_state.fatigue = "No"
    st.session_state.spiders = "No"
    st.session_state.ascites = "No"
    st.session_state.varices = "No"
    st.session_state.histology = "No"

# --- Custom CSS for Styling ---
background_image_url = 'https://static.vecteezy.com/system/resources/previews/000/431/192/original/human-liver-on-red-background-vector.jpg'

st.markdown("""
<style>
/* ===== Layout you already had ===== */
.st-emotion-cache-wfksaw{
  display:flex;gap:1rem;width:50%;max-width:100%;height:100%;min-width:1rem;
  flex-flow:column;flex:1 1 0%;align-items:center;justify-content:center;margin:0 auto;
}

/* ⚠️ Scope your general text color to the page content only (so it DOESN'T hit the dropdown portal) */
.stApp .main .block-container p,
.stApp .main .block-container li,
.stApp .main .block-container .st-ag{
  color:#F0EAD6 !important;
  font-size:2rem !important;
}

@supports (scrollbar-color:transparent transparent){
  *{scrollbar-width:thin;scrollbar-color:transparent transparent;}
}
*,::before,::after{box-sizing:border-box;}

.main-title{
  text-align:center;font-size:5.5rem !important;font-weight:900;color:#fff !important;
  text-shadow:5px 5px 12px #000;margin:20px 0;line-height:1.1;
}
.sub-title{
  padding-left:162px !important;text-align:left;font-size:2.5rem !important;font-weight:700;
  color:#FFD700 !important;text-shadow:2px 2px 5px #000;margin-bottom:30px;display:block;
}
.section-header{
  padding-left:162px !important;font-size:1.8rem !important;font-weight:700;color:#ADD8E6 !important;
  text-shadow:1px 1px 4px #000;margin-bottom:20px;display:block;margin-left:0;
}
.patient-attributes-title{
  font-size:2rem !important;font-weight:700;color:#ADD8E6 !important;text-shadow:1px 1px 4px #000;
  margin-bottom:20px;margin-left:162px !important;display:block;margin-top:0 !important;
}

.stApp{
  background-image:url("https://static.vecteezy.com/system/resources/previews/000/431/192/original/human-liver-on-red-background-vector.jpg");
  background-size:cover;background-position:center;background-repeat:no-repeat;background-attachment:fixed;
}
.stApp::before{
  content:"";position:absolute;inset:0;background-color:rgba(0,0,0,.4);
}
.main .block-container{background-color:transparent;color:#fff;font-size:3rem;}
h1,h2,h3,h4,h5,h6{color:#ADD8E6 !important;text-shadow:2px 2px 4px #000;}

.st-emotion-cache-1h61j49,.st-emotion-cache-pkj50z{
  background-color:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.5);color:#fff;font-size:2rem;
}
.st-emotion-cache-1r6g21x,.st-emotion-cache-186s5zh,.st-emotion-cache-18aao1k{
  color:#fff;font-size:3rem !important;
}
/* Make buttons full-width pink bars */
    div.stButton > button {
        width: 100%;               /* stretch across column */
        height: 50px;              /* taller button */
        font-size: 5rem !important;           /* bigger text */
        font-weight: bold;
        border-radius: 10px;       /* rounded corners */
        background-color: #FF4B6E; /* pink button */
        color: white;              /* white text */
        border: none;
    }
            
            

    /* Hover effect */
    div.stButton > button:hover {
        background-color: #ff1c4c; /* darker pink */
        color: white;
    }
/* ===== FINAL, ROBUST SELECTBOX FIX ===== */
/* Selected value in the closed select */
div[data-baseweb="select"] [role="button"],
div[data-baseweb="select"] [aria-haspopup="listbox"],
div[data-baseweb="select"] [class*="singleValue"],
div[data-baseweb="select"] [class*="value"]{
  color:#000 !important;           /* make selected text black */
}

/* The dropdown menu lives in a portal. Target it by role, not by container */
[role="listbox"], 
[role="listbox"] *, 
[role="option"], 
[role="option"] *{
  color:#000 !important;           /* force options text black */
  opacity:1 !important;
}

/* Hover/selected option highlight */
[role="listbox"] [aria-selected="true"],
[role="listbox"] [role="option"]:hover{
  background:#f0f0f0 !important;
  color:#000 !important;
}

/* Optional: make the select background white so black text pops */
div[data-baseweb="select"]{
  background:#fff !important;
  border-radius:12px;
}
  /* Force smaller warning text inside alert boxes */
div[data-testid="stAlert"] {
    font-size: 18px !important;
    line-height: 1.2 !important;
            color: white !important;  
}

div[data-testid="stAlert"] p {
    font-size: 18px !important;
    line-height: 1.2 !important;
            color: white !important;  
}

div[data-testid="stAlert"] span {
    font-size: 18px !important;
    line-height: 1.2 !important;
            color: white !important;  
}

</style>

<!-- Title -->
<h1 class="main-title">HUMAN LIVER ANALYSIS</h1>
<h2 class="sub-title">Enter Patient's data:</h2>
<h3 class="section-header">Patient Vitals</h3>
""", unsafe_allow_html=True)


# --- App Title and Header ---

# Initialize session state for all input values
if 'age' not in st.session_state:
    st.session_state.age = 0
    st.session_state.bilirubin = 0.0
    st.session_state.alk_phosphate = 0
    st.session_state.sgot = 0
    st.session_state.albumin = 0.0
    st.session_state.protime = 0.0
    st.session_state.sex = "Male"
    st.session_state.steroid = "No"
    st.session_state.antivirals = "No"
    st.session_state.fatigue = "No"
    st.session_state.spiders = "No"
    st.session_state.ascites = "No"
    st.session_state.varices = "No"
    st.session_state.histology = "No"

# Create a flag to track if all inputs are valid
is_valid_input = True

# --- Input Form ---
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # Age Input and Validation (Range: 0 to 90)
        age = st.number_input("Age", min_value=0, key="age")  # no max_value

        # Custom check instead of Streamlit's orange popup
        if not (0 <= age <= 90):
            st.warning("Age should be in this range (0–90).")
            is_valid_input = False



        # Bilirubin Input and Validation (Range: 0.0 to 75.0)
        st.number_input("Total Bilirubin", min_value=0.0, format="%.2f", value=st.session_state.bilirubin, key="bilirubin")
        if not (0.0 <= st.session_state.bilirubin <= 75.0):
            st.warning("Total Bilirubin should be in(0.0-75.0).")
            is_valid_input = False

        # Alk Phosphate Input and Validation (Range: 0 to 2110)
        st.number_input("Alk Phosphate", min_value=0, value=st.session_state.alk_phosphate, key="alk_phosphate")
        if not (0 <= st.session_state.alk_phosphate <= 2110):
            st.warning("Alk Phosphate should be in this(0-2110).")
            is_valid_input = False

    with col2:
        # Sgot Input and Validation (Range: 0 to 4929)
        st.number_input("Sgot (AST)", min_value=0, value=st.session_state.sgot, key="sgot")
        if not (0 <= st.session_state.sgot <= 4929):
            st.warning("Sgot should be in this range (0-4929).")
            is_valid_input = False

        # Albumin Input and Validation (Range: 0.0 to 5.5)
        st.number_input("Albumin", min_value=0.0, format="%.2f", value=st.session_state.albumin, key="albumin")
        if not (0.0 <= st.session_state.albumin <= 5.5):
            st.warning("Albumin should be in this (0.0-5.5).")
            is_valid_input = False

        # Protime Input and Validation (Range: 0.0 to 150.0)
        st.number_input("Protime", min_value=0.0, value=st.session_state.protime, key="protime")
        if not (0.0 <= st.session_state.protime <= 150.0):
            st.warning("Protime should be in(0.0-150.0).")
            is_valid_input = False

st.markdown("<hr style='margin: 1px 0;'>", unsafe_allow_html=True)
st.markdown('<h2 class="patient-attributes-title">Patient Attributes</h2>', unsafe_allow_html=True)
with st.container():
    col3, col4 = st.columns(2)

    with col3:
        st.selectbox("Gender", options=["Male", "Female", "Other"], key="sex")
        st.selectbox("Steroid", options=["No", "Yes"], key="steroid")
        st.selectbox("Antivirals", options=["No", "Yes"], key="antivirals")
        st.selectbox("Fatigue", options=["No", "Yes"], key="fatigue")

    with col4:
        st.selectbox("Spiders", options=["No", "Yes"], key="spiders")
        st.selectbox("Ascites", options=["No", "Yes"], key="ascites")
        st.selectbox("Varices", options=["No", "Yes"], key="varices")
        st.selectbox("Histology", options=["No", "Yes"], key="histology")

# Create a container for the buttons to be on the same line
st.markdown("<hr style='margin:25px 0;'>", unsafe_allow_html=True)
button_col1, button_col2 = st.columns(2)


with button_col1:
    predict_button = st.button("Predict", use_container_width=True)

with button_col2:
    refresh_button = st.button("Refresh", on_click=refresh_page, use_container_width=True)

# Handle the prediction logic
if predict_button:
    # Check if all numerical inputs are at their default value of 0
    is_default_input = (st.session_state.age == 0 and
                        st.session_state.bilirubin == 0.0 and
                        st.session_state.alk_phosphate == 0 and
                        st.session_state.sgot == 0 and
                        st.session_state.albumin == 0.0 and
                        st.session_state.protime == 0.0)

    if is_default_input:
        st.error("Please enter patient data to get a prediction.")
    elif not is_valid_input:
        st.error("Please fix the warnings above to get a valid prediction.")
    else:
        # Convert categorical inputs to numerical format
        sex_encoded = 1 if st.session_state.sex == "Male" else 2
        steroid_encoded = 1 if st.session_state.steroid == "Yes" else 2
        antivirals_encoded = 1 if st.session_state.antivirals == "Yes" else 2
        fatigue_encoded = 1 if st.session_state.fatigue == "Yes" else 2
        spiders_encoded = 1 if st.session_state.spiders == "Yes" else 2
        ascites_encoded = 1 if st.session_state.ascites == "Yes" else 2
        varices_encoded = 1 if st.session_state.varices == "Yes" else 2
        histology_encoded = 1 if st.session_state.histology == "Yes" else 2

        # Prepare data for the model
        single_data = [
            st.session_state.age, sex_encoded, steroid_encoded, antivirals_encoded, fatigue_encoded,
            spiders_encoded, ascites_encoded, varices_encoded, st.session_state.bilirubin,
            st.session_state.alk_phosphate, st.session_state.sgot, st.session_state.albumin,
            st.session_state.protime, histology_encoded
        ]
        numerical_data = np.array(single_data).reshape(1, -1)

        # Load model & make a prediction
        model = load_model("models/logistic_regression_hepB_model.pkl")
        prediction = model.predict(numerical_data)
        pred_prob = model.predict_proba(numerical_data)

        prediction_label = {1: "LIVER DISEASE POSITIVE", 2: "LIVER DISEASE NEGATIVE"}
        final_result = prediction_label.get(prediction[0])

        st.subheader("Prediction Results")
        st.success(f"Prediction: {final_result}")

        st.subheader("Prediction Probability Scores")

        pred_probability_score = {
    "LIVER DISEASE POSITIVE": round(pred_prob[0][0] * 100, 2),
    "LIVER DISEASE NEGATIVE": round(pred_prob[0][1] * 100, 2),
    }



        for key, value in pred_probability_score.items():
            st.markdown(
                f"""
                <div style="font-size:18px; font-weight:bold; color:white;">
                    {key}: {value}%
                </div>
                """,
                unsafe_allow_html=True
            )
