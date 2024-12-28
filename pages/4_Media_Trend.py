import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Advertising Mediums and Spending Trends in 2023", layout="wide")

# Introduction
st.title("Advertising Mediums and Spending Trends in 2023")
st.markdown("""
In 2023, advertising in the U.S. has been shaped by the rapid growth of digital channels, especially **mobile** and **video advertising**, along with the rise of **programmatic advertising**. Traditional offline media like TV and radio have seen a decline, while specific niches remain viable. Here are some key insights:
""")

# Data for advertising mediums in 2023
data = {
    'Medium': ['Mobile Advertising', 'Video Advertising', 'Programmatic Advertising', 'Offline Media', 'Out-of-home Advertising'],
    'Spending ($B)': [623, 50, 43, 150, 35],  # Example spending data
}

df = pd.DataFrame(data)

# Display table
st.subheader("Advertising Mediums and Spending Trends")
st.dataframe(df)

# Create a pie chart for ad spending with a start angle of 30 degrees
st.subheader("Advertising Spending by Medium (in $ Billions)")
fig, ax = plt.subplots()
ax.pie(df['Spending ($B)'], labels=df['Medium'], autopct='%1.1f%%', startangle=30, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title("Advertising Spending by Medium in 2023")
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)

# Trends Explanation
st.markdown("""
### Key Trends:
1. **Mobile Advertising**: Continues to grow rapidly, driven by the increasing number of mobile users and social media platforms like Instagram and TikTok.
2. **Video Advertising**: Short-form videos and platforms such as YouTube have attracted significant ad spending, with video advertising growing by 49% year-on-year.
3. **Programmatic Advertising**: Automated, real-time bidding for ad inventory has made programmatic advertising highly efficient and effective.
4. **Offline Media**: Traditional channels like TV and radio are facing declines but still hold value for targeting specific demographics.
5. **Out-of-home (OOH) Advertising**: Continues to grow as it adapts to new digital formats like billboards and experiential marketing.

These statistics show how digital channels have taken the lead, while traditional media continues to adapt to the changing landscape.

**Sources**:
- [Publift Advertising Trends 2023](https://www.publift.com)
- [Statista Digital Advertising Trends](https://www.statista.com)
""")
