SELECT DISTINCT a.ID, a.EMAIL, a.FIRST_NAME, a.LAST_NAME
FROM DEVELOPERS a, SKILLCODES b
WHERE 
#b'1000' & b'1111', // 첫 번째 비트만이 둘 다 1이므로, 연산 결과는 b'1000'이 됨.
#b'1000' | b'1111', // 모든 비트에 하나라도 1이 포함되어 있으므로, 연산 결과는 b'1111'이 됨.
    (a.SKILL_CODE & b.CODE) > 0 # 코드 중 연관되는 값이 하나라도 있다면?
    AND b.NAME IN ("Python", "C#") # 그리고 그 값이 파이썬이나 C라면?
ORDER BY a.ID;