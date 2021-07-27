## 📌 Problem
Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

Input Format

The Employee table containing employee data for a company is described as follows:

![](image/2021-02-25-20-01-07.png)

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.

**Sample Input**

![](image/2021-02-25-20-02-01.png)

**Sample Output**
```
Angela
Bonnie
Frank
Joe
Kimberly
Lisa
Michael
Patrick
Rose
Todd
```

</br>

## 📌 Code
문제가 긴데, 읽어보면 단순히 name을 알파벳 순서로 정렬하라는 거다.<br>
`ORDER BY` 부분에 숫자 1을 썼는데 의미는 'SELECT문에서 첫번째 있는 걸로 정렬해줘' 라는 뜻이다.
```sql
SELECT NAME
FROM Employee
ORDER BY 1;
```