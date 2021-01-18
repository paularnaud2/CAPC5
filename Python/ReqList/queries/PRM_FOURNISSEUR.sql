WITH CTR_FRN AS (
    SELECT DISTINCT ctr.CTR_T_NUM CONTRAT, acm.ACM_T_LIB FOURNISSEUR
    FROM CONTRAT.ASS_CTR_TAM_ACM acta
    JOIN CONTRAT.ACTEUR_MARCHE acm ON acm.ACM_ID = acta.ACM_ID
    JOIN CONTRAT.TYPE_ACTEUR tam ON tam.TAM_ID = acta.TAM_ID
    JOIN CONTRAT.CONTRAT ctr ON ctr.CTR_ID = acta.CTR_ID
    WHERE 1=1
    AND tam.TAM_C_CODE LIKE 'F%'
    )

SELECT prm.PRM_ID, cf.FOURNISSEUR
FROM SGEL_PRM_SCH.T_PRM prm
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
JOIN CTR_FRN cf ON situ.SCN_CF_NUMERO_CONTRAT = cf.CONTRAT
WHERE prm.PRM_ID IN @@IN@@