
import streamlit as st
import pandas as pd
from roughviz.charts import Pie

df = pd.DataFrame({"a": ["a", "b"], "b": [1, 2], "c": [2, 3]})

# Pie Chart
pie = Pie(data=df, labels="a", values="b")
