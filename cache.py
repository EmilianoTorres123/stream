import pandas as pd
import streamlit as st
import codecs
name_link =codec.open('https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/movies.csv','ru','latin1')

st.title('Streamlit con cache')

@st.cache
def load_data(nrows):
    data = pd.read_csv(name_link, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state = st.text('cargando')
data = load_data(1000)
data_load_state.text('hecho!! (using st.cache)')

st.dataframe(data)
