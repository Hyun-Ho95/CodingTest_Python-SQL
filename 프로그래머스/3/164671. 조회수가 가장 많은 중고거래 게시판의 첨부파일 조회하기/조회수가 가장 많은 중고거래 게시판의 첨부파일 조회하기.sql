SELECT CONCAT('/home/grep/src/',F.BOARD_ID,'/',F.FILE_ID,F.FILE_NAME,F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD B
INNER JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE B.BOARD_ID = (SELECT BOARD_ID
                    FROM USED_GOODS_BOARD 
                    GROUP BY BOARD_ID
                    ORDER BY VIEWS DESC
                    LIMIT 1)
ORDER BY F.FILE_ID DESC