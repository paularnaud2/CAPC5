SELECT COUNT(*) VOL, situ.SCN_APP_APPLICATION_CODE SI, prm.PRM_DG_NUMERO_CONTRAT CTR_PRM
, situ.SCN_CF_NUMERO_CONTRAT CTR_SCN, situ.SCN_ST_TYPE_OFFRE_CODE TYPE_OFFRE
FROM SGEL_PRM_SCH.T_PRM prm
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
WHERE 1=1
AND prm.PRM_DG_ETAT_CODE = 'ACTI'
AND prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC'
AND prm.PRM_SC_SEGMENT = 'C5'
AND prm.PRM_DG_NUMERO_CONTRAT IN ('PROTOC-501', 'GRD-F003')
AND prm.PRM_ID LIKE '@@PRM_RANGE_TEST@@%'
AND ROWNUM <= 10
GROUP BY situ.SCN_APP_APPLICATION_CODE, prm.PRM_DG_NUMERO_CONTRAT, situ.SCN_CF_NUMERO_CONTRAT, situ.SCN_ST_TYPE_OFFRE_CODE
ORDER BY 1 DESC