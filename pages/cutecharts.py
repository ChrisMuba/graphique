
import streamlit as st
from cutecharts.charts import Bar
from cutecharts.components import Page
from cutecharts.faker import Faker

def bar_chart():
    chart = Bar("My Cute Bar Chart")
    chart.set_options(labels=Faker.choose(), x_label="X", y_label="Y")
    chart.add_series("series-A", Faker.values())
    return chart


st.title("Cutecharts Bar Chart with Streamlit")
st.write(bar_chart().render_notebook())
