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


alter table memberTbl add column rg_date DATETIME DEFAULT CURRENT_TIMESTAMP;

insert into memberTbl(memberId, memberName, memberAddress) values("1","당탕이", "경기 부천시 중동");

insert into memberTbl(memberId, memberName, memberAddress) values("2","김동윤", "경기 광주시");

insert into memberTbl(memberId, memberName, memberAddress) values("3","김철수", "전남 광주시");

insert into memberTbl(memberId, memberName, memberAddress) values("4","훈이", "서울시");

select * from memberTbl;

CREATE TABLE buyTbl (
  buyTblId INT AUTO_INCREMENT PRIMARY KEY,
  memberId VARCHAR(3) NOT NULL,
  prodName VARCHAR(3) NOT NULL,
  price INT NOT NULL,
  amount INT NOT NULL,
  FOREIGN KEY (memberId) REFERENCES memberTbl(memberId)
);




