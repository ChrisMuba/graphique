
import streamlit as st

# Vega-Altair
import streamlit as st
import altair as alt
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8],
  'Color': ['red', 'blue', 'green', 'orange', 'purple']
})

# Create a horizontal bar chart with custom colors
altair_chart = alt.Chart(data).mark_bar().encode(
    x='Value',
    y='Category',
    color='Color'
).properties(
    width=400,
    height=400,
    title='My Horizontal Bar Chart'
)



# Plotly
import streamlit as st
import plotly.graph_objects as go

# Create a sample dataframe
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



# Matplotlib
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataframe
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
   st.pyplot(plt)
   
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

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


import streamlit as st
import matplotlib.pyplot as plt

# Create a sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]

# Create a line plot
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Line Plot')

# Display the code and plot within an expander
with st.expander("Code and Plot"):
    # Display the code
    code = '''
import matplotlib.pyplot as plt

# Create a sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]

# Create a line plot
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Line Plot')

# Display the plot
plt.show()
'''
    st.code(code, language='python')

    # Display the plot
    st.pyplot(plt)

   











