
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

   # Plotly
import plotly.express as px

# Create a sample dataframe
data = {
  'Category': ['A', 'B', 'C', 'D'],
  'Value': [10, 15, 7, 10]
}

# Create a pie chart
fig = px.pie(data, values='Value', names='Category', title='My Pie Chart')

# Bokeh
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
from bokeh.models import ColumnDataSource
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
  'Category': ['A', 'B', 'C', 'D', 'E'],
  'Value': [10, 15, 7, 10, 8]
})

data['angle'] = data['Value']/data['Value'].sum() * 2*pi
data['color'] = Category20c[len(data)]

p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@Category: @Value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Category', source=data)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None





# Onglets "Altair", "Plotly" & "Bokeh"
tab1, tab2, tab3 = st.tabs(["Altair", "Plotly", "Bokeh"])

with tab1:
   #Display Vega-Altair Chart
   st.altair_chart(chart) 
   #Display Plotly Chart
with tab2:
   st.plotly_chart(fig)

with tab3:
   st.bokeh_chart(p)
   
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
    
    fig = px.pie(data, values='Value', names='Category', title='My Pie Chart')

    :blue[*Display Pie Chart*]
    
    st.plotly_chart(fig)
    """)
   











