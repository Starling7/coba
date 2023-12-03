drop table if exists logistics;
create table logistics (
	id serial,
	product_nama text,
	ekspedisi_nama text,
	ongkir text,
	kota_tujuan text,
	handphone text,
	nomor_resi text,
	tanggal_dikirim date,
	tanggal_sampai date
);

insert into logistics (product_nama, ekspedisi_nama, ongkir, kota_tujuan, handphone, nomor_resi, tanggal_dikirim, tanggal_sampai) 
values
	('Sepatu', 'JNT', 'FREE', 'SEMARANG', 62838, 'A009', '2023-10-01', '2023-10-11'),
	('Sepatu', 'JNT', 'FREE', 'SEMARANG', 62838, 'A009', '2023-10-01', '2023-10-11'),
	('Sepatu', 'JNT', 'FREE', 'SEMARANG', 62838, 'A009', '2023-10-01', '2023-10-11'),
	('Sepatu', 'JNT', 'FREE', 'SEMARANG', 62838, 'A009', '2023-10-01', '2023-10-11')
	;