
import streamlit as st
import roughviz

# Bar Chart
import pandas as pd 
d = {'Year': ['1980', '1981', '1982'], 'A': [3, 4, 10]}
df = pd.DataFrame(data=d)
roughviz.bar(df["Year"], df["A"], axisRoughness = 0.7, axisStrokeWidth = 0.7, roughness=2.3, highlight="gray")

