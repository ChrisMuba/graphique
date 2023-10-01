

import streamlit as st
import altair as alt
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Create a sample dataframe
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8],
  'Color': ['red', 'blue', 'green', 'orange', 'purple']
})

# Create a bar chart with custom colors using Altair
altair_chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value',
    color='Color'
).properties(
    width=400,
    height=400,
    title='My Vertical Bar Chart'
)

# Create a vertical bar chart with custom colors using Plotly
plotly_chart = go.Figure(data=[go.Bar(x=data['Category'], y=data['Value'], marker=dict(color=data['Color']))])
plotly_chart.update_layout(title='My Vertical Bar Chart')
plotly_chart.update_xaxes(title_text='Category')
plotly_chart.update_yaxes(title_text='Value')

# Create a vertical bar chart with custom colors using Matplotlib
plt.bar(data['Category'], data['Value'], color=data['Color'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('My Vertical Bar Chart')

# Create tabs
tab1, tab2, tab3 = st.tabs(["Altair", "Plotly", "Matplotlib"])

# Add content to each tab
with tab1:
    st.altair_chart(altair_chart)
    with st.expander("Code *Vega-Altair*"):
        st.code('''
import streamlit as st
import altair as alt
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8],
  'Color': ['red', 'blue', 'green', 'orange', 'purple']
})

# Create a bar chart with custom colors
altair_chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value',
    color='Color'
).properties(
    width=400,
    height=400,
    title='My Vertical Bar Chart'
)

# Display Vega-Altair Vertical Bar Chart
st.altair_chart(altair_chart)
''', language='python')

with tab2:
    st.plotly_chart(plotly_chart)
    with st.expander("Code *Plotly*"):
        st.code('''
import streamlit as st
import plotly.graph_objects as go

# Create a sample data
data = {
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8],
  'Color': ['red', 'blue', 'green', 'orange', 'purple']
}

# Create a vertical bar chart with custom colors
plotly_chart = go.Figure(data=[go.Bar(x=data['Category'], y=data['Value'], marker=dict(color=data['Color']))])
plotly_chart.update_layout(title='My Vertical Bar Chart')
plotly_chart.update_xaxes(title_text='Category')
plotly_chart.update_yaxes(title_text='Value')

# Display Plotly Vertical Bar Chart
st.plotly_chart(plotly_chart)
''', language='python')

with tab3:
    st.pyplot(plt)
    with st.expander("Code *Matplotlib*"):
        st.code('''
import streamlit as st
import matplotlib.pyplot as plt

# Create a sample data
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8],
  'Color': ['red', 'blue', 'green', 'orange', 'purple']
})

# Create a bar chart with custom colors
plt.bar(data['Category'], data['Value'], color=data['Color'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('My Vertical Bar Chart')

# Display Matplotlib Vertical Bar Chart
st.pyplot(plt)
''', language='python')




