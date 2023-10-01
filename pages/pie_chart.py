
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

    *Create a sample dataframe*
    
    data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 10]
    })

    *Create a pie chart*
    
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
    
    *Display Pie Chart*
    
    st.altair_chart(chart)
    """)
