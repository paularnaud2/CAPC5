SELECT DISTINCT
prm.PRM_ID as PDL
, prm.PRM_DG_ETAT_CODE as ETAT_PRM
, prm.PRM_SC_ETAT_CONTRACTUEL_CODE as SCN_PRM
, situ.SCN_APP_APPLICATION_CODE as SI_PRM
, prm.PRM_DG_NIV_OUV_SERV as NIV_OUV_SRV_PRM
FROM SGEL_PRM_SCH.T_PRM prm
LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
WHERE 1=1
AND prm.PRM_ID IN @@IN@@