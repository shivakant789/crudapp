Presented By-Shiva kant Sharma

################################

The Application is created using Django and Backend as Postgresql.
Assumpations
1.To create a Employee Entry,Employee can register himself by Giving his Emp Id,Name,Email,salary,Gender,Occupation.
2.We can edit Employee data instead Employee ID.
3.We can Delete  Employee data.
4.We can order the data with Name,Salary.
5.We can search the Employee on basis of gender and Occupation.

#################################

Approach to the Solution
1.I have used Django and Postgresql for this solution.
2.For Searching and Sorting postgresql queries are used.
3.I have used Django views.py,Templates to show my result.
4.Table is created with name Employee with database name postgres.
5Table contains columns such Id as primary key,Name,Email,Salary,Gender,Occupation.

table Creation Query:

create table employee
(
id serialkey primary key,
empname varchar(150),
email varchar(150),
occcupation varchar(150),
empsal int,
gender char,
address varchar(150)
);


Insert
INSERT INTO TABLE_NAME (id,empname,email,occupation,empsal,gender,address)
VALUES (value1, value2, value3,..val7);

Searching 
select * from employee where gender=%s and occupation=%s',[gender,occupation]

Sorting by name
select * from employee order by empname
 
Delete
delete from employee where id= 2;


#############################

Steps to run Application
1.Install django
pip install Django
2.create project
Django-admin startproject crudapp
Run Project
3.cd prj_name then python manage.py runserver
5copy paste contents inside crudapp which is present  with manage.py file. 
4The front page index.html contains entry for a new Employee(move to Insert.html).
5Index.html also contains functionality like Edit the Employee,Delete the Employee.
6.You can search the Employee on basis of Gender and Department
7.you can prioritize the given table By name,By Salary Or again back to the initial state by using Refresh button.
8.In the Edit page you can change the values of Employee.But you cannot change Employee Id.
