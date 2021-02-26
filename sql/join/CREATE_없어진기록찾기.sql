DROP TABLE animal_ins;
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

  
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) values ('A352713', 'Cat', '2017-04-13 16:29:00', 'Normal', 'Gia', 'Spayed female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) values ('A350375', 'cat', '2017-03-06 15:01:00	', 'Normal', 'Meo', 'Neutered Male');

insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A349733', 'Dog', '2017-09-27 19:09:00', 'Allie', 'Spayed female');
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A352713', 'Cat', '2017-04-25 12:25:00', 'Gia', 'Spayed female'); 
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A349990', 'Cat', '2018-02-02 14:18:00', 'Spice', 'Spayed female');