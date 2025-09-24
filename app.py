#import webbrowser
import urllib.parse
import pandas as pd
import streamlit as st

def getGraph(df):
    edges=""
    for _,row in df.iterrows():
       if not pd.isna(row.iloc[3]):
          edges +=f'\t"{row.iloc[0]}" -> "{row.iloc[3]}";\n'
    return f'digraph {{\n{edges}}}'

st.title("hierachical data viewer")

df=pd.read_csv('data/employee.csv',header=0).convert_dtypes()
#st.dataframe(df)
#print(df)
tabs=st.tabs(["Source","Graph","dot code"])

tabs[0].dataframe(df)
chart=getGraph(df)
tabs[1].graphviz_chart(chart,use_container_width=True)
#print(d)
url=f'http://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(chart)}'
tabs[2].link_button("visualize online",url)
#webbrowser.open(url)
tabs[2].code(chart)