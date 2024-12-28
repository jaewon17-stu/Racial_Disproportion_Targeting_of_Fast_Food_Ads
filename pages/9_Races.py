import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Racial Distribution in States with High and Low Obesity Rates", layout="wide")

# Introduction
st.title("Racial Distribution in States with Highest and Lowest Obesity Rates")
st.markdown("""
This analysis displays the racial distribution for the 5 states with the highest obesity rates and the 5 states with the lowest obesity rates, using bar charts. The top row shows the highest obesity states, and the bottom row shows the lowest obesity states.
""")

# Data for racial distribution (mock data, replace with actual data)
data_high = {
    'State': ['Mississippi', 'West Virginia', 'Arkansas', 'Louisiana', 'Kentucky'],   # Highest Obesity Rates
    'White (%)': [59, 93, 79, 60, 85],                                                # Highest Obesity White Population
    'Black (%)': [37, 4, 15, 32, 8],                                                  # Highest Obesity Black Population
    'Hispanic (%)': [3, 1, 6, 6, 3],                                                  # Highest Obesity Hispanic Population
    'Asian (%)': [1, 0.5, 1, 2, 1],                                                   # Highest Obesity Asian Population
    'Other (%)': [0, 1.5, 2, 0, 3]                                                    # Highest Obesity Other
}

data_low = {
    'State': ['Colorado', 'Hawaii', 'California', 'Montana', 'New York'],             # Lowest Obesity Rates
    'White (%)': [68, 25, 37, 87, 55],                                                # Lowest Obesity White Population
    'Black (%)': [4, 2, 6, 0.4, 15],                                                  # Lowest Obesity Black Population
    'Hispanic (%)': [22, 10, 39, 4, 20],                                              # Lowest Obesity Hispanic Population
    'Asian (%)': [3, 37, 14, 1, 8],                                                   # Lowest Obesity Asian Population
    'Other (%)': [3, 26, 4, 7, 2]                                                     # Lowest Obesity Other
}

# Convert the data into pandas DataFrames
df_highest_obesity = pd.DataFrame(data_high)
df_lowest_obesity = pd.DataFrame(data_low)

# Function to create bar charts
def create_bar_chart(row):
    labels = ['White (%)', 'Black (%)', 'Hispanic (%)', 'Asian (%)', 'Other (%)']
    sizes = [row['White (%)'], row['Black (%)'], row['Hispanic (%)'], row['Asian (%)'], row['Other (%)']]
    fig, ax = plt.subplots()
    ax.bar(labels, sizes, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
    ax.set_ylim(0, 100)  # Ensure the y-axis scale is consistent across all charts
    plt.title(f"{row['State']}")
    plt.ylabel("Percentage (%)")
    return fig

# Display bar charts for the highest obesity states in the first row
st.subheader("Racial Distribution in States with Highest Obesity Rates")

cols_high = st.columns(len(df_highest_obesity))  # Dynamically create the correct number of columns
for i, row in df_highest_obesity.iterrows():
    with cols_high[i]:
        fig = create_bar_chart(row)
        st.pyplot(fig)

# Display bar charts for the lowest obesity states in the second row
st.subheader("Racial Distribution in States with Lowest Obesity Rates")

cols_low = st.columns(len(df_lowest_obesity))  # Dynamically create the correct number of columns
for i, row in df_lowest_obesity.iterrows():
    with cols_low[i]:
        fig = create_bar_chart(row)
        st.pyplot(fig)
