import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("/Users/abijiththiyagarajan/Desktop/univision/MODEL/random_forest_mod.pkl", "rb") as f:
    model = pickle.load(f)

st.title("👔 Employee Attrition Prediction")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=65)
department = st.selectbox("Department", ["Sales", "HR", "Finance", "Operations", "IT"])
job_role = st.selectbox("Job Role", ["Engineer", "Manager", "Sales Rep", "Director", "Analyst"])
years_at_company = st.slider("Years at Company", 0, 40)
salary = st.number_input("Salary", min_value=1000, max_value=100000)
satisfaction_score = st.slider("Satisfaction Score (1-10)", 1, 10, 3)
performance_score = st.slider("Performance Score (1-5)", 1, 5, 3)
promotions = st.number_input("Number of Promotions", min_value=0, max_value=10, value=1)

# Derived Feature
age_years_interaction = age * years_at_company

# Manual Encoding Dictionaries
department_mapping = {
    "Finance": 0,
    "HR": 1,
    "IT": 2,
    "Operations": 3,
    "Sales": 4
}

job_role_mapping = {
    "Analyst": 0,
    "Director": 1,
    "Engineer": 2,
    "Manager": 3,
    "Sales Rep": 4
}

# Encode input
department_encoded = department_mapping[department]
job_role_encoded = job_role_mapping[job_role]

# Create input DataFrame
input_df = pd.DataFrame([[
    age, department_encoded, job_role_encoded, years_at_company, salary,
    satisfaction_score, performance_score, promotions,
    age_years_interaction
]], columns=[
    "Age", "Department", "Job Role", "Years at Company", "Salary",
    "Satisfaction Score", "Performance Score", "Promotions", "Age_Years_Interaction"
])

# Prediction
if st.button("Predict Attrition"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("❌ This employee is likely to leave the company.")
    else:
        st.success("✅ This employee is likely to stay with the company.")



# import streamlit as st
# import pickle
# import pandas as pd
# # Load the model
# with open("/Users/abijiththiyagarajan/Desktop/univision/MODEL/random_forest_model.pkl", "rb") as f:
#     model = pickle.load(f)


# st.title("👔 Employee Attrition Prediction")



# age = st.number_input("Age", min_value=18, max_value=65)
# department = st.selectbox("Department", ["Sales", "HR", "Finance", "Operations", "IT"])
# job_role = st.selectbox("Job Role", ["Engineer", "Manager", "Sales Rep", "Director", "Analyst"])
# years_at_company = st.slider("Years at Company", 0, 40)
# salary = st.number_input("Salary", min_value=1000, max_value=100000)
# satisfaction_score = st.slider("Satisfaction Score (1-10)", 1, 10, 3)
# performance_score = st.slider("Performance Score (1-5)", 1, 5, 3)
# promotions = st.number_input("Number of Promotions", min_value=0, max_value=10, value=1)
# #team_assignment = st.text_input("Team Assignment (Enter any team name)", value="Team 001")


# age_years_interaction = age * years_at_company



# input_df = pd.DataFrame([[
#     age, department, job_role, years_at_company, salary,
#     satisfaction_score, performance_score, promotions,
#     age_years_interaction
# ]], columns=[
#     "Age", "Department", "Job Role", "Years at Company", "Salary",
#     "Satisfaction Score", "Performance Score", "Promotions", "Age_Years_Interaction"
# ])





# def simple_label_encoder(value, categories):
#     return categories.index(value) if value in categories else -1  # -1 for unknowns

# input_df["Department"] = simple_label_encoder(department, ["Sales", "HR", "Finance", "Operations", "IT"])
# input_df["Job Role"] = simple_label_encoder(job_role, ["Engineer", "Manager", "Sales Rep", "Director", "Analyst"])




# if st.button("Predict Attrition"):
#     prediction = model.predict(input_df)[0]
#     if prediction == 1:
#         st.error("❌ This employee is likely to leave the company.")
#     else:
#         st.success("✅ This employee is likely to stay with the company.")
