# import library
import streamlit as st
import cutecharts.charts as ctc

# import data
df=pd.DataFrame({
  x:["Sun.","Mon.","Tue.","Wed.","Thu.","Fri.","Sat."],
  y:[14, 15, 17, 20, 22.3, 23.7, 24.8],
  z:[16, 16.4, 23.6, 24.5, 19.9, 13.6, 13.4]})

# Bar Chart
chart = ctc.Bar("Toronto Temperature",width=’500px’,height=’400px’)
chart.set_options(
 labels=list(df[‘x’]),
 x_label='Days',
 y_label='Temperature (Celsius)' ,
 colors=[‘#1EAFAE’ for i in range(len(df))]
 )
chart.add_series('This week',list(df[‘y’]))
chart.render_notebook()
