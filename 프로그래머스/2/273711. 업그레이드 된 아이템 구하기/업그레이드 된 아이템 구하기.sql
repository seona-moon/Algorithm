# 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템
SELECT ITEM_ID,ITEM_NAME,RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (SELECT IT.ITEM_ID
                FROM ITEM_TREE IT
                JOIN ITEM_INFO II ON II.ITEM_ID = IT.PARENT_ITEM_ID
                WHERE II.RARITY = 'RARE')
ORDER BY ITEM_ID DESC