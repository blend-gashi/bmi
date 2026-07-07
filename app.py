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
#st.title("BMI Calc")
st.title(":orange[:material/checklist:] BMI Calc")
st.title("Body Mass Index - Kalkulatori për llogaritjen e peshës ideale")

# Ruajtja e te dhenave ne databaze
db = client["bmi_users"]
collection = db["users"]

# Columns
col1, col2 = st.columns(2)
with col1:
    streamlit_image_coordinates(
        "https://cdn-icons-png.flaticon.com/256/10476/10476467.png",
        width=250,
        height=250,    
    )
    st.header(':dizzy: Si ta përdorim')
    st.write("Plotëso të dhënat në formular dhe pastaj kliko butoni dhe të paraqitet rezultati.")
    st.write('Te dhenat ruhen ne Mongodb dhe aplikacioni është deployed me streamlit.')

with col2:
    # Te dhenat per perdoruesin
    emri = st.text_input(":raising_hand_man: Emri")
    mosha = st.text_input(":hatching_chick: Mosha")

    # Gjinia
    gjinia = st.selectbox(':couple: Gjinia', [' Mashkull', 'Femër'])

    # Pesha
    pesha = st.slider('Select a value (kg):', 40, 120, value=80)

    # Gjatesia
    gjatesia = st.slider('Sheno gjatesine (cm):', 120, 220, value=180)

    # Data
    # Date range input
    start_date = datetime.date(2026, 7, 8)
    date = st.date_input("Dita/Data", (start_date))

    bmi = pesha / ((gjatesia/100)**2)

    if st.button('Llogarit dhe ruaj'):
        st.write(f'Emri: {emri}.')
        st.write(f'Pesha: {pesha}.')
        st.write(f'Gjatesia:{gjatesia}')
        st.title(f":muscle:BMI: {round(bmi,2)}")
        collection.insert_one({
            "emri": emri,
            "mosha": mosha,
            "gjinia":gjinia,
            "pesha":pesha,
            "gjatesia":gjatesia,
            "bmi":bmi,
            "data":str(date)
        })
