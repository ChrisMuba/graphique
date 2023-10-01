



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

# Create tabs
tab1, tab2, tab3 = st.tabs(["Altair", "Plotly", "Matplotlib"])

# Add content to each column
with tab1:
    st.altair_chart(altair_chart)
    with st.expander("Code *Altair*"):
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
''', language='python')

with tab2:
    st.plotly_chart(plotly_chart)
    with st.expander("Code *Plotly*"):
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
''', language='python')

with tab3:
    st.pyplot(matplotlib_chart)
    with st.expander("Code *Matplotlib*"):
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
''', language='python')

