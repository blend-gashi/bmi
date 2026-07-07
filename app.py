import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

# Konfigurim i faqes
st.set_page_config(
    page_title="BMI Calc - Kalkulatori per llogaritjen e peshes ideale",
    page_icon="🎯",
)

# Lidhja me MongoDB
uri = st.secrets["mongodb_srv"]
client =  MongoClient(uri)
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Dizajnimi i faqes
st.title("BMI Calc")
st.title("Body Mass Index - Kalkulatori për llogaritjen e peshës ideale")

# Show an image


# Ruajtja e te dhenave ne databaze
db = client["bmi_users"]
collection = db["users"]



# Columns
col1, col2 = st.columns(2)

with col1:
    with st.echo("below"):
        value = streamlit_image_coordinates(
            "bg.jpeg",
            width=250,
            key="local2",
        )

        st.write(value)

with col2:
    # Te dhenat per perdoruesin
    emri = st.text_input("Emri")
    mbiemri = st.text_input("Mbiemri")
    mosha = st.number_input("Mosha")

    # Gjinia
    gjinia = st.selectbox('Gjinia', ['Mashkull', 'Femër'])

    # Pesha
    pesha = st.slider('Select a value (kg):', 40, 120, value=80)

    # Gjatesia
    gjatesia = st.slider('Sheno gjatesine (cm):', 120, 220, value=180)

    # Data
    # Date range input
    start_date = datetime.date(2026, 7, 8)
    date_range = st.date_input("Dita kur jeni peshuar per here te fundit", (start_date))
    st.write(f"Start date: {date_range}")



    if st.button('Click Me'):
        st.write("Button clicked!")
