-- sql --- stands for structured query language 

-- invented by ibm in 1970

-- 1974 accepted for the rdms

-- invented by raymond boyee and donald chamberlin 

-- it is used to manage and manipulate data both data base sql are interconnecged each other



-- order of excecution:  
-- from - where - group by - having - select - order by - limit - offset 

-- this is excecution of the query 



-- features of sql 

-- popular demand techonolgy 
-- manages and retrives the data from datasets 

-- efficency for handling  high volume data 







-- unstructure data : data doesnot have predefined data models or  structure 
-- it lacks for formal and organisezed frame work  it is more challenging for traditional data base to handle 
-- images , mails, photos 


-- -- structured data : the data is organisezed and formatted in the way that us easily readable by humans and machines 
-- -- it follows a fixed schema or database 
-- tables , csv, excel



-- data base: it is structured collection of data that can be accesees amd managed easily store and retreive the 
-- information efficinetly 





-- traditinal file sysytem :A traditional database is a system used to store and manage structured data in tables.

-- characterstics of traditinal file system 


-- horitoanl- rows
-- vertical- columns 


-- data redudancy: it occurs when piece of data stored multiple places with in data base  or across database


-- -- data isolation: the ability of data base system to allow multiple transaction to acces the same data without 
--        interfering each other 



-- data acces: it becomes diffult to  acces important data if multiple users are searching at the same time 



-- ACID

-- A: Atomicity------------Atomicity means a transaction is completed fully or not completed at all.


-- C: consistency--------consistency ensures the database remains correct and valid before and after a transaction.

-- I: isolation-------Isolation ensures multiple transactions do not interfere with each other.


-- D: durability-------Durability ensures committed data is permanently saved even if system crashes.




-- NUT SHELL: IT IS USED To communicate with database system to retrive the information from db 





-- COMMANDS: IN THE SQL THEY ARE 5 COMMANDS

-- DDL DML DCL TCL DQL



-- DDL: data defintion language 
-- it is used create and modify table structure of database

-- create , alter , drop, truncate

-- create: a new table , db


-- Alter: it is used to modify the existing table by adding unique attributes

-- drop: it used drop the table from the data base 


-- truncate: it is used delete the rows in the table 




-- DML: Data manipluation language 
-- it is used manipulate the data the present db it used to maniplute adb and data accesees
--  , insert, update, delete



-- insert : insert the new values in the table 


-- update : it is used to modify existing record in the table 


-- delete: the delete commad used to delete specific row or even all the rows from  tables of syntax 
-- deletes from table name


-- lock command : is used to control acces to data in db especially when multiples users are trying to read or write 
-- data at the same time 






-- DCL: DATA CONTROL LANGUAGE 
--  it is used for mainting the security which gives acces and permisson of db  commands the comes under DCL
-- priviliges----------> permisiion


-- grant: it user  to acees tje data bases


-- revoke: this commad withdraw the user acces priviliges supplied by using the grant command 





-- DQL :Stands For data query language 

-- DQL stands for Data Query Language.

-- select- It is used to retrieve or fetch data from a databas






-- TCL:transaction control language 
--  it is used genrally for manging the databse to maintain consistency
--  a group of tasks combines into single excecution unit using transaction 
--  each transaction start with particular task and it is completd once 


-- commit: it is used to permantly save a tranaction 

-- roll back: it is used to restore the tranaction is not  saved 


-- savepoint :
-- it used to hold the tranaction temporarily can be rolled backed its  previos state at any point 





























-- 5 Important Points: DELETE vs TRUNCATE vs DROP


-- Point	                   DELETE	                TRUNCATE	                     DROP
-- 1. Purpose    	Removes selected rows	         Removes all rows	            Removes entire table

-- 2. WHERE       Clause Supports WHERE	     Does not support WHERE	            Does not support WHERE

-- 3. Table         Structure	Table remains	   Table remains	                    Table deleted

-- 4. Speed	            Slower	                     Faster	                            Fastest

-- 5. Type	             DML Command	               DDL Command	                         DDL Command










-- -- rdbms is relational database managemnt system 
-- --  data stores in table fromat 
-- --  handles large amount of data 
-- --  supoort multiple users ata time 
-- --  security is more rdbms 
-- -- supoort a distributed data base where u can  manage and have the acces fir multiple data base same time 



-- -- dbms : data base managemnet system 
-- -- stores data in xml , json 
-- --  handles less amount of data 
-- --  supoort sigle user only 
-- -- no supoort distrribute data base






-- data models : data models defines how the data is interconnected to each other and how proccesed 
-- and stored each other inside system  also defines logical structes desgin 


-- hierarchial model : it wasthe first model in dbms models ever used in this model daa organisezed in tree
-- like structure connected to  each other  by links 



-- network models :
-- it is represents comples data relationship uisng graph like structure 
-- where data can have many to manty realtionships 



-- entity models :
-- it is mall and well represnted models in apictorial form in the differant shapes 
 
--  pictorial represents  the data that describes how data is communicated and related each other 








-- sql data types: the sql data types specfices  which type of values  is stored in the database 

  


-- numeric data type ------------. int, float, boolean

-- character-----------------------> char, varchar


-- binary------------------------> binary , image

-- data&time---------------------> data , data time, time stamp

--           miscellaneous--------------------> xml, json
--              |
--              | 
--     consistency of various nixture of various things that are not usally connected with each other 





-- numeric data types--holds a intger value  and whokle number and withpout the decimal point 
-- float---stores the decimal point 


-- string data types: it used for character data text

-- char(n)---it is fixed leght of character thaat can cantian number of letters speical charcters 
-- its size can be 0 to 255 charcters


-- varchar: it is similar to char but it stored varible length string size is also more than char data 
-- range to 0 to 60,000



-- data and time :used for storing data and time info 

-- data time: the data time tupe is used for storing the values that can cantian both data s well as the time format 


-- time &stamp:
-- it is also simalr to data and time it can covert current time into various time zones 

-- UTC---universal time coordinated 
-- GMT--- green which time 






-- boolean data type :
-- it is used for true are false values o is consider falase non zero conider true 

-- binary----stores the fixed length of a vaiable 

-- varbinary---stores the varible length of a variable 






-- sql operators: are used to specify certain conditions in an sql statemnet sql operators classfied into 5 

-- Arithmetic Operators
-- +
-- -
-- *
-- /
-- %


-- Comparison Operators
-- =
-- >
-- <
-- >=
-- <=
-- !=
-- <>



-- Logical Operators
-- AND
-- OR
-- NOT
-- Special Operators
-- IN
-- BETWEEN
-- LIKE
-- IS NULL
-- EXISTS






-- -- Normalization:Normalization is a database design technique used to minimize redundancy and maintain
-- --data consistency by organizing data into multiple related tables






-- sql expersiion : is combination of one more values operators and
--  sql function that are same all evaluated to a value 







-- select statment: it is used to retrive the data from the database and it is the most commonly used sql statement
-- select * from customer;

-- select (*): it is used retrive all the columns fromthe table 
-- it is called as wild card charcter 

-- it is know as asterisk



-- select distnict: it is used to retrive the unique values from the data and it is used remove the duplicates from the result set 


-- select where : it is used filter the data based on the specified condition it is used to retrive the specific data from the table 


-- like opertor: it is used to search for a specific pattern in a column 
-- they are two wild card operators ofttenused in conjuction with the like operator 

-- the percent sign % represents zero or more character

-- % k ---> starts with k
-- k % ---> ends with k




-- order by : it is used to sort the result set in either ascending or descending order by default it is sorted in ascending order 
-- select * from customer order by name asc;



-- Rand(): the random statemnet used to display the record present in the table randomly 

-- select * from customer order by rand() limit 5;



-- limit : it is used to specify the number of records to return from the result set 
-- it is often used with order by clause to limit the number of records



-- offset: it is used to specify the number of records to skip before starting to return the records from the result set

-- select * from customer order by name asc limit 5 offset 5;




-- AND operator: all conditons must be true 
-- it is used to filter the data based on multiple conditions and it return the result only whne all  the condtions must b true 

-- or  operator : at least one condition must be true 
-- it is used to filter the data based on multiple conditions and it return the result when at least one of the condition is true



-- Not operator: it is used to negate a condition and it return the result when the condition is false
-- it will give opsite result of the condition 


-- select * from customers 
-- where not country = "usa";


-- In operator : it is used to specify multiple values in  a where clause and it return the result when the value matches any value in the list 
-- select * from customers 
-- where country in ("usa", "canada", "uk");



-- between operator: it is used to filter the data based on a range of values and it return the result when the value is between the specified range
-- select * from customers 
-- where age between 18 and 30;










clauses : it is inbuilt sql class that use certain conditional expersiion 
which helps to acces a particular set of records from the data base 



where clause : it is used to specify a condition reterving the data from table 
it can perform row operation 

it can be used select update delete statment 




order by clause : it used to srot the result records in the database tables 
it can be arranged in either asc and desc 



group by clause : this statemnt is used to group together aby rows of a column with 
same values stored in them 
based on a function specfied in the statement 

split ----->apply------------>combine 
it is mostely used with arggrate function 



having clause : having clause is used to fetch groups pf rows or values which are matched 
with specified condition in group statement 

it can perform a column operation 










































-- Aggregate fucntion: it is a function that used to perform a calculation on a set of values and a return a
-- single value as a result 

-- it maniley used by group by clause and having clause to perform the calculation on the group of data 


-- group by clause spilts the result set into group of values 

-- GROUP BY is a row operation because it groups multiple rows into summary groups based on the values of one or more columns.


-- sum , mean ,max, count, avg


-- sum-->numeric
-- avg--->numeric
-- count-->both
-- min&max---> both 







-- scalar function : it is  a function that operates on single value and return a single value as aresult 

-- performs a single row at a time ans retuns one result per row 

-- scalar function : Lcase,Ucase,Lenght,mid, round

-- Ucase: it is used to conert the string value to upper case 

-- lcase : it is used to convert the string value into lower case 

-- length: it is used to return the number of charcters in astring value 

-- mid: it is used to return a specific number of charcters from a string value starting from a specified position 

-- round: it is used to round a numeric value to specified number of decimal places 


example:
-- select Ucase(name) from customers;
-- select lcase(name) from customers;
-- select length(name) from customers;
-- select mid(name, 1, 3) from customers;
-- select round(price, 2) from products;







  









-- union : the union operator is used to combine the result set of two or more  select statments 

-- every select stament within union must have the same number of columns 
-- Combines the results.
-- Removes duplicate rows.
-- Slightly slower because SQL must check for duplicates.


-- SELECT NAME FROM EMPLOYEES
-- UNION
-- SELECT NAME FROM MANAGERS;



-- union all : it is used to combine the result set of two or more select statments 
-- but  it doesnot allow to remove the duplicates rows from the result set 

-- select city from customers 
-- union all
-- select city from suppliers;
-- order by city 
