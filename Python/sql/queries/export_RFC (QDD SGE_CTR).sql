SELECT rot.PRM_ID as POINT, '1' as ETAT
FROM BIC_REFERENTIEL.T_ROLE_TITULAIRE rot
JOIN BIC_REFERENTIEL.T_CONTRAT_ACCES ctr ON ctr.ROT_ID = rot.ROT_ID
WHERE 1=1
AND ctr.ACC_DATE_FIN IS NULL
AND ctr.ACC_SEGMENT = 'C5'