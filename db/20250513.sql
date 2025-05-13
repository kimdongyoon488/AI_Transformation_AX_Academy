INSERT INTO buyTbl (memberId, prodName, price, amount)
VALUES
  ('1', 'TV', 50, 1),
  ('2', '에어컨', 120, 2),
  ('3', '냉장고', 80, 1),
  ('4', '선풍기', 30, 3);

INSERT INTO buyTbl (memberId, prodName, price, amount)
VALUES('1', '에어컨', 50, 2);

CREATE TABLE itemTBL (
  itemName VARCHAR(20) NOT NULL,
  company VARCHAR(20) NOT NULL,
  cost INT NOT NULL,
  amount INT NOT NULL
);

INSERT INTO itemTBL (itemName, company, cost, amount)
VALUES 
('컴퓨터1', '삼성', 8, 0),
('세탁기1', 'LG', 25, 30);

select *
from itemTBL;

select itemName, company, cost, amount 
from itemTbl 
order by amount desc;

alter table buyTbl modify prodName varchar(30);

desc buyTbl



-- VARCHAR, CHAR - mysql 은 접두사로 전체 데이터 사이즈를 표기한다
-- (숫자)는 문자 개수를 의미하며 크기가 255 바이트 이내이면 접두사는 포함되지 않음
-- (숫자)는 문자 개수를 의미하며 크기가 256 바이트 이상이면 접두사는 포함되지 않음 
CREATE TABLE vc (v VARCHAR(4), c CHAR(4));
INSERT INTO vc VALUES ('ab  ', 'ab  ');
INSERT INTO vc VALUES ('abcd', 'abcd');
INSERT INTO vc VALUES ('가나다라', '가나다라');

SELECT CONCAT('(', v, ')'), CONCAT('(', c, ')') FROM vc;


ALTER TABLE vc MODIFY v VARCHAR(200);
INSERT INTO vc VALUES ('가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마', '가나다라');


SELECT CONCAT('(', v, ')'), CONCAT('(', c, ')') FROM vc;



SELECT memberId, SUM(amount) as '제품 수' FROM buyTbl
GROUP BY memberId;