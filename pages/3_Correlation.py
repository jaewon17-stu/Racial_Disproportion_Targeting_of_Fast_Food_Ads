import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Correlation Between Advertising Spending and Obesity")

# Example data for correlation analysis (same data as before)
advertising_data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Advertising Spending ($M)': [1200, 950, 850, 780, 620]
}

obesity_data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Obesity Rate (%)': [25.1, 31.4, 29.5, 30.2, 28.0]
}

# Create DataFrames
df_advertising = pd.DataFrame(advertising_data)
df_obesity = pd.DataFrame(obesity_data)

# Merge data on State
df = pd.merge(df_advertising, df_obesity, on="State")

st.subheader("Combined Data: Advertising and Obesity Rates")
st.dataframe(df)

# Correlation calculation
correlation = df['Advertising Spending ($M)'].corr(df['Obesity Rate (%)'])
st.subheader(f"Correlation between Advertising Spending and Obesity Rate: {correlation:.2f}")

# Scatter plot of the relationship
st.subheader("Advertising Spending vs Obesity Rate")
fig, ax = plt.subplots()
ax.scatter(df['Advertising Spending ($M)'], df['Obesity Rate (%)'])
plt.xlabel("Advertising Spending ($M)")
plt.ylabel("Obesity Rate (%)")
plt.title("Correlation between Advertising Spending and Obesity")
st.pyplot(fig)
