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
  
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A350276', 'Cat', '2014-05-02 12:16:00', 'Normal', 'Jewel', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A381217', 'Dog', '2017-07-08 09:41:00', 'Sick', 'Cherokee', 'Neutered Male');

insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A350276', 'Cat', '2018-01-28 17:51:00', 'Jewel', 'Spayed Female');
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A381217', 'Dog', '2017-06-09 18:51:00', 'Cherokee', 'Neutered Male');