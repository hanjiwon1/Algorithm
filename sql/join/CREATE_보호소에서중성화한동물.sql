drop table animal_ins;
DROP TABLE animal_outs;

CREATE TABLE animal_ins(
  animal_id varchar(20) NOT null,
  animal_type varchar(20) not null,
  datetime datetime not null,
  intake_condition varchar(20) not null,
  name varchar(20),
  sex_upon_intake varchar(20) not null);


CREATE TABLE animal_outs(
  animal_id varchar(20) not null,
  animal_type varchar(20) NOT null,
  datetime datetime not null,
  name varchar(20),
  sex_upon_outcome varchar(20) not null);
  
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A367438', 'Dog', '2015-09-10 16:01:00', 'Normal', 'Cookie', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A382192', 'Dog', '2015-03-13 13:14:00', 'Normal', 'Maxwell 2	', 'Intact Male');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A405494', 'Dog', '2014-05-16 14:17:00', 'Normal', 'Kaila', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A410330', 'Dog', '2016-09-11 14:09:00', 'Sick', 'Chewy', 'Intact Female');

insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A367438', 'Dog', '2015-09-12 13:30:00', 'Cookie', 'Spayed Female');
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A382192', 'Dog', '2015-03-16 13:46:00', 'Maxwell 2', 'Neutered Male');
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A405494', 'Dog', '2014-05-20 11:44:00', 'Kaila', 'Spayed Female');
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A410330', 'Dog', '2016-09-13 13:46:00', 'Chewy', 'Spayed Female');