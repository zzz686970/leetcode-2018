-- 1 last hire_date employee
-- 查找最晚入职员工的所有信息
select * from employees where hire_date in (select max(hire_date) from employees)

-- 2. 查找入职员工时间排名倒数第三的员工所有信息
-- limit  m, n starting from m+1, fetch n records
select * from employees order by hire_date desc limit 2, 1

select * from employees 
	where hire_date = (select hire_date 
								from employees 
								order by hire_date desc limit 2, 1)

select * from (select rownum rn, a.* 
					from (select * from employees 
								order by hire_date desc ) a)
	where rn = 3

-- oracle
select * from (select a.*, dense_rank() over(order by hire_date desc) as rank 
					 from employees ) where rank = 3

-- 3. 查找各个部门当前(to_date='9999-01-01')领导当前薪水详情以及其对应部门编号
-- 主表选择salaries

select s.*, d.dept_no from salaries s join dept_manager as d 
	on s.emp_no = d.emp_no 
	where s.to_date = '9999-01-01'
	and d.to_date = '9999-01-01'


-- 可能出现离职的领导，因此需要做进一步的限制
select salaries.emp_no,salaries.salary,salaries.from_date,salaries.to_date,dept_manager.dept_no 
from dept_manager  inner join salaries
on dept_manager.emp_no = salaries.emp_no
where dept_manager.to_date = '9999-01-01' 
and salaries.to_date = '9999-01-01'
and dept_manager.emp_no is not null;

-- 4. 查找所有已经分配部门的员工的last_name和first_name
select e.last_name, e.first_name, d.dept_no 
	from employees e
	join dept_no d 
	on e.emp_no = d.emp_no;


-- 5. 查找所有员工的last_name和first_name以及对应部门编号dept_no，也包括展示没有分配具体部门的员工
select e.last_name, e.first_name, d.dept_no 
	from employees e
	left join dept_no d 
	on e.emp_no = d.emp_no;

-- 6. 查找所有员工入职时候的薪水情况，给出emp_no以及salary， 并按照emp_no进行逆序
 select e.emp_no, s.salary 
 	from employees as e 
 	join salaries s 
 	on e.emp_no = s.emp_no and e.hire_date = s.from_date
 	order by emp_no

SELECT e.emp_no, s.salary FROM employees AS e, salaries AS s
WHERE e.emp_no = s.emp_no AND e.hire_date = s.from_date
ORDER BY e.emp_no

 select emp_no, salary 
 	from salaries
 	group by emp_no having min(from_date)
 	order by emp_no 
/*
内连接取左右两张表的交集形成一个新表，如果需要对新表进行操作就内连接
from where 并列仍然还是两张表，笛卡尔积先连接再过滤
 */

--7. 查找所有员工入职时候的薪水情况，给出emp_no以及salary， 并按照emp_no进行逆序
SELECT e.emp_no, s.salary FROM employees AS e, salaries AS s
WHERE e.emp_no = s.emp_no AND e.hire_date = s.from_date
ORDER BY e.emp_no DESC

--8. 查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t
select emp_no, count(salary) as t
	from (select distinct emp_no, salary 
			from salaries )
	group by emp_no
	having t > 15;



--9. 找出所有员工当前(to_date='9999-01-01')具体的薪水salary情况，对于相同的薪水只显示一次,并按照逆序显示

select salary from salaries  where to_date='9999-01-01' group by salary order by salary desc;

/*
对于distinct,groupby的性能。
数据量非常巨大时候，比如1000万中有300W重复数据，这时候的distinct的效率略好于group by；
对于相对重复量较小的数据量比如1000万中1万的重复量，用groupby的性能会远优于distnct。
 */

-- mysql获取当前时间 : now()

-- sqlServer获取当前时间: getDate()


--10. 获取所有部门当前manager的当前薪水情况，给出dept_no, emp_no以及salary，当前表示to_date='9999-01-01'


SELECT dept_manager.dept_no,dept_manager.emp_no,salaries.salary
FROM dept_manager,salaries
WHERE dept_manager.emp_no=salaries.emp_no 
AND dept_manager.to_date='9999-01-01' 
AND salaries.to_date='9999-01-01'
and dept_manager.emp_no is not null;


--11. 

































