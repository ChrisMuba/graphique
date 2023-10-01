
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

   # Plotly
import plotly.express as px

# Create a sample dataframe
data = {
  'Category': ['A', 'B', 'C', 'D'],
  'Value': [10, 15, 7, 10]
}

# Create a pie chart
plotly_chart = px.pie(data, values='Value', names='Category', title='My Pie Chart')

# Matplotlib
import matplotlib.pyplot as plt

# Create a sample dataframe
data = {
  'Category': ['A', 'B', 'C', 'D'],
  'Value': [10, 15, 7, 10]
}

# Create a pie chart
matplotlib_chart, ax = plt.subplots()
ax.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%')
ax.set_title('My Pie Chart')



# Onglets "Altair", "Plotly" & "Bokeh"
tab1, tab2, tab3 = st.tabs(["Altair", "Plotly", "Matplotlib"])

with tab1:
   # Display Vega-Altair Chart
   st.altair_chart(altair_chart) 
   # Display Plotly Chart
with tab2:
   st.plotly_chart(plotly_chart)
   # Display Matplotlib Chart
with tab3:
   st.pyplot(matplotlib_chart)
   
# Expanders
with st.expander("Code Vega-Altair"):
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
    
    :blue[*Display Pie Chart*]
    
    st.altair_chart(altair_chart)
    """)

with st.expander("Code *Plotly*"):
    st.write("""

    :blue[*import necessary libraries*]
    
    import plotly.express as px

    :blue[*Create a sample dataframe*]
    
    data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 10]
    }

    :blue[*Create a pie chart*]
    
    plotly_chart = px.pie(data, values='Value', names='Category', title='My Pie Chart')

    :blue[*Display Pie Chart*]
    
    st.plotly_chart(plotly_chart)
    """)

with st.expander("Code *Matplotlib*"):
    st.write("""

    :blue[*import necessary libraries*]
    
    import matplotlib.pyplot as plt

    :blue[*Create a sample dataframe*]
    
    data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 10]
    }

    :blue[*Create a pie chart*]
    
   matplotlib_chart, ax = plt.subplots()
   ax.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%')
   ax.set_title('My Pie Chart')

    :blue[*Display Pie Chart*]
    
    st.pyplot(matplotlib_chart)
    """)
   











