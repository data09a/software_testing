-- create table salary (
--  sid int(10) primary key,
--  empid int(10) not null,
--  salary int(10) not null -- salary
-- );
-- insert into salary values ('1', '7', '2100');
-- insert into salary values ('2', '6', '2000');
-- insert into salary values ('3', '12', '5000');
-- insert into salary values ('4', '9', '1999');
-- insert into salary values ('5', '10', '1900');
-- insert into salary values ('6', '1', '3000');
-- insert into salary values ('7', '2', '5500');
-- insert into salary values ('8', '5', '2000');
-- insert into salary values ('9', '3', '1500');
-- insert into salary values ('10', '8', '4000');
-- insert into salary values ('11', '11', '2600');
-- insert into salary values ('12', '4', '5300');
-- select * from salary;
-- -- 
-- drop table if exists courses;
-- create table courses (
--  courseNo int(10) unsigned primary key auto_increment,
--  name varchar(255)
-- );
-- insert into courses values
-- ('1', 'database'),
-- ('2', 'qtp'),
-- ('3', 'linux'),
-- ('4', 'system test'),
-- ('5', 'unit test'),
-- ('6', 'testing process');
-- select * from courses
-- 
-- 
-- drop table if exists scores;
-- create table scores (
-- 
--  id int(10) unsigned primary key auto_increment,
--  courseNo int(10),
--  studentNo varchar(10),
--  score tinyint(4)
-- );
-- 
-- insert into scores values
-- ('1', '1', '001', '90'),
-- ('2', '1', '002', '75'),
-- ('3', '2', '002', '98'),
-- ('4', '3', '001', '86'),
-- ('5', '3', '003', '80'),
-- ('6', '4', '004', '79'),
-- ('7', '5', '005', '96'),
-- ('8', '6', '006', '80');
-- 
-- select * from scores
-- 
-- select * from students

## 1. inner join

-- inner join scores on students.studentno = scores.studentno;

-- select * from students, scores where students.studentNo = scores.studentNo;

-- select * from  scores
-- inner join courses on scores.courseno = courses.courseno;

-- select * from students as stu
-- inner join scores as sc on stu.studentno = sc.studentno
-- inner join courses as cou on sc.courseno = cou.courseno;
-- 
-- 
-- select stu.name, cou.name as CourseName, sc.score from students as stu
-- inner join scores as sc on stu.studentno = sc.studentno
-- inner join courses as cou on sc.courseno = cou.courseno
-- where stu.name = 'Jack';
-- -- 
-- select
--  stu.name,
--  cs.name,
--  sc.score
-- from
--  students stu
-- inner join scores sc on stu.studentNo = sc.studentNo
-- inner join courses cs on sc.courseNo = cs.courseNo
-- where
--  stu.name = 'Jack'and cs.name = 'database';
-- 
-- select
-- 	stu.name,
-- 	cs.name,
-- 	sc.score
-- from  
-- 	students stu
-- inner join scores sc on stu.studentNo = sc.studentNo
-- inner join courses cs on sc.courseNo = cs.courseNo
-- where 
-- 	cs.name = 'database'

 ## look up the highest score in the male, show name, coursename, scores
-- 
-- select 
-- 	stu.name,
-- 	cs.name,
-- 	sc.score
-- from 
-- 	students stu
-- inner join scores sc on stu.studentNo = sc.studentNo
-- inner join courses cs on sc.courseNo = cs.courseNo
-- where 
-- 	stu.sex ='M'
-- order by
-- 	sc.score desc 
-- limit 1


## 2. left join 
-- 
-- select * from  students stu 
-- left join scores sc on stu.studentNo = sc.studentNo;

-- select * from  students stu 
-- left join scores sc on stu.studentNo = sc.studentNo
-- left join courses cs on cs.courseNo = sc.courseNo;

-- select * from scores sc
-- right join students stu on stu.studentNo = sc.studentNo;
-- 
-- select * from scores sc
-- right join students stu on stu.studentNo = sc.studentNo
-- left join courses cs on cs.courseNo = sc.courseNo
