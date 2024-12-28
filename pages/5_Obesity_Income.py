import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Obesity Rates and Income Comparison", layout="wide")

# Introduction
st.title("Obesity Rates and Income: A Comparative Analysis")
st.markdown("""
This analysis examines the relationship between obesity rates and average income by comparing the 5 states with the highest obesity rates to the national average income.

We aim to answer the question: Do states with higher obesity rates also have lower-than-average income levels?
""")

# Data for states with highest obesity rates and their respective income (mock data, replace with actual data)
data = {
    'State': ['Mississippi', 'West Virginia', 'Arkansas', 'Louisiana', 'Kentucky'],
    'Obesity Rate (%)': [39.7, 39.1, 37.4, 36.8, 36.5],
    'Average Income ($)': [45000, 44000, 46000, 47000, 46500]
}

# National average income (example)
national_average_income = 65000

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the data in a table
st.subheader("States with Highest Obesity Rates and Their Average Income")
st.dataframe(df)

# Calculate income differences from the national average
df['Income Difference from National Average ($)'] = df['Average Income ($)'] - national_average_income

# Display the income difference
st.subheader("Income Difference from National Average")
st.dataframe(df[['State', 'Income Difference from National Average ($)']])

# Create a bar chart for income comparison
st.subheader("Average Income by State Compared to National Average")
fig, ax = plt.subplots()
df.plot(kind='bar', x='State', y='Average Income ($)', ax=ax, color='skyblue', label='State Income')
ax.axhline(y=national_average_income, color='red', linestyle='--', label='National Average Income')
plt.ylabel("Income ($)")
plt.title("Average Income by State Compared to National Average")
plt.legend()
st.pyplot(fig)

# Analysis explanation
st.markdown("""
### Analysis:
- The red dashed line represents the national average income.
- States with higher obesity rates (e.g., Mississippi, West Virginia) tend to have lower-than-average incomes compared to the national average.
- This data suggests a potential correlation between higher obesity rates and lower income levels, which could be explored further through deeper socioeconomic analysis.
""")
