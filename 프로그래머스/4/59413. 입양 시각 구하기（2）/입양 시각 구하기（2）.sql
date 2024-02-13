SET @HOUR := -1; # 변수 선언
SELECT (@HOUR := @HOUR+1) AS HOUR # 대입 연산자
     , (SELECT COUNT(ANIMAL_ID)
        FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23
ORDER BY HOUR







# SET @HOUR := -1 ; # 변수 선언문
# SELECT (@HOUR := @HOUR +1) AS HOUR # := 대입연산자
#      , (SELECT COUNT(DATETIME) 
#         FROM ANIMAL_OUTS 
#         WHERE HOUR(DATETIME) = @HOUR) AS COUNT
# FROM ANIMAL_OUTS
# WHERE @HOUR < 23