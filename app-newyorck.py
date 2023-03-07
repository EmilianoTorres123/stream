import streamlit as st
import pandas as pd
import numpy as np

sidebar=st.sidebar

st.title('Paseos en bicleta en nueva york')
st.title('Nombre: Aarron Emiliano Torres')
st.title('Correo: zS20006726@estudiantes.uv.mx')
#--- LOGO ---#
st.sidebar.image("logo.jpg")
st.sidebar.markdown("##")


DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Ciclo de carga datos en nueva york...')
data = load_data(500)
data_load_state.text("Hecho! (using st.cache)")

if st.sidebar.checkbox('Mostrar datos sin procesar'):
    st.subheader('Raw data')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


# Some number in the range 0-23
hour_to_filter = sidebar.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('mapa de todas las recogidas %s:00' % hour_to_filter)
st.map(filtered_data)
