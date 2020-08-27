WITH frn AS (
    SELECT DISTINCT ctr.CTR_T_NUM CONTRAT, acm.ACM_T_LIB FRN , acta.ACT_C_EIC EIC
    FROM CONTRAT.ASS_CTR_TAM_ACM acta
    JOIN CONTRAT.ACTEUR_MARCHE acm ON acm.ACM_ID = acta.ACM_ID
    JOIN CONTRAT.TYPE_ACTEUR tam ON tam.TAM_ID = acta.TAM_ID
    JOIN CONTRAT.CONTRAT ctr ON ctr.CTR_ID = acta.CTR_ID
    WHERE 1=1
    AND tam.TAM_C_CODE LIKE 'F%'
)

SELECT prm.PRM_ID POINT
, prm.PRM_DG_ETAT_CODE as ETAT_SGE
, prm.PRM_SC_ETAT_CONTRACTUEL_CODE as SCN_SGE
, situ.SCN_CF_NUMERO_CONTRAT CONTRAT_SGE
, situ.SCN_CF_CATEGORIE_CODE as CAT_SGE
--, prm.PRM_DG_NIV_OUV_SERV as NIV_OUV_SRV_SGE
--, CASE WHEN prm.PRM_DG_NIV_OUV_SERV > 0 THEN 'O' ELSE 'N' END COMMUNIQUANT
, TO_CHAR(situ.SCN_SIT_DATE_DEBUT, 'DD/MM/YYYY') DATE_DEBUT_SCN_SGE
--, TO_CHAR(situ.SCN_SIT_DATE_FIN, 'DD/MM/YYYY') DATE_FIN_SCN_SGE
, TO_CHAR(prm.PRM_TECH_DATE_MAJ	, 'DD/MM/YYYY') DATE_MAJ_SGE
, DECODE(situ.SCN_APP_APPLICATION_CODE
		, 'QETGC', 'DISCO'
		, situ.SCN_APP_APPLICATION_CODE) as SI_SGE
--, situ.SCN_ST_FORM_TARIF_ACHEMIN as FTA_SGE
, frn.FRN FRN_SGE
FROM SGEL_PRM_SCH.T_PRM prm
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
JOIN frn frn ON situ.SCN_CF_NUMERO_CONTRAT = frn.CONTRAT
WHERE 1=1
AND prm.PRM_ID IN @@IN1@@