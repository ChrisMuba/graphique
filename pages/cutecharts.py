
import streamlit as st
import cutecharts

# Data for the chart
data = [10, 20, 30, 40, 50]

# Create a Streamlit app
st.title("Bar Chart Example")

# Create a Cutecharts chart
chart = cutecharts.BarChart(
    data=data,
    orientation="h",
    width=800,
    height=400,
    title="Bar Chart Example",
    x_label="Values",
    y_label="Frequency"
)

# Display the chart in the Streamlit app
st.write(chart)
