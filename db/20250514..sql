-- GROUP BY
select  memberId, SUM(price) 총금액 FROM buyTbl
GROUP BY memberId;


-- with rollup
select  memberId, SUM(price) 총금액 FROM buyTbl
GROUP BY memberId,prodName with rollup;

create table 


-- 복사

ALTER TABLE itemTBL
ADD COLUMN itemID INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;

create table itemTBL1
(select * from itemTBL);

select * from itemTBL1;


-- 수정
UPDATE itemTBL SET itemName = '고급 세탁기' WHERE itemName = '세탁기1';
UPDATE itemTBL SET itemName = '고급 냉장고' WHERE itemName = '컴퓨터1';




-- CASE~ WHEN ~ ELSE ~ END

SELECT 
  itemName,
  company,
  cost,
  amount,
  CASE 
    WHEN cost >= 20 THEN '고가 제품'
    WHEN cost >= 10 THEN '중가 제품'
    ELSE '저가 제품'
  END AS 등급
FROM itemTBL;


select ascii('a'), CHAR(65);
select itemName, length(itemName) from itemtbl; 