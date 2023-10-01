
import streamlit as st
from cutecharts.charts import Line

def line_chart():
    chart = Line("Line Chart")
    chart.set_options(
        labels=["A", "B", "C", "D", "E", "F", "G"], 
        x_label="I'm xlabel", 
        y_label="I'm ylabel",
    )
    chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
    chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])
    return chart

def main():
    st.title("Cutecharts Line Chart with Streamlit")
    st.write(line_chart().render_notebook())

if __name__ == "__main__":
    main()
