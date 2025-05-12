CREATE TABLE tablename (
column_name1 INT,
column_name2 VARCHAR(15),
column_name3 INT );


create table emp(
	empId INT,
	name varchar(15),
	phone INT
);


select *
from emp;

insert into emp values(1,"홍길동",01012341234);

insert into emp values(2,"고길동",01054325432);

delete from emp where empId =2;

update emp set name = "김희동" where empId= 1;

drop table emp;

create table memberTbl(
	memberId varchar(20),
	memberName varchar(40),
	memberAddress varchar(200)
);

insert into memberTbl values("Dang","당탕이", "경기 부천시 중동");

select * from memberTbl;

alter table memberTbl add column rg_date DATETIME DEFAULT CURRENT_TIMESTAMP;

CREATE TABLE userTBL (
  userName VARCHAR(3) NOT NULL PRIMARY KEY,
  birthYear INT NOT NULL,
  addr VARCHAR(2) NOT NULL,
  mobile VARCHAR(12)
);

CREATE TABLE buyTBL (
  userName VARCHAR(3) NOT NULL,
  prodName VARCHAR(3) NOT NULL,
  price INT NOT NULL,
  amount INT NOT NULL,
  FOREIGN KEY (userName) REFERENCES userTBL(userName)
);



