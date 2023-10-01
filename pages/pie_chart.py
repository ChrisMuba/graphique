
import streamlit as st
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

st.altair_chart(chart)

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


import plotly.express as px

# Create a sample dataframe
data = {
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8]
}

# Create a pie chart
fig = px.pie(data, values='Value', names='Category', title='My Pie Chart')

st.plotly_chart(fig)


import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("Altair")
    st.altair_chart(chart)

with col2:
   st.header("Plotly")
   st.plotly_chart(fig)












