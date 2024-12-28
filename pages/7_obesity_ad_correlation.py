import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Fast Food Ad Spending: Highest vs Lowest Obesity States", layout="wide")

# Introduction
st.title("Fast Food Ad Spending: Comparison Between States with Highest and Lowest Obesity Rates")
st.markdown("""
This analysis compares the **fast food advertising spending** between the 5 states with the **highest obesity rates** and the 5 states with the **lowest obesity rates**.

We aim to answer the question: Do states with lower obesity rates spend less on fast food advertising compared to states with higher obesity rates?
""")

# Data for fast food advertising spending in states with highest and lowest obesity rates (mock data, replace with actual data)
data = {
    'State': ['Mississippi', 'West Virginia', 'Arkansas', 'Louisiana', 'Kentucky',   # Highest Obesity Rates
              'Colorado', 'Hawaii', 'California', 'Montana', 'New York'],          # Lowest Obesity Rates
    'Obesity Rate (%)': [39.7, 39.1, 37.4, 36.8, 36.5,                              # Highest Obesity
                         24.7, 25.0, 25.6, 26.1, 27.2],                            # Lowest Obesity
    'Fast Food Ad Spending ($M)': [500, 450, 480, 490, 470,                         # Highest Obesity Fast Food Spending
                                   200, 180, 220, 190, 210]                        # Lowest Obesity Fast Food Spending
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Sort the data by Fast Food Ad Spending in descending order
df_sorted = df.sort_values(by='Fast Food Ad Spending ($M)', ascending=False)

# Display the data in a table
st.subheader("Fast Food Advertising Spending in States with Highest and Lowest Obesity Rates (Sorted by Ad Spending)")
st.dataframe(df_sorted)

# Define colors: Red for the top 5 states (highest obesity) and Green for the bottom 5 states (lowest obesity)
colors = ['red' if i < 5 else 'green' for i in range(len(df_sorted))]

# Create a bar chart for fast food ad spending comparison (sorted)
st.subheader("Fast Food Advertising Spending Comparison (Sorted by Ad Spending)")
fig, ax = plt.subplots(figsize=(10, 6))  # Increase figure size to fit the labels
df_sorted.plot(kind='bar', x='State', y='Fast Food Ad Spending ($M)', ax=ax, color=colors, legend=False)

# Rotate the x-axis labels to make state names clear
plt.xticks(rotation=45, ha='right')

plt.ylabel("Fast Food Ad Spending ($M)")
plt.title("Fast Food Ad Spending by State (Sorted by Ad Spending)")
plt.tight_layout()  # To make sure everything fits into the layout
st.pyplot(fig)

# Analysis explanation
st.markdown("""
### Analysis:
- The bar chart shows fast food advertising spending in descending order, with the top 5 states with the highest obesity rates highlighted in **red**.
- States with higher obesity rates (e.g., **Mississippi**, **West Virginia**) are generally spending more on fast food advertising compared to states with lower obesity rates (e.g., **Colorado**, **Hawaii**), which are highlighted in **green**.
- This data suggests a potential relationship between higher fast food ad spending and higher obesity rates, but further analysis would be needed to account for other factors like income, availability of healthy food options, and public health campaigns.
""")
