--Requete EDF Commerce Hebdo et quotidienne à partir du 14 décembre
SELECT * FROM AFF
WHERE 1=1
AND PRM LIKE '@@PRM_RANGE_2@@%'
AND ROWNUM < 150