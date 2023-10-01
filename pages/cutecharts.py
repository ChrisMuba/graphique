
import streamlit as st
from cutecharts.charts import Line

# Create a line chart
chart = Line("Line Chart")
chart.set_options(
    labels=["A", "B", "C", "D", "E", "F", "G"],
    x_label="I'm xlabel",
    y_label="I'm ylabel",
)
chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])

# Display the chart in the Streamlit app
st.altair_chart(chart, use_container_width=True)
