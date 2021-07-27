SELECT COUNT(*)
FROM ANIMAL_INS

-- COUNT()를 통해서 행의 개수를 구할 수 있다.
-- '*' 대신 COUNT(NAME) 이런 식으로 사용한다면
-- NAME 칼럼에 NULL이 들어있지 않은 행 갯수를 가져오게 될 것이다.