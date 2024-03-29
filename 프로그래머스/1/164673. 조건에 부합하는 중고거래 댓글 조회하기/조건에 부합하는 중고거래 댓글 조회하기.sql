SELECT b.TITLE
     , b.BOARD_ID
     , r.REPLY_ID
     , r.WRITER_ID
     , r.CONTENTS
     , DATE_FORMAT(r.CREATED_DATE,'%Y-%m-%d')
FROM USED_GOODS_BOARD b
INNER JOIN USED_GOODS_REPLY r ON b.BOARD_ID = r.BOARD_ID
WHERE b.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY r.CREATED_DATE, b.TITLE












# SELECT B.TITLE
#      , R.BOARD_ID
#      , R.REPLY_ID
#      , R.WRITER_ID
#      , R.CONTENTS
#      , DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
# FROM USED_GOODS_BOARD B
# INNER JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
# WHERE B.CREATED_DATE like '2022-10%'
# ORDER BY B.CREATED_DATE , B.TITLE