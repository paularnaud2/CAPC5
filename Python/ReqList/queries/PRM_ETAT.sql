SELECT DISTINCT prm.PRM_ID as POINT
, prm.PRM_DG_ETAT_CODE as ETAT_PRM
, prm.PRM_SC_ETAT_CONTRACTUEL_CODE as SCN_PRM
FROM SGEL_PRM_SCH.T_PRM prm
WHERE 1=1
AND prm.PRM_ID IN @@IN@@