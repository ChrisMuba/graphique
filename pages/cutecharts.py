
import streamlit as st
import altair as alt
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8]
})

# Create a pie chart
chart = alt.Chart(data).mark_arc().encode(
    alt.Theta('Value:Q', stack=True),
    alt.Color('Category:N')
).properties(
    width=400,
    height=400
).project(
    'identity'
)

st.altair_chart(chart)
