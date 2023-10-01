

import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Create a sample dataframe
data = pd.DataFrame({
   'Category': ['A', 'B', 'C', 'D'],
   'Value': [10, 15, 7, 10]
})

# Create a pie chart using Altair
altair_chart = alt.Chart(data).mark_arc().encode(
   alt.Theta('Value:Q', stack=True),
   alt.Color('Category:N')
).properties(
   width=400,
   height=400,
   title='My Pie Chart'  # Add your title here
).project(
   'identity'
)

# Create a pie chart using Plotly
plotly_chart = px.pie(data, values='Value', names='Category', title='My Pie Chart')

# Create a pie chart using Matplotlib
matplotlib_chart, ax = plt.subplots()
ax.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%')
ax.set_title('My Pie Chart')

# Create columns
col1, col2, col3 = st.columns(3)

# Add content to each column
with col1:
    st.altair_chart(altair_chart)
    st.code('''
import altair as alt
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
   'Category': ['A', 'B', 'C', 'D'],
   'Value': [10, 15, 7, 10]
})

# Create a pie chart using Altair
altair_chart = alt.Chart(data).mark_arc().encode(
   alt.Theta('Value:Q', stack=True),
   alt.Color('Category:N')
).properties(
   width=400,
   height=400,
   title='My Pie Chart'  # Add your title here
).project(
   'identity'
)

# Display Altair Pie Chart
st.altair_chart(altair_chart)
''')

with col2:
    st.plotly_chart(plotly_chart)
    st.code('''
import plotly.express as px
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
   'Category': ['A', 'B', 'C', 'D'],
   'Value': [10, 15, 7, 10]
})

# Create a pie chart using Plotly
plotly_chart = px.pie(data, values='Value', names='Category', title='My Pie Chart')

# Display Plotly Pie Chart
st.plotly_chart(plotly_chart)
''')

with col3:
    st.pyplot(matplotlib_chart)
    st.code('''
import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
   'Category': ['A', 'B', 'C', 'D'],
   'Value': [10, 15, 7, 10]
})

# Create a pie chart using Matplotlib
matplotlib_chart, ax = plt.subplots()
ax.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%')
ax.set_title('My Pie Chart')

# Display Matplotlib Pie Chart
st.pyplot(matplotlib_chart)
''')
