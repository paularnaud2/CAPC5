WITH t as(
	SELECT prm.PRM_ID as PRM
	, situ.SCN_ST_TYPE_OFFRE_CODE TYPE_OFFRE_SCN
	, CASE WHEN prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC' THEN 'O' ELSE 'N' END EN_SERVICE
	, CASE WHEN prm.PRM_DG_NUMERO_CONTRAT = 'PROTOC-501' THEN 'OH' ELSE 'NO' END as TYPE_OFFRE_CTR
	FROM SGEL_PRM_SCH.T_PRM prm
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
)

SELECT COUNT(*) VOL
, DATE_EFFET_SOUHAITEE
, DATE_EFFET_PREVUE
, PRESTATION
, MODEREA
, REGION
, SI
, EN_SERVICE
, TYPE_OFFRE
FROM
(
	SELECT dem.DEM_ID_PRM as PRM, dem.AFF_T_DISCO as AFFAIRE
	, nat.NAT_C_PRESTATION PRESTATION
	, dem.DEM_R_STATUT STATUT
	, ee.EST_T_ETAT as ETAT_EXTERNE
	, TO_CHAR(t_pres.PRE_DEM_DATEEFFET, 'DD/MM/YYYY')as DATE_EFFET_SOUHAITEE
	, TO_CHAR(t_rece.PRE_REC_REC_DATE_EFFET, 'DD/MM/YYYY')as DATE_EFFET_PREVUE
	, frn.FRN_T_ACTEUR as FOURNISSEUR
	, DECODE (mai.MAI_T_REGION
		, 'M8 - Auvergne Centre Limousin', 'ACL'
		, 'M8 - Est', 'EST'
		, 'M8 - Ile de France', 'IDF'
		, 'M8 - Manche Mer du Nord', 'MMN'
		, 'M8 - Méditerranée', 'MED'
		, 'M8 - Ouest', 'OUE'
		, 'M8 - Rhône Alpes Bourgogne', 'RAB'
		, 'M8 - Sud Ouest', 'SUO'
		) REGION
	, CASE WHEN  nat.NAT_C_PRESTATION LIKE '%A' THEN 'COSY' ELSE 'GINKO' END SI
	, t_rece.PRE_REC_REC_MODEREA_CODE MODEREA
	, t.EN_SERVICE
	, CASE WHEN t.TYPE_OFFRE_SCN IS NULL THEN t.TYPE_OFFRE_CTR ELSE t.TYPE_OFFRE_SCN END TYPE_OFFRE
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
	LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
	LEFT JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
	LEFT JOIN SGEL_IAP_SCH.T_AFFAIRE aff ON dem.AFF_T_DISCO = aff.AFF_ID
	LEFT JOIN SGEL_IAP_SCH.T_PRESTATION t_pres ON aff.AFF_ID_SEQUENCE = t_pres.AFF_ID_SEQUENCE
	LEFT JOIN SGEL_IAP_SCH.T_RECEVABILITE t_rece ON t_pres.PRE_REC_ID = t_rece.PRE_REC_ID
	LEFT JOIN t ON dem.DEM_ID_PRM = t.PRM
	WHERE 1=1
	AND dem.DEM_R_STATUT IN ('AFF-ENCOURS', 'AFF-TERMINEE')
	AND t_rece.PRE_REC_REC_DATE_EFFET >= TO_DATE('01/01/2021', 'DD/MM/YYYY')
	AND t_rece.PRE_REC_REC_DATE_EFFET <= TO_DATE('03/01/2021', 'DD/MM/YYYY')
)
GROUP BY 
 DATE_EFFET_SOUHAITEE
, DATE_EFFET_PREVUE
, PRESTATION
, MODEREA
, REGION
, SI
, EN_SERVICE
, TYPE_OFFRE