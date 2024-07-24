import pandas as pd
import streamlit as st
import pickle 

filename = 'final_health_model.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Health Test Result App')
st.subheader("""This app takes in certain variables to enable prediction of your hospital test result""")

def user_input():
    Age = st.number_input('How old are you?', min_value = 13, max_value = 89)
    Gender = st.selectbox('What is your gender?',  options = ['Female', 'Male'], index = 0)
    BloodType = st.selectbox('What is your blood type?',  options = ['A-', 'A+', 'AB-', 'AB+', 'B-', 'B+', 'O-', 'O+'], index = 0)
    MedicalCondition = st.selectbox('What is your medical condition?',  options = ['Arthritis', 'Asthma','Cancer', 'Diabetes', 'Hypertension', 'Obesity'], index = 0)
    BillingAmount = st.number_input('How much is your bill?', min_value = -3000.0, max_value = 75000.0)
    AdmissionType = st.selectbox('What is your admission type?',  options = ['Elective', 'Emergency', 'Urgent'], index = 0)
    Medication = st.selectbox('What is your medication?',  options = ['Aspirin', 'Ibuprofen', 'Lipitor', 'Paracetamol', 'Penicillin'], index = 0)
    DaysHospitalized = st.number_input('How many days did you spend in the hospital?', min_value = 1, max_value = 30)


    #Mapping the values
    gender_mapping = {'Male': 1, 'Female': 0}
    blood_type_mapping = {'A-': 0, 'A+': 1, 'AB-': 2, 'AB+': 3, 'B-': 4, 'B+': 5, 'O-': 6, 'O+': 7}
    medical_condition_mapping = {'Arthritis': 0, 'Asthma': 1,'Cancer': 2, 'Diabetes': 3, 'Hypertension': 4, 'Obesity': 5}
    admission_type_mapping = {'Elective': 0, 'Emergency': 1, 'Urgent': 2}
    medication_mapping = {'Aspirin': 0, 'Ibuprofen': 1, 'Lipitor': 2, 'Paracetamol': 3, 'Penicillin': 4}

    data = {
        'Age': Age,
        'Gender': gender_mapping[Gender],
        'Blood Type': blood_type_mapping[BloodType],
        'Medical Condition': medical_condition_mapping[MedicalCondition],
        'Billing Amount': BillingAmount,
        'Admission Type': admission_type_mapping[AdmissionType],
        'Medication': medication_mapping[Medication],
        'Days Hospitalized': DaysHospitalized
    }

    features = pd.DataFrame(data, index = [0])
    return features

df = user_input()

def prediction():
    predict_ = model.predict(df)

    if predict_ == 0:
        result = 'Abnormal'
    

    elif predict_ == 1:
        result = 'Inconclusive'


    elif predict_ == 2:
        result = 'Normal'


    else:
        result = 'Null'

    return result

# Prediction button
if st.button("Predict"):
    result_ = prediction()

    if result_ == 'Abnormal':
        st.success("Predicted Test Result: :red[{}]".format(result_))

    elif result_ == 'Inconclusive':
        st.success("Predicted Test Result: :blue[{}]".format(result_))

    elif result_ == 'Normal':
        st.success("Predicted Test Result: {}".format(result_))





    