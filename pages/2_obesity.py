import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Obesity Data by State")

# Load and display the obesity data (example with mock data)
data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Obesity Rate (%)': [25.1, 31.4, 29.5, 30.2, 28.0]
}

df = pd.DataFrame(data)

st.subheader("Obesity Rates by State")
st.dataframe(df)

# Bar chart of obesity rates
st.subheader("Obesity Rates (%)")
fig, ax = plt.subplots()
df.plot(kind='bar', x='State', y='Obesity Rate (%)', ax=ax, color='orange')
plt.ylabel("Obesity Rate (%)")
plt.title("Obesity Rates by State")
st.pyplot(fig)
