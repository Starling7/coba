import streamlit as st
from sqlalchemy import text

list_tribune = ['', 'Economy', 'Regular', 'VIP', 'VVIP']
list_gender = ['', 'male', 'female']
list_match= ['', 'Indonesia vs Argentina', 'Indonesia vs Thailand', 'Indonesia vs Malaysia']
list_stadium = ['', 'Jakarta International Stadium', 'Jatidiri Stadium', 'Maguwoharjo Stadium']
list_price = ['', '150000', '250000', '350000', '500000']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://radityacr740:o8KrhDcWj4wN@ep-super-smoke-81752083.us-east-2.aws.neon.tech/fpmbddb")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS TICKETS (id serial, tribune_name varchar, supporter_name varchar, gender char(25), \
                                                       stadium_name varchar, ticket_price varchar, match_name varchar, date_info date);')
    session.execute(query)

st.header('FOOTBALL TICKETS DATABASES')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM tickets ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO tickets (tribune_name, supporter_name, gender, stadium_name, ticket_price, match_name, date_info) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':None})
            session.commit()

    data = conn.query('SELECT * FROM tickets ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        tribune_name_lama = result["tribune_name"]
        supporter_name_lama = result["supporter_name"]
        gender_lama = result["gender"]
        stadium_name_lama = result["stadium_name"]
        ticket_price_lama = result["ticket_price"]
        match_name_lama = result["match_name"]
        date_info_lama = result["date_info"]

        with st.expander(f'a.n. {supporter_name_lama}'):
            with st.form(f'data-{id}'):
                tribune_name_baru = st.selectbox("tribune_name", list_tribune, list_tribune.index(tribune_name_lama))
                supporter_name_baru = st.text_input("supporter_name", supporter_name_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                stadium_name_baru = st.selectbox("stadium_name", list_stadium, list_stadium.index(stadium_name_lama))
                ticket_price_baru = st.selectbox("ticket_price", list_price, list_price.index(ticket_price_lama))
                match_name_baru = st.selectbox("match_name", list_match, list_match.index(match_name_lama))
                date_info_baru = st.date_input("date_info", date_info_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE tickets \
                                          SET tribune_name=:1, supporter_name=:2, gender=:3, stadium_name=:4, \
                                          ticket_price=:5, match_name=:6, date_info=:7 \
                                          WHERE id=:8;')
                            session.execute(query, {'1':tribune_name_baru, '2':supporter_name_baru, '3':gender_baru, '4':str(stadium_name_baru), 
                                                    '5':ticket_price_baru, '6':match_name_baru, '7':date_info_baru, '8':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM tickets WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
