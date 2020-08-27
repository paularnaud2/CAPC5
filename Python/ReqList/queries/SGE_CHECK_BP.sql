WITH aff_BP as
(
	SELECT DISTINCT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE, dem.DEM_R_STATUT as STATUT
	, CASE WHEN nat.NAT_C_PRESTATION = 'F800B' THEN 'LONG' ELSE 'COURT' END TYPE
	, DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANG
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	WHERE 1=1
	AND nat.NAT_C_PRESTATION IN ('F800B', 'F820')
	AND dem.DEM_ID_PRM NOT LIKE '00%'
	AND dem.DEM_R_STATUT <> 'AFF-ANNULEE'
)

SELECT prm.PRM_ID as POINT
, DECODE(situ.SCN_APP_APPLICATION_CODE
	, 'QETGC', 'DISCO'
	, situ.SCN_APP_APPLICATION_CODE) as SI
, prm.PRM_SC_ETAT_CONTRACTUEL_CODE ETAT_CTR
, CASE WHEN prm.PRM_DG_NUMERO_CONTRAT = 'PROTOC-501' THEN 'O'  ELSE 'N' END as OH
, aff_BP.TYPE as TYPE_BP, aff_BP.AFFAIRE AFF_BP, aff_BP.STATUT AFF_BP_STATUT
FROM SGEL_PRM_SCH.T_PRM prm
LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
LEFT JOIN aff_BP aff_BP ON (prm.PRM_ID = aff_BP.POINT AND aff_BP.RANG = 1)
WHERE 1=1
AND prm.PRM_SC_SEGMENT IN ('C5', 'INDET')
AND prm.PRM_ID IN @@IN1@@
--AND prm.PRM_ID IN ('19524167854286', '01100144557179', '01100289273089', '01140955125222')