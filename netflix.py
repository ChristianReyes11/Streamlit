import streamlit as st
import pandas as pd
import codecs

st.title('NETFLIX BY Christian Reyes')


@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    def lowercase(x): return str(x).lower()
    return data


data_load_state = st.text('Loading..')
data = load_data(500)
data_load_state.text('DONE')

st.dataframe(data)
