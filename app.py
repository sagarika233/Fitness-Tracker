import streamlit as st
import pandas as pd
from tracker import FitnessTracker
from user import User

# App Title
st.title("🏋️‍♂️ Fitness Tracker Dashboard")

# Sidebar for User Info
st.sidebar.header("User Information")
name = st.sidebar.text_input("Name", "John Doe")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)

user = User(name, age, weight, height)
tracker = FitnessTracker(user)

# Main Tabs 
tab1, tab2 = st.tabs(["📋 Log Workout", "📊 Workout History"])

# Workout Logging
with tab1:
    st.subheader("Log Your Workout")
    workout_type = st.selectbox("Workout Type", ["Running", "Cycling", "Swimming", "Gym"])
    duration = st.number_input("Duration (minutes)", min_value=1, value=30)
    calories = st.number_input("Calories Burned", min_value=1, value=200)

    if st.button("Log Workout"):
        tracker.log_workout(workout_type, duration, calories)
        st.success("Workout logged successfully!")

# Workout History & Visualization
with tab2:
    st.subheader("Workout History")
    workouts = tracker.view_workouts()

    if workouts:
        df = pd.DataFrame(workouts)
        st.dataframe(df)

        # Visualization
        st.subheader("Workout Trends")
        st.bar_chart(df.groupby("type")["calories"].sum())
    else:
        st.warning("No workout history found.")
