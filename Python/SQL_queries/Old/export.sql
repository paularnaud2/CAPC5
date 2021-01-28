SET echo OFF
SET colsep ','
spool "C:\Users\pa159cbn\Desktop\export.csv"
SELECT prm.PRM_ID,
  situ.SCN_SIT_DATE_DEBUT
FROM SGEL_PRM_SCH.T_PRM prm
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ
ON prm.SCN_ID                     = situ.SCN_ID
WHERE 1                           =1
--AND prm.PRM_ID = '14405643841002'
AND situ.SCN_SITU_TYPE            = 'C'
AND prm.PRM_SC_DATE_DER_MES          IS NULL
AND situ.SCN_APP_APPLICATION_CODE = 'GINKO'
AND prm.PRM_SC_SEGMENT = 'C5';
SPOOL OFF;