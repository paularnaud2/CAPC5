SELECT prm.PRM_ID, prm.PRM_SC_ETAT_CONTRACTUEL_CODE, prm.PRM_DG_NUMERO_CONTRAT
FROM SGEL_PRM_SCH.T_PRM prm
WHERE 1=1
AND prm.PRM_SC_SEGMENT = 'C5'
AND prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC'
AND prm.PRM_ID LIKE '@@PRM_RANGE_TEST@@%'
AND ROWNUM <= 10