SELECT J.FLAVOR
FROM FIRST_HALF H
INNER JOIN JULY J ON J.FLAVOR = H.FLAVOR
GROUP BY FLAVOR
ORDER BY SUM(J.TOTAL_ORDER)+SUM(H.TOTAL_ORDER) DESC
LIMIT 3