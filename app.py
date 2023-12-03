import streamlit as st
from sqlalchemy import text

list_product = ['', 'Sepatu', 'Bola', 'Jersey', 'Topi', 'Celana']
list_ongkir = ['', 'FREE', 'FEE']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://radityacr740:o8KrhDcWj4wN@ep-super-smoke-81752083.us-east-2.aws.neon.tech/fpmbddb")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS LOGISTICS (id serial, product_nama varchar, ekspedisi_nama varchar, ongkir text,  kota_tujuan text, handphone varchar, nomor_resi text, tanggal_dikirim date, tanggal_sampai);')
    session.execute(query)

st.header('DATA LOGISTIK PT SIGMA JAYA')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM logistics ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO logistics (product_nama, ekspedisi_nama, ongkir, kota_tujuan, handphone, nomor_resi, tanggal_dikirim, tanggal_sampai) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':None, '9':None})
            session.commit()

    data = conn.query('SELECT * FROM logistics ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        product_nama_lama = result["product_nama"]
        ekspedisi_nama_lama = result["ekspedisi_nama"]
        ongkir_lama = result["ongkir"]
        kota_tujuan_lama = result["kota_tujuan"]
        handphone_lama = result["handphone"]
        nomor_resi_lama = result["nomor_resi"]
        tanggal_dikirim_lama = result["tanggal_dikirim"]
        tanggal_sampai_lama = result["tanggal_sampai"]

        with st.expander(f'a.n. {product_nama_lama}'):
            with st.form(f'data-{id}'):
                product_nama_baru = st.selectbox("product_nama", list_product, list_product.index(product_nama_lama))
                ekspedisi_nama_baru = st.text_input("ekspedisi_nama", ekspedisi_nama_lama)
                ongkir_baru = st.selectbox("ongkir", list_ongkir, list_ongkir.index(ongkir_lama))
                kota_tujuan_baru = st.text_input("kota_tujuan" , kota_tujuan_lama)
                handphone_baru = st.text_input("handphone", handphone_lama)
                nomor_resi_baru = st.text_input("nomor_resi", nomor_resi_lama)
                tanggal_dikirim_baru = st.date_input("tanggal_dikirim", tanggal_dikirim_lama)
                tanggal_sampai_baru = st.date_input("tanggal_sampai", tanggal_sampai_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE logistics \
                                          SET product_nama=:1, ekspedisi_nama=:2, ongkir=:3, kota_tujuan=:4, \
                                          handphone=:5, nomor_resi=:6, tanggal_dikirim=:7, tanggal_sampai=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':product_nama_baru, '2':ekspedisi_nama_baru, '3':ongkir_baru, '4':kota_tujuan_baru, 
                                                    '5':handphone_baru, '6':nomor_resi_baru, '7':tanggal_dikirim_baru, '8':tanggal_sampai_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()