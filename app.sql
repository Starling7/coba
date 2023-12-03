drop table if exists ticket;
create table ticket (
	id serial,
	class_name text,
	customer_name text,
	gender text,
	stadium_name text,
	ticket_price text,
	match_name text,
	time_info time,
	date_info date
);

insert into ticket (class_name, customer_name, gender, stadium_name, ticket_price, match_name, time_info, date_info) 
values
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03')
	;
