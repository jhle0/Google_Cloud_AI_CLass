REM   Script: 2024-07-08-2.sql
REM   2024-07-08.sql - 그룹 함수

REM   Script: install-emp-dept-salgrade


REM   install-emp-dept-salgrade


REM   Script: Session-Install emp and dept


REM   Session-Install emp and dept


create table dept(   
  deptno     number(2,0),   
  dname      varchar2(14),   
  loc        varchar2(13),   
  constraint pk_dept primary key (deptno)   
);

create table emp(   
  empno    number(4,0),   
  ename    varchar2(10),   
  job      varchar2(9),   
  mgr      number(4,0),   
  hiredate date,   
  sal      number(7,2),   
  comm     number(7,2),   
  deptno   number(2,0),   
  constraint pk_emp primary key (empno),   
  constraint fk_deptno foreign key (deptno) references dept (deptno)   
);

insert into DEPT (DEPTNO, DNAME, LOC) 
values(10, 'ACCOUNTING', 'NEW YORK');

insert into dept   
values(20, 'RESEARCH', 'DALLAS');

insert into dept   
values(30, 'SALES', 'CHICAGO');

insert into dept  
values(40, 'OPERATIONS', 'BOSTON');

insert into emp   
values(   
 7839, 'KING', 'PRESIDENT', null,   
 to_date('17-11-1981','dd-mm-yyyy'),   
 5000, null, 10   
);

insert into emp  
values(  
 7698, 'BLAKE', 'MANAGER', 7839,  
 to_date('1-5-1981','dd-mm-yyyy'),  
 2850, null, 30  
);

insert into emp  
values(  
 7782, 'CLARK', 'MANAGER', 7839,  
 to_date('9-6-1981','dd-mm-yyyy'),  
 2450, null, 10  
);

insert into emp  
values(  
 7566, 'JONES', 'MANAGER', 7839,  
 to_date('2-4-1981','dd-mm-yyyy'),  
 2975, null, 20  
);

insert into emp  
values(  
 7788, 'SCOTT', 'ANALYST', 7566,  
 to_date('13-JUL-87','dd-mm-rr') - 85,  
 3000, null, 20  
);

insert into emp  
values(  
 7902, 'FORD', 'ANALYST', 7566,  
 to_date('3-12-1981','dd-mm-yyyy'),  
 3000, null, 20  
);

insert into emp  
values(  
 7369, 'SMITH', 'CLERK', 7902,  
 to_date('17-12-1980','dd-mm-yyyy'),  
 800, null, 20  
);

insert into emp  
values(  
 7499, 'ALLEN', 'SALESMAN', 7698,  
 to_date('20-2-1981','dd-mm-yyyy'),  
 1600, 300, 30  
);

insert into emp  
values(  
 7521, 'WARD', 'SALESMAN', 7698,  
 to_date('22-2-1981','dd-mm-yyyy'),  
 1250, 500, 30  
);

insert into emp  
values(  
 7654, 'MARTIN', 'SALESMAN', 7698,  
 to_date('28-9-1981','dd-mm-yyyy'),  
 1250, 1400, 30  
);

insert into emp  
values(  
 7844, 'TURNER', 'SALESMAN', 7698,  
 to_date('8-9-1981','dd-mm-yyyy'),  
 1500, 0, 30  
);

insert into emp  
values(  
 7876, 'ADAMS', 'CLERK', 7788,  
 to_date('13-JUL-87', 'dd-mm-rr') - 51,  
 1100, null, 20  
);

insert into emp  
values(  
 7900, 'JAMES', 'CLERK', 7698,  
 to_date('3-12-1981','dd-mm-yyyy'),  
 950, null, 30  
);

insert into emp  
values(  
 7934, 'MILLER', 'CLERK', 7782,  
 to_date('23-1-1982','dd-mm-yyyy'),  
 1300, null, 10  
);

select ename, dname, job, empno, hiredate, loc   
from emp, dept   
where emp.deptno = dept.deptno   
order by ename;

select dname, count(*) count_of_employees 
from dept, emp 
where dept.deptno = emp.deptno 
group by DNAME 
order by 2 desc;

DESC EMP


SELECT * FROM EMP;

DESC EMP 


CREATE TABLE DUMMY (DUMMY NUMBER);

INSERT INTO DUMMY VALUES (0);

CREATE TABLE salgrade ( 
  grade NUMBER, 
  losal NUMBER, 
  hisal NUMBER 
);

INSERT INTO salgrade VALUES (1, 700, 1200);

INSERT INTO salgrade VALUES (2, 1201, 1400);

INSERT INTO salgrade VALUES (3, 1401, 2000);

INSERT INTO salgrade VALUES (4, 2001, 3000);

INSERT INTO salgrade VALUES (5, 3001, 9999);

SELECT AVG(SAL), MAX(SAL), SUM(SAL) FROM EMP;

SELECT AVG(SAL), MAX(SAL), SUM(SAL)  
FROM EMP 
WHERE JOB LIKE 'CLERK';

SELECT MAX(HIREDATE), MIN(HIREDATE) 
FROM EMP;

COUNT(EMP);


COUNT(*);


SELECT COUNT(*) 
FROM EMP;

SELECT AVG(SAL) FORM EMP;

SELECT AVG(SAL) FROM EMP;

SELECT AVG(COMM) FROM EMP;

SELECT AVG(NVL(COMM, 0)) 
FROM EMP;

SELECT ENAME 
FROM EMP 
WHERE DEPTNO IN (10, 20, 30);

SELECT AVG(SAL) 
FROM EMP 
-- WHERE DEPTNO IN (10, 20, 30) 
GROUP BY DEPTNO;

SELECT DEPTNO, AVG(SAL) 
FROM EMP 
-- WHERE DEPTNO IN (10, 20, 30) 
GROUP BY DEPTNO;

SELECT DEPTNO, AVG(SAL) 
FROM EMP;

ELECT DEPTNO, AVG(SAL) 


FROM EMP 


GROUP BY DEPTNO


SELECT DEPTNO, AVG(SAL) 
FROM EMP 
-- WHERE DEPTNO IN (10, 20, 30) 
GROUP BY DEPTNO 
;

SELECT JOB, AVG(SAL) 
FROM EMP 
GROUP BY JOB;

SELECT JOB, AVG(SAL), MAX(SAL), MIN(SAL), SUM(SAL) 
FROM EMP 
GROUP BY JOB;

SELECT DEPTNO, AVG(SAL) 
FROM EMP 
GROUP BY DEPTNO 
HAVING AVG(SAL) >= 2500;

SELECT JOB, AVG(SAL) 
FROM EMP 
GROUP BY JOB 
HAVING AVG(SAL) >= 1500;

SELECT DEPTNO 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, COUNT(*) AS PEOPLE 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, SUM(ENAME) 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, COUNT(*) 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, COUNT(*) AS PEOPLE 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, COUNT(*) AS PEOPLE 
FROM EMP 
GROUP BY DEPTNO 
HAVING COUNT(*) >= 4;

SELECT DEPTNO, COUNT(*) AS PEOPLE 
FROM EMP 
GROUP BY DEPTNO 
HAVING PEOPLE >= 4;

SELECT DEPTNO, COUNT(*) AS PEOPLE 
FROM EMP 
GROUP BY DEPTNO 
HAVING COUNT(*) >= 4;

SELECT AVG(SAL) 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, MAX(AVG(SAL)) 
FROM EMP 
GROUP BY DEPTNO;

SELECT MAX(AVG(SAL)) 
FROM EMP 
GROUP BY DEPTNO;

SELECT DEPTNO, JOB, AVG(SAL) 
FROM EMP 
GROUP BY DEPTNO, JOB;

