-- 코드를 입력하세요
SELECT B.WRITER_ID
     , U.NICKNAME
     , SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B
INNER JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
WHERE STATUS = 'DONE'
GROUP BY B.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES
# INNER JOIN USED_GOODS_FILE F ON B.