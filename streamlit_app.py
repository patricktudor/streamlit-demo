import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World!")

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")

st.header("This is a header with a divider", divider='rainbow')

st.markdown("This is created using st.markdown.")

col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value", 1, 50)
with col2:
    st.write("The value of :red[***x***] is", x)

st.header("Charts", divider='rainbow')

chart_data = pd.DataFrame(np.random.randn(x, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
