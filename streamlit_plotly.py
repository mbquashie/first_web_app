import streamlit as st
import seaborn as sns
import pandas as pd

from sklearn.datasets import load_iris

import plotly.express as px
iris= load_iris()
 
labels =iris.feature_names
targets=iris.target

df=pd.DataFrame(iris.data, columns=labels)

df["targets"]=targets

st.write("""How sepal width, sepal length, petal width and petal lenth relate to species of plants using the Iris Dataset""")

fig1=px.scatter_3d(df, x='petal width (cm)', y='petal length (cm)', z='sepal length (cm)',color='sepal width (cm)', symbol='targets')


st.plotly_chart(fig1, use_container_width=True)

