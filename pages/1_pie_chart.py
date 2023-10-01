
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

# Create tabs
tabs = st.tabs(["Vega-Altair", "Plotly", "Matplotlib"])

if tabs[0]:
    # Display Vega-Altair Chart
    st.altair_chart(altair_chart)
    # Display Vega-Altair Code
    with st.expander("Code Vega-Altair"):
        st.code("""
        #import necessary libraries
        
        import streamlit as st
        
        import altair as alt
        
        import pandas as pd
    
        #Create a sample dataframe
        
        data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 10]
        })
    
        #Create a pie chart
        
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
        
        # Display Pie Chart
        
        st.altair_chart(altair_chart)
        """)
elif tabs[1]:
    # Display Plotly Chart
    st.plotly_chart(plotly_chart)
    # Display Plotly Code
    with st.expander("Code Plotly"):
        st.code("""
        # import necessary libraries
        
        import plotly.express as px
    
        # Create a sample dataframe
        
        data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 10]
        }
    
        # Create a pie chart
        
        plotly_chart = px.pie(data, values='Value', names='Category', title='My Pie Chart')
    
        # Display Pie Chart
        
        st.plotly_chart(plotly_chart)
        """)
else:
    # Display Matplotlib Chart
    st.pyplot(matplotlib_chart)
    # Display Matplotlib Code
    with st.expander("Code Matplotlib"):
        st.code("""
        # import necessary libraries
        
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
    
        # Display Pie Chart
        
        st.pyplot(matplotlib_chart)
        """)
