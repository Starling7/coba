drop table if exists schedule;
create table schedule (
	id serial,
	train_name text,
	passenger_name text,
	gender text,
	departure_station text,
	ticket_price text,
	arrival_station text,
	departure_time time,
	departure_date date
);

insert into schedule (train_name, passenger_name, gender, departure_station, ticket_price, arrival_station, departure_time, departure_date) 
values
	('Argo Semeru (17)', 'Juan', 'male', 'Gubeng (SGU)', 630000, 'Malang (ML)', '09:00', '2023-10-01'),
	('Bima (23)', 'Eafa', 'female', 'Gambir (GMR)', 290000, 'Gubeng (SGU)', '10:00', '2022-11-02'),
	('Pandagulang (77F)', 'Alea', 'female', 'Pasarsenen (PSE)', 340000, 'Kertosono (KTN)', '10:00', '2022-03-03'),
	('Sancaka (22CA)', 'Abyan', 'male', 'Gubeng (SGU)', 330000, 'Nganjuk (NJ)', '11:00', '2022-10-04'),
	('Jayakarta (217)', 'Eisa', 'male', 'Mojokerto (MR)', 750000, 'Yogyakarta (YK)', '23:00', '2022-10-05'),
	('Bima (23)', 'Maya', 'female', 'Madiun (MN)', 280000, 'Kertosono (KTN)', '08:00', '2022-08-18'),
	('Jayakarta (217)', 'Aisha', 'female', 'Gubeng (SGU)', 320000, 'Malang (ML)', '20:30', '2022-07-07'),
	('Argo Semeru (17)', 'Nicolas', 'male', 'Pasarsenen (PSE)', 550000, 'Nganjuk (NJ)', '22:00', '2022-05-08'),
	('Sancaka (22CA)', 'Fatima', 'female', 'Yogyakarta (YK)', 450000, 'Gubeng (SGU)', '11:30', '2022-10-09'),
	('Jayakarta (217)', 'Louis', 'male', 'Madiun (MN)', 625000, 'Gubeng (SGU)', '12:40', '2022-10-11')
	;
