## 📌 Problem
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

![](image/2021-03-10-11-59-45.png)

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

- Root: If node is root node.
- Leaf: If node is leaf node.
- Inner: If node is neither root nor leaf node.

**Sample Input**

![](image/2021-03-10-12-00-34.png)

**Sample Output**
```
1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf
```

**Explanation**

The Binary Tree below illustrates the sample:
![](image/2021-03-10-12-01-17.png)

<br>

## 📌 Code
```sql
select N, (case
                when P is NULL then 'Root'
                when N not in (select distinct P from BST where P is not NULL) then 'Leaf'
                else 'Inner'
            end)
from BST
order by 1;
```

<br>

## 📌 풀이
- parent is Null -> 'Root'
- parent not in (parent 리스트) -> 'Leaf'
- 둘 다 아니라면 -> 'Inner'

```sql
case
    when P is NULL then 'Root'
    when N not in (select distinct P from BST where P is not NULL) then 'Leaf'
    else 'Inner'
end
```