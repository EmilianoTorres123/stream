import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

DATA_URL = "https://firebasestorage.googleapis.com/v0/b/streamlit-emiliano.appspot.com/o/csv%2Fdataset.csv?alt=media&token=2b4a735e-a7df-45e2-951d-45f61019d07d"

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data[ (data['index'] >= startid) & (data['index'] <= endid) ]

    return filtered_data_byrange

startid =  st.text_input('Start index : ')
endid = st.text_input('End index : ')
btnRange = st.button('Search by range' )

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filterbyrange.shape[0] # Gives number of rows
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbyrange)

        

