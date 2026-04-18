from src.placement_prediction.exception import Cu_Exception
import pandas as pd
import sys
import pickle
import streamlit as st
from pymongo import MongoClient
import os

if __name__ == "__main__":
    try:

        # 🔥 MongoDB Connection (SAFE VERSION)
        MONGO_URI = os.getenv("MONGO_URI")

        if not MONGO_URI:
            st.error("❌ MONGO_URI not found. Check Render environment variable.")
            st.stop()

        client = MongoClient(
            MONGO_URI,
            tls=True,
            tlsAllowInvalidCertificates=True  # 🔥 Fix SSL issue
        )

        db = client["placement_db"]
        collection = db["students"]

        # Title
        st.title("🎓 Placement Prediction App")

        # Load model and preprocessor
        model = pickle.load(open("artifacts/model.pkl", "rb"))
        preprocessor = pickle.load(open("artifacts/Data_Preprocessing.pkl", "rb"))

        st.header("Enter Student Details")

        # Inputs
        cgpa = st.number_input("CGPA", min_value=3.5, max_value=10.0, step=0.2)

        branch = st.selectbox(
            "Branch",
            ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil"]
        )

        college_tier = st.selectbox(
            "College Tier",
            ["Tier 1", "Tier 2", "Tier 3"]
        )

        internships_count = st.number_input("Internships Count", min_value=0, step=1)
        projects_count = st.number_input("Projects Count", min_value=0, step=1)
        certifications_count = st.number_input("Certifications Count", min_value=0, step=1)

        communication_skill_score = st.slider("Communication Skill Score", 0, 10)
        backlogs = st.number_input("Backlogs", min_value=0, step=1)

        # 🔮 Predict button
        if st.button("Predict Placement"):

            data = {
                "cgpa": [cgpa],
                "branch": [branch],
                "college_tier": [college_tier],
                "internships_count": [internships_count],
                "projects_count": [projects_count],
                "certifications_count": [certifications_count],
                "communication_skill_score": [communication_skill_score],
                "backlogs": [backlogs]
            }

            df = pd.DataFrame(data)

            # Preprocess
            transformed_data = preprocessor.transform(df)

            # Predict
            prediction = model.predict(transformed_data)
            result = "Placed" if prediction[0] == 1 else "Not Placed"

            if prediction[0] == 1:
                st.success("✅ Student is likely to be PLACED")
            else:
                st.error("❌ Student is likely to be NOT PLACED")

            # 💾 Save to MongoDB
            try:
                save_data = {
                    "cgpa": cgpa,
                    "branch": branch,
                    "college_tier": college_tier,
                    "internships_count": internships_count,
                    "projects_count": projects_count,
                    "certifications_count": certifications_count,
                    "communication_skill_score": communication_skill_score,
                    "backlogs": backlogs,
                    "prediction": result
                }

                collection.insert_one(save_data)
                st.success("📁 Data saved successfully!")

            except Exception as db_error:
                st.error(f"❌ Failed to save data: {db_error}")

        # 📊 Show Stored Data
        if st.button("Show Stored Data"):
            try:
                data = list(collection.find({}, {"_id": 0}))

                if data:
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                else:
                    st.warning("No data found")

            except Exception as fetch_error:
                st.error(f"❌ Error fetching data: {fetch_error}")

    except Exception as e:
        st.error(f"❌ App crashed: {e}")
        raise Cu_Exception(e, sys)
