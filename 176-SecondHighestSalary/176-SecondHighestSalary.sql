-- Last updated: 6/12/2026, 12:45:03 AM
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee); 