SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC;

-- ORDER BY 에 여러 기준을 넣어줄 수 있다.
-- 위와 같이 작성한다면
-- 우선 NAME을 기준으로 오름차순으로 정렬 후
-- DATETIME을 기준으로 내림차순으로 한번 더 정렬한다.