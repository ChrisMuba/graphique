
import streamlit as st
import cutecharts.charts as ccc

# Create a bar chart
chart = ccc.BarChart()

# Add data to the chart
chart.add_series(
    name="Sales",
    data=[10, 20, 30, 40, 50],
    label_opts={"position": "top"},
)

# Set the chart title
chart.set_title("Sales by Month")

# Display the chart
st.altair_chart(chart, use_container_width=True)
