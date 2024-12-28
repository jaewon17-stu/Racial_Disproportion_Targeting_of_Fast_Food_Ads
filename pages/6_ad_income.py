import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Fast Food Advertising Spending vs Total Ad Spending", layout="wide")

# Introduction
st.title("Fast Food Advertising Spending vs Total Ad Spending in States with High Obesity Rates")
st.markdown("""
This analysis compares the fast food advertising spending in 5 states with the highest obesity rates to the total advertising spending in the U.S. 

We aim to answer the question: Do states with higher obesity rates also have higher fast food ad spending compared to the total ad spending?
""")

# Data for fast food advertising spending in 5 states with highest obesity rates (mock data, replace with actual data)
data = {
    'State': ['Mississippi', 'West Virginia', 'Arkansas', 'Louisiana', 'Kentucky'],
    'Fast Food Ad Spending ($M)': [500, 450, 480, 490, 470],  # Example fast food ad spending in millions
    'Total Ad Spending ($M)': [1500, 1400, 1450, 1475, 1425]  # Example total ad spending in millions
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the data in a table
st.subheader("Fast Food Advertising Spending vs Total Ad Spending")
st.dataframe(df)

# Calculate the percentage of fast food ad spending from the total ad spending
df['Fast Food Ad Spending (%)'] = (df['Fast Food Ad Spending ($M)'] / df['Total Ad Spending ($M)']) * 100

# Display the percentage
st.subheader("Percentage of Fast Food Ad Spending from Total Ad Spending")
st.dataframe(df[['State', 'Fast Food Ad Spending (%)']])

# Create a bar chart for fast food ad spending percentage
st.subheader("Fast Food Advertising Spending as a Percentage of Total Ad Spending")
fig, ax = plt.subplots()
df.plot(kind='bar', x='State', y='Fast Food Ad Spending (%)', ax=ax, color='lightgreen', label='Fast Food Ad Spending (%)')
plt.ylabel("Percentage (%)")
plt.title("Fast Food Ad Spending as a Percentage of Total Ad Spending")
st.pyplot(fig)

# Analysis explanation
st.markdown("""
### Analysis:
- The bar chart shows how much of the total advertising budget in each state is allocated to fast food advertising.
- States with higher obesity rates such as **Mississippi** and **West Virginia** also show a relatively high percentage of their total ad spending going to fast food.
- Further analysis could involve comparing fast food ad spending to other variables like access to healthy food options and public health initiatives.
""")
