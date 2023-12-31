

import streamlit as st
import altair as alt
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.sidebar.success("Selectionner un graphique.")

# Create a sample dataframe
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8],
  'Color': ['red', 'blue', 'green', 'orange', 'purple']
})

# Create a bar chart with custom colors using Altair
altair_chart = alt.Chart(data).mark_bar().encode(
    x='Value',
    y='Category',
    color='Color'
).properties(
    width=400,
    height=400,
    title='My Horizontal Bar Chart'
)

# Create a horizontal bar chart with custom colors using Plotly
plotly_chart = go.Figure(data=[go.Bar(x=data['Value'], y=data['Category'], orientation='h', marker=dict(color=data['Color']))])
plotly_chart.update_layout(title='My Horizontal Bar Chart')
plotly_chart.update_xaxes(title_text='Value')
plotly_chart.update_yaxes(title_text='Category')

# Create a horizontal bar chart with custom colors using Matplotlib
plt.barh(data['Category'], data['Value'], color=data['Color'])
plt.xlabel('Value')
plt.ylabel('Category')
plt.title('My Horizontal Bar Chart')

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
    x='Value',
    y='Category',
    color='Color'
).properties(
    width=400,
    height=400,
    title='My Horizontal Bar Chart'
)

# Display Vega-Altair Horizontal Bar Chart
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

# Create a horizontal bar chart with custom colors
plotly_chart = go.Figure(data=[go.Bar(x=data['Value'], y=data['Category'], orientation='h', marker=dict(color=data['Color']))])
plotly_chart.update_layout(title='My Horizontal Bar Chart')
plotly_chart.update_xaxes(title_text='Value')
plotly_chart.update_yaxes(title_text='Category')

# Display Plotly Horizontal Bar Chart
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
plt.barh(data['Category'], data['Value'], color=data['Color'])
plt.xlabel('Value')
plt.ylabel('Category')
plt.title('My Horizontal Bar Chart')

# Display Matplotlib Horizontal Bar Chart
st.pyplot(plt)
''', language='python')



