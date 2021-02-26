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
  
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A354597', 'Cat', '2014-05-02 12:16:00', 'Normal', 'Ariel', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A373687', 'Dog', '2014-03-20 12:31:00', 'Normal', 'Rosie', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A412697', 'Dog', '2016-01-03 16:25:00', 'Normal', 'Jackie', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A413789', 'Dog', '2016-04-19 13:28:00', 'Normal', 'Benji', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake) VALUES ('A414198', 'Dog', '2015-01-29 15:01:00', 'Normal', 'Shelly', 'Spayed Female');
insert into animal_ins(animal_id, animal_type, datetime, intake_condition,  sex_upon_intake) VALUES ('A368930', 'Dog', '2014-06-08 13:20:00', 'Normal', 'Neutered Male');

insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A354597', 'Cat', '2014-05-02 12:16:00', 'Ariel', 'Spayed Female');
insert into animal_outs(animal_id, animal_type, datetime, name, sex_upon_outcome) values ('A373687', 'Dog', '2014-03-20 12:31:00', 'Rosie', 'Spayed Female');
insert into animal_outs(animal_id, animal_type, datetime, sex_upon_outcome) values ('A368930', 'Dog', '2014-06-13 15:52:00', 'Spayed Female');

