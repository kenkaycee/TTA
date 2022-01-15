# SQL Home Learning Tasks 
# 1) Create a relational database (2tables) of your own choice
# Solution 
# Let create database to store information on patients admitted to the hospital

create database bartimore_hospital;

/* Task 2: Create two tables, 
Both tables must have a primary key and the correct datatypes.
 Include a minimum of 5 fields in at least one of the tables
*/

/* Solution:
Create table north_team that contains medical records of patients under the care of North Team 
( a Community Mental Health Team) */
use bartimore_hospital;

create table north_team(
hospital_no char(6) not null,
first_name varchar(30) not null,
last_name varchar(30) not null,
nhs_number int(5) not null,
diagnosis varchar(30) not null,
risk varchar(10) not null,
cluster int(10) not null,
date_referred date not null,
primary key(hospital_no),
unique (nhs_number));

# create a second table demography that contains patient demographical details 
create table demography(
patient_id int(10) not null,
nhs_number int(5) not null,
date_birth date not null,
religion varchar(30) not null,
ethnicity varchar(30) not null,
occupation varchar(30) not null,
primary key (patient_id),
unique (nhs_number)
);

/* Task 3:
View and show both table structures and data to make sure they are setup correctly
*/
# Solution
explain north_team;
explain demography;

/* Task 4:
Enter records into both tables and view them.
Make sure at least one of your tables has 10 records.
*/

# Solution
insert into north_team(hospital_no, first_name, last_name, nhs_number, diagnosis, risk, cluster, 
date_referred)
values ("x12345", "James", "Smith", 100000, "Psychosis", "Low", 7, "2000-07-21"),
("x14536", "Emeka", "Okeke", 100001, "Depression", "High", 12, "2020-07-30"),
("x15553", "Keneddy", "Jason", 100002, "Anxiety", "Medium", 10, "2021-09-20"),
("y16789", "Michael", "Obama", 100003, "Anxiety", "Low", 10, "2022-01-07"),
("x15667", "Vincent", "Amrit", 100004, "Bipolar", "High", 9, "2007-08-14"),
("z67856", "Georgina", "Nuela", 100005, "Alcohol", "Low", 6, "2018-08-20"),
("g78909", "Jasmine", "Williams", 100006, "Schizophrenia", "High", 13, "2019-06-30"),
("d89097", "Rolna", "Lord", 100007, "Insomnia", "Medium", 11, "2016-05-31"),
("t13456", "Ngozi", "Henry", 100008, "PTSD", "High", 9, "2017-06-28"),
("r65789", "Tom", "Fox", 100009, "Anxiety", "Medium", 10, "2018-03-18"),
("v60909", "Rashford", "Percy",100010, "Alcohol", "High", 6, "2016-09-29"),
("f67321", "Martin", "Mayo", 100011, "Schizophrenia", "Medium", 13, "2017-10-11"),
("ju8909", "Angela", "Eze", 100012, "Depression", "High", 12, "2011-11-19"),
("k80896", "Alex", "King", 100013, "Insomnia", "Low", 11, "2022-01-10"),
("i00675", "Austine", "Arteta", 100014, "Bipolar", "High", 14, "2015-02-28"),
("q65789", "Samuel", "Oliver", 100015, "Bipolar", "Medium", 14, "2019-12-18"),
("m89096", "Mikel", "Hahn", 100016, "EUPD", "High", 15, "2021-09-17");
select * from north_team;

insert into demography(patient_id, nhs_number, date_birth, religion, ethnicity, occupation)
values(1, 100016, "1990-09-09", "Atheist", "White-British", "Nurse"),
(2, 100015, "1980-08-18", "Christian", "Black-African", "Engineer"),
(3, 100014, "1983-06-30", "Muslim", "Black-Asian", "Computer Scientist"),
(4, 100001, "2000-04-12", "Muslim", "Black_African", "Data Scientist"),
(5, 100020, "1999-08-02", "Christian", "White-Irish", "Doctor"),
(6, 100022, "1950-01-01", "Hindu", "White-Others", "Radiographer"),
(7, 100011, "1981-05-17", "Atheist", "Black-African", "Plumber");
select * from demography;

# Task 5: Update record 
update demography set nhs_number = 100030
where patient_id = 7;

update north_team set date_referred = "2011-10-11"
where first_name = "Rashford";

# Task 6: Delete a record 
#Solution
# delete patient in the north team that were referred prior to 2015
delete from north_team
where date_referred < "2015-01-01";
select * from north_team;

# Task 7: Join tables 
/*
Solution: Inner Join - returns rows that have matching values in both tables.
For you to join two tables, the tables must have a common column. Both North_teat and demography have 
column nhs_number. This column can be used to perfom various joins 
*/
# select sepcified columns from both tables 
select north_team.first_name, north_team.last_name, north_team.diagnosis, demography.ethnicity
from north_team inner join demography 
on north_team.nhs_number = demography.nhs_number;

# select all columns from both tables 
select * from north_team
inner join demography
on north_team.nhs_number = demography.nhs_number;

# Left (outer) join 
/* Left join : Returns all records from the left table, and the matched records from the right
table*/
select first_name, hospital_no, risk, cluster, date_birth, occupation
from north_team left join demography
on north_team.nhs_number = demography.nhs_number;

# Right (outer) join 
/* Right join : Returns all records from the right table, and the matched records from the left
table*/

select first_name, hospital_no, risk, cluster, date_birth, occupation
from north_team right join demography
on north_team.nhs_number = demography.nhs_number;

/* Task 8:
Run a simple query (one field/column) searching one table*/
# Solution:
select diagnosis from north_team
where risk = "Medium";

/* Task 9:
Run a complex query (more than one field/column) to demonstrate the relations
between the 2 tables*/
/* Soultion:
let's select identified columns from both tables using left join only if the cluster is above 8 and 
risk category is either high or medium: */
 
select first_name, last_name, diagnosis, risk, cluster, date_birth, ethnicity
from north_team left join demography
on north_team.nhs_number = demography.nhs_number
where cluster > 8 and risk = "High" or risk = "Medium";

/* Task 10: 
Retrieve all your data sorted in ascending order on an appropriate field (one table)*/
# Solution : select all columns in north team order by date the patient was referred in ascending order */

select * from north_team 
order by date_referred asc;

/* Task 11:
Filter data using comparison operators (one table) */

# Solution: select all columns in north_team if risk is medium or high 

select * from north_team 
where risk = "Medium" or risk = "High"
order by risk;


