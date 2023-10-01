
import streamlit as st

# Vega-Altair
import altair as alt
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
   'Category': ['A', 'B', 'C', 'D'],
   'Value': [10, 15, 7, 10]
})

# Create a pie chart
chart = alt.Chart(data).mark_arc().encode(
   alt.Theta('Value:Q', stack=True),
   alt.Color('Category:N')
).properties(
   width=400,
   height=400,
   title='My Pie Chart'  # Add your title here
).project(
   'identity'
)



   #Plotly
import plotly.express as px

# Create a sample dataframe
data = {
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8]
}

# Create a pie chart
fig = px.pie(data, values='Value', names='Category', title='My Pie Chart')



tab1, tab2 = st.tabs(["Altair", "Plotly"])

with tab1:
   #Display Vega-Altair Chart
   st.altair_chart(chart) 
   #Display Plotly Chart
with tab2:
   st.plotly_chart(fig)
   


with st.expander("Code"):
st.write("""

    :blue[*import necessary libraries*]
    
    import streamlit as st
    import altair as alt
    import pandas as pd

    :blue[*Create a sample dataframe*]
    
    data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 10]
    })

    :blue[*Create a pie chart*]
    
    chart = alt.Chart(data).mark_arc().encode(
        alt.Theta('Value:Q', stack=True),
        alt.Color('Category:N')
    ).properties(
        width=400,
        height=400,
        title='My Pie Chart'  # Add your title here
    ).project(
        'identity'
    )
    
    :blue[*Display Pie Chart*]
    
    st.altair_chart(chart)
    """)

with st.expander("Code"):
    st.write("""

    :blue[*import necessary libraries*]
    
    import plotly.express as px

    :blue[*Create a sample dataframe*]
    
    data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 15, 7, 10, 8]
    }

    :blue[*Create a pie chart*]
    
    fig = px.pie(data, values='Value', names='Category', title='My Pie Chart')

    :blue[*Display Pie Chart*]
    
    st.plotly_chart(fig)
    """)
   











