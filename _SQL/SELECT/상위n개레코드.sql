SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

-- DATETIME으로 정렬을 한 후 (default 값은 ASC, 오름차순이다)
-- LIMIT 를 통해서 원하는 개수를 가져올 수 있다.

-- ex)  LIMIT 1 : 맨 위에서부터 1개까지 정보 조회
--      LIMIT 3 : 맨 위에서부터 3개까지 정보 조회
--      LIMIT 2,6 : 위에서 2번째부터 6번째까지의 정보 조회