import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Fast Food Advertising Data")

# Load and display the advertising data (example with mock data)
data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Advertising Spending ($M)': [1200, 950, 850, 780, 620]
}

df = pd.DataFrame(data)

st.subheader("Fast Food Advertising Spending by State")
st.dataframe(df,width=800)

# Bar chart of fast food advertising spending
st.subheader("Advertising Spending (in $ Millions)")
fig, ax = plt.subplots(figsize=(8, 4))
df.plot(kind='bar', x='State', y='Advertising Spending ($M)', ax=ax)
plt.ylabel("Spending ($M)")
plt.title("Fast Food Advertising Spending by State")

st.pyplot(fig)
