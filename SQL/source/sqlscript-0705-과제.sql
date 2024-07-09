REM   Script: 2024-07-05-r.sql
REM   구글클라우드 AI 수업 과제

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

SELECT HIREDATE 
FROM EMP;

DESC EMP


SELECT HIREDATE 
FROM EMP;

SELECT EMPNO, ENAME, HIREDATE 
FROM EMP 
WHERE HIREDATE >= '01-JAN-81';

SELECT DEPTNO, ENAME, SAL 
FROM EMP 
WHERE DEPTNO = '10' AND SAL >= 3000;

SELECT DEPTNO, ENAME, SAL 
FROM EMP 
WHERE DEPTNO = '10' OR SAL > 3000;

SELECT DEPTNO, ENAME, SAL 
FROM EMP 
WHERE DEPTNO = '10' AND SAL > 3000;

SELECT EMPNO, ENAME, SAL, JOB 
FROM EMP 
WHERE JOB = 'MANAGER' AND SAL >= 1500;

SELECT EMPNO, ENAME, SAL 
FROM EMP 
WHERE SAL >= 1500 & SAL <= 3000;

SELECT EMPNO, ENAME, SAL 
FROM EMP 
WHERE SAL >= 1500 AND SAL <= 3000;

SELECT EMPNO, ENAME, SAL 
FROM EMP 
WHERE SAL BETWEEN 1500 AND 3000;

SELECT EMPNO, ENAME, COMM 
FROM EMP 
WHERE COMM = 300 OR COMM = 500 OR COMM =1400;

SELECT EMPNO, ENAME, COMM 
FROM EMP 
WHERE COMM IN (300, 500, 1400);

SELECT EMPNO, ENAME, MGR 
FROM EMP;

SELECT EMPNO, ENAME, MGR 
FROM EMP 
WHERE MGR = null;

SELECT EMPNO, ENAME, MGR 
FROM EMP 
WHERE MGR = NULL;

SELECT EMPNO, ENAME, MGR 
FROM EMP 
-- WHERE MGR = NULL;  NULL은 할당, 연산, 비교 안됨!!!     
WHERE MGR IS NULL;

SELECT ENAME 
FROM EMP 
WHERE ENAME LIKE S%;

SELECT ENAME 
FROM EMP 
WHERE ENAME LIKE 'S%';

SELECT EMPNO, ENAME 
FROM EMP 
WHERE ENAME LIKE 'S%';

SELECT EMPNO, ENAME 
FROM EMP 
WHERE ENAME LIKE '%S%';

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE JOB NOT IN 'SALESMAN';

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE NOT JON = 'SALSESMAN';

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE NOT JOB = 'SALSESMAN';

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE NOT JOB = 'SALESMAN';

SELECT * FROM DEPT;

SELECT EMPNO, ENAME, SAL 
FROM EMP 
ORDER BY SAL DESC;

SELECT ENAME, (SAL*4) AS "SALARY" 
FROM EMP 
ORDER BY SALARY DESC;

SELECT ENAME, SAL 
FROM EMP 
ORDER BY SAL DESC, FNAME DESC;

SELECT ENAME, SAL 
FROM EMP 
ORDER BY SAL DESC, ENAME DESC;

SELECT ENAME, SAL 
FROM EMP 
ORDER BY SAL DESC, ENAME ASC;

SELECT EMPNP, ENAME, (SAL*4) AS "MONTHSAL", HIREDATE 
FROM EMP;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", HIREDATE 
FROM EMP;

SELECT EMPNO, ENAME, (SAL*4*12) AS "YEARSAL" 
FROM EMP;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", DEPTNO 
FROM EMP;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", DEPTNO 
FROM EMP 
WHERE EMP = '10';

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", DEPTNO 
FROM EMP 
WHERE DEPTNO = '10';

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", COMM, DEPTNO, HIREDATE 
FROM EMP;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", COMM, DEPTNO, HIREDATE 
FROM EMP 
WHERE HIREDATE = '20-FEB-81' 
;

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE ENAME IN ['JONES', 'BLAKE'];

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE ENAME IN ('JONES', 'BLAKE');

SELECT EMPNO, CMM, (SAL*4) AS "MONTHNAME" 
FROM EMP 
WHERE JOB = 'SALESMAN';

SELECT EMPNO, COMM, (SAL*4) AS "MONTHNAME" 
FROM EMP 
WHERE JOB = 'SALESMAN';

DESC EMP


SELECT * FORM EMP;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", HIREDATE 
FROM EMP 
 
 
 
 
-- 2. 사원 테이블에서 사번, 사원이름, 연봉을 얻으시오 
SELECT EMPNO, ENAME, (SAL*4*12) AS "YEARSAL" 
FROM EMP 
 
 
 
 
     
-- 3. 사원 테이블에서 부서 번호가 10번인 사원의 사번, 사원이름, 봉급, 부서번호를 얻으시오 
SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", DEPTNO 
FROM EMP 
WHERE DEPTNO = '10' 
 
 
 
 
 
-- 4. 사원 테이블에서 입사일이 '81/02/20'일인 사원의 사번, 사원이름, 봉급, 커미션, 부서번호를 얻으시오 
SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", COMM, DEPTNO 
FROM EMP 
WHERE HIREDATE = '20-FEB-81' 
 
 
 
 
 
-- 5. 사원 테이블에서 'JONES'와 'BLAKE'의 사번, 이름, 직책을 얻으시오 
SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE ENAME IN ('JONES', 'BLAKE') 
 
 
 
 
-- 6. 사원 테이블에서 직책이 'SALESMAN'인 사원의 사번, 커미션, 봉급을 구하시오 
SELECT EMPNO, COMM, (SAL*4) AS "MONTHNAME" 
FROM EMP 
WHERE JOB = 'SALESMAN' 
 
 
-- 7. 부서 테이블에서 부서위치가 'DALLAS'인 사원의 부서번호, 부서명, 부서위치를 구하시오 
SELECT EMPNO,  
 
SELECT * FORM EMP 
 
 
 
 
-- 8. 사원 테이블에서 봉급이 2000에서 3000사이인 사원의 사번, 사원이름, 봉급을 구하시오 
 
-- 9. 사원 테이블에서 커미션이 800에서 1400사이인 사원의 사번, 사원이름, 커미션을 구하시오 
 
-- 10. 사원 테이블에서 부서번호가 10번이고 직책이 'CLERK'이고 입사일이 82년도인 사원을 모두 얻으시오  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
;

SELECT * FROM EMP;

SELECT * FORM EMP;

SELECT * FROM EMP;

SELECT * FROM DEPT;

SELECT DEPTNO, DNAME, LOC 
FROM DEPT 
WHERE LOC = 'DALLAS';

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL" 
FROM EMP 
WHERE MONTHSAL BETWEEN 2000 AND 3000;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", HIREDATE 
FROM EMP 
 
 
 
 
-- 2. 사원 테이블에서 사번, 사원이름, 연봉을 얻으시오 
SELECT EMPNO, ENAME, (SAL*4*12) AS "YEARSAL" 
FROM EMP 
 
 
 
 
     
-- 3. 사원 테이블에서 부서 번호가 10번인 사원의 사번, 사원이름, 봉급, 부서번호를 얻으시오 
SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", DEPTNO 
FROM EMP 
WHERE DEPTNO = '10' 
 
 
 
 
 
-- 4. 사원 테이블에서 입사일이 '81/02/20'일인 사원의 사번, 사원이름, 봉급, 커미션, 부서번호를 얻으시오 
SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL", COMM, DEPTNO 
FROM EMP 
WHERE HIREDATE = '20-FEB-81';

SELECT EMPNO, ENAME, JOB 
FROM EMP 
WHERE ENAME IN ('JONES', 'BLAKE');

SELECT EMPNO, COMM, (SAL*4) AS "MONTHNAME" 
FROM EMP 
WHERE JOB = 'SALESMAN';

SELECT DEPTNO, DNAME, LOC 
FROM DEPT 
WHERE LOC = 'DALLAS' 
 
 
 
 
-- 8. 사원 테이블에서 봉급이 2000에서 3000사이인 사원의 사번, 사원이름, 봉급을 구하시오 
SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL" 
FROM EMP 
WHERE SAL BETWEEN 2000 AND 3000;

SELECT EMPNO, ENAME, (SAL*4) AS "MONTHSAL" 
FROM EMP 
WHERE SAL BETWEEN 2000 AND 3000;

SELECT * FORM EMP;

SELECT * FROM EMP;

SELECT EMPNO, ENAME, SAL 
FROM EMP 
WHERE SAL BETWEEN 2000 AND 3000;

SELECT EMPNO, ENAME, COMM 
FROM EMP 
WHERE COMM BETWEEN 800 AND 1400;

SELECT EMPNO, ENAME, JOB, DEPTNO, HIREDATE 
FORM EMP 
WHERE DEPTNO = '10' AND JOB = 'CLERK' AND HIREDATE LIKE '%82';

SELECT EMPNO, ENAME, JOB, DEPTNO, HIREDATE 
FROM EMP 
WHERE DEPTNO = '10' AND JOB = 'CLERK' AND HIREDATE LIKE '%82';

