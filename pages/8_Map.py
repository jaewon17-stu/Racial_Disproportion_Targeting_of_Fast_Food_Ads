import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and layout
st.set_page_config(page_title="Obesity Rates Map of the U.S.", layout="wide")

# Introduction
st.title("Obesity Rates in the U.S.: Highlighting the Highest and Lowest Obesity States")
st.markdown("""
This map highlights the 5 states with the **highest obesity rates** in red and the 5 states with the **lowest obesity rates** in green.
""")

# Data for obesity rates in states (mock data, replace with actual data)
data = {
    'State': ['Mississippi', 'West Virginia', 'Arkansas', 'Louisiana', 'Kentucky',   # Highest Obesity Rates
              'Colorado', 'Hawaii', 'California', 'Montana', 'New York'],           # Lowest Obesity Rates
    'Obesity Rate (%)': [39.7, 39.1, 37.4, 36.8, 36.5,                              # Highest Obesity
                         24.7, 25.0, 25.6, 26.1, 27.2],                            # Lowest Obesity
    'Code': ['MS', 'WV', 'AR', 'LA', 'KY',                                           # State Codes for Mapping
             'CO', 'HI', 'CA', 'MT', 'NY'],
    'Color': ['red', 'red', 'red', 'red', 'red',                                     # Red for Highest Obesity
              'green', 'green', 'green', 'green', 'green']                          # Green for Lowest Obesity
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Create a Plotly choropleth map
fig = px.choropleth(df, 
                    locations="Code",
                    locationmode="USA-states",
                    color="Color",
                    hover_name="State",
                    hover_data=["Obesity Rate (%)"],
                    scope="usa",
                    color_discrete_map={"red": "red", "green": "green"},
                    title="States with Highest and Lowest Obesity Rates")

# Update the layout for a cleaner map
fig.update_layout(
    geo=dict(
        showlakes=True, lakecolor='rgb(255, 255, 255)'),
    title_x=0.5
)

# Display the map in Streamlit
st.plotly_chart(fig)
