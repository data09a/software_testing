-- drop table if exists students;
-- create table students (
--   studentNo varchar(10) primary key,
--   name varchar(10),
--   sex varchar(1),
--   hometown varchar(20),
--   age tinyint(4),
--   class varchar(10),
--   card varchar(20)
-- )


-- insert into students values
-- ('001', 'Amy', 'F', 'NYC', '20', '1', '340322199001247654'),
-- ('002', 'Jack', 'M', 'NJ', '18', '2', '340322199002242354'),
-- ('003', 'John', 'M', 'MA', '24', '3', '340322199003247654'),
-- ('004', 'Bill', 'M', 'ME', '22', '4', '340322199005247654'),
-- ('005', 'Julia', 'F', 'NYC', '19', '3', '340322199004247654'),
-- ('006', 'Amanda', 'F', 'SC', '18', '1', '340322199006247654'),
-- ('007', 'Andrew', 'M', 'PA', '20', '2', '340322199007247654'),
-- ('008', 'Linda', 'F', 'FL', '15', '3', null),
-- ('009', 'Simon', 'M', 'CA', '21', '1', ''),
-- ('010', 'Emily', 'F', 'TX', '26', '2', '340322199607247654'),
-- ('011', 'Bob', 'M', 'NJ', '30', '4', '340322199005267754'),
-- ('012', 'Robert', 'M', 'MA', '26', '3', '340322199000297655')
-- 

## 1. select all or partial

-- select * from students;

-- select name,sex,age from students;

## 2. gave nickname

-- select s.name,s.sex,s.age from students as s;

-- select name as NAME, sex as SEX, age as AGE from students;

## 3. distinct

-- select distinct sex from students;

## 4. condition

-- select * from students where studentNo = 001;

-- select age from students where name ='Jack';

-- select * from students where age <20;

-- select * from students where hometown != 'NYC'

-- select card from  students where studentNo = 007;

-- select * from students where class != 1;

-- select name, sex from students where age > 20;

-- select * from students where age < 20 and sex = 'F';

-- select * from students where sex = 'F' or class = '1';

-- select * from students where not hometown = 'MA'

-- select * from students where hometown = 'NJ' or hometown = 'PA';

-- select * from students where class = 1 and hometown = 'CA';

-- select * from students where age != 20;

-- select * from  students where  name like 'J%';

-- select * from  students where  name like '%a%';
-- 
-- select * from  students where  name like '%a';

-- select * from  students where  name like 'Bo_';

-- select * from  students where studentNo like '%1';
-- 
-- select * from  students where name like 'J%' and age >= 20;

-- select * from  students where  hometown in ('NYC', 'NJ', 'MA');

-- select * from students where age between 18 and 20;

-- select * from students where age between 18 and 22 and sex = 'F';
-- select * from students where age not between 20 and 25;

-- select * from students where card is null;

-- select * from students where card is not null;

## 5. list in order

-- select * from students order by age;
-- select * from students order by age desc, studentNo;
-- select *  from students order by class, studentNo;

## 6. function

-- select count(*) from students;
-- select max(age) from students where sex = 'F';
-- select min(age) from students;
-- select sum(age) from students where hometown = 'NYC';
-- select avg(age) from students where sex = 'F';

-- select count(*) from students where class = '3' and age <18;
-- 
-- select max(age), min(age), avg(age) from students;
-- 
-- select count(*) from  students where class = '1';
-- -- -- 
## 7. group
--  select sex,count(*) from students group by sex

-- select class,sex,count(*) from students group by class,sex;
-- 
-- select class, avg(age), max(age), min(age) from students group by class;
-- 
-- select sex,count(*) from students group by sex having sex='M';

-- select class, avg(age), max(age), min(age) from students group by class having class != '1';

## 8. select partical row

--  select * from students limit 0,3;
   # get line 4 to line 6
--  select * from students limit 3,3;

## 9. page

-- select * from students limit 5,5;

-- select * from students limit 10,5;
-- 
