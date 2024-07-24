INTRODUCTION:
Diagnolytics is a machine learning solution worked on by Team ALAN of the AI/ML Section of the QuintAfriq xPloreCSR programme
Diagnolytics is a solution that enlightens patients on the status of the medical tests taken after/during hospitalization

ABOUT:
DIAGNOLYTICS is an AI-based solution that simplifies medical test results with just a little medical information inputted.
It uses features like the length of stay at the hospital, medications prescribed, medical condition, medical fees and a few other information to predict the severity of the patient’s test results.
Patients often get discharged without fully understanding the severity of their conditions, which can often be explained by their test results.

DATA SOURCE:
The data was sourced from Kaggle and provided by the instructors of the AI/ML Track
The dataset contains the following columns:
    - Name
    - Age
    - Blood Type
    - Medical Condition
    - Date of Admission
    - Doctor
    - Hospital
    - Insurance Provider
    - Billing Amount
    - Room Number
    - Admission Type
    - Discharge Date
    - Medication
    - Test Results (An indicator of the normalcy of the patient's test result)
                    
This is a multi-classification problem.

DATA STRUCTURE:
The data contained 55,500 rows and 15 columns of information

DATA PREPROCESSING:
LabelBinarizer and LabelEncoder were used to transform several columns, like “Test Results”, “Admission Type” and “Gender”

FEATURE ENGINEERING:
A few columns that were deemed irrelevant to the model building process were dropped. E.g. “Name”, “Room Number”, “Insurance Provider” etc. One extra column (“Days Hospitalized”) was engineered from two different columns (“Date of Admission” and “Discharge Date”)

MODEL TRAINING AND EVALUATION:
The dataset was split into two parts: 80% for the training data and 20% for the testing data
With up to 8 different algorithm used, we went with the model with the best accuracy score
The baseline model of the data provider, using the Random Forest Classifier, had an accuracy of 34%

LIST OF MODELS USED AND ACCURACY ACHIEVED:
Logistic Regression - 33.8%
Gaussian NB - 33.6%
Gradient Boosting Classifier - 34.5%
Decision Tree Classifier - 40.6%
K-Neighbors Classifier - 36.6%
Support Vector Classifier - 33.3%
eXtreme Gradient Boosting Classifier - 36.1%
Random Forest Classifier - 44.0%

MODEL DEPLOYMENT:
The model was successfully deployed locally using Streamlit. 
It functioned according to expectations and the results were colour-themed.

CONCLUSION:
With over 79% of the Nigerian population unfamiliar with medical terms, DIAGNOLYTICS is expected to help patients with clarification in understanding the severity of their medical conditions using the little information they have access to.
