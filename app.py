import streamlit as st
from sqlalchemy import text

list_train = ['', 'Argo Semeru (17)', 'Bima (23)', 'Pandagulang (77F)', 'Sancaka (22CA)', 'Jayakarta (217)']
list_gender = ['', 'male', 'female']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://radityacr740:o8KrhDcWj4wN@ep-super-smoke-81752083.us-east-2.aws.neon.tech/fpmbddb")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SCHEDULE (id serial, train_name varchar, passenger_name varchar, gender char(25), \
                                                       departure_station varchar, ticket_price varchar, arrival_station text, departure_date date);')
    session.execute(query)

st.header('DATABASE PASSENGER KAI')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO schedule (train_name, passenger_name, gender, departure_station, ticket_price, arrival_station, departure_time, departure_date) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':None, '8':None})
            session.commit()

    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        train_name_lama = result["train_name"]
        passenger_name_lama = result["passenger_name"]
        gender_lama = result["gender"]
        departure_station_lama = result["departure_station"]
        ticket_price_lama = result["ticket_price"]
        arrival_station_lama = result["arrival_station"]
        departure_time_lama = result["departure_time"]
        departure_date_lama = result["departure_date"]

        with st.expander(f'a.n. {passenger_name_lama}'):
            with st.form(f'data-{id}'):
                train_name_baru = st.selectbox("train_name", list_train, list_train.index(train_name_lama))
                passenger_name_baru = st.text_input("passenger_name", passenger_name_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                departure_station_baru = st.text_input("departure_station", departure_station_lama)
                ticket_price_baru = st.text_input("ticket_price", ticket_price_lama)
                arrival_station_baru = st.text_input("arrival_station", arrival_station_lama)
                departure_time_baru = st.time_input("departure_time", departure_time_lama)
                departure_date_baru = st.date_input("departure_date", departure_date_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE schedule \
                                          SET train_name=:1, passenger_name=:2, gender=:3, departure_station=:4, \
                                          ticket_price=:5, arrival_station=:6, departure_time=:7, departure_date=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':train_name_baru, '2':passenger_name_baru, '3':gender_baru, '4':str(departure_station_baru), 
                                                    '5':ticket_price_baru, '6':arrival_station_baru, '7':departure_time_baru, '8':departure_date_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
