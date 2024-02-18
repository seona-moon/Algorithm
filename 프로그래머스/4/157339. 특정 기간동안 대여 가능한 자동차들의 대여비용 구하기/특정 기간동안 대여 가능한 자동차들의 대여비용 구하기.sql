SELECT C.CAR_ID, C.CAR_TYPE, FLOOR(C.DAILY_FEE*(1-P.DISCOUNT_RATE*0.01)*30) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON C.CAR_TYPE = P.CAR_TYPE
AND P.DURATION_TYPE = '30일 이상'
WHERE C.CAR_TYPE IN ('세단', 'SUV')
AND CAR_ID NOT IN (SELECT DISTINCT CAR_ID
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   WHERE (START_DATE BETWEEN '2022-11-01' AND '2022-11-30')
                   OR (END_DATE BETWEEN '2022-11-01' AND '2022-11-30')
                   OR (START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30'))
AND FLOOR(C.DAILY_FEE*(1-P.DISCOUNT_RATE*0.01)*30) BETWEEN 200000 AND 2000000
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID DESC