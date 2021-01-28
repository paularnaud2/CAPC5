WITH ccd_dr as (
	SELECT '011' as "CCD", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '012' as "CCD", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '013' as "CCD", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '014' as "CCD", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '015' as "CCD", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '016' as "CCD", 'Picardie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '021' as "CCD", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '022' as "CCD", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '023' as "CCD", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '024' as "CCD", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '025' as "CCD", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '026' as "CCD", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '041' as "CCD", 'Picardie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '042' as "CCD", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '043' as "CCD", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '045' as "CCD", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '051' as "CCD", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '052' as "CCD", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '054' as "CCD", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '055' as "CCD", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '056' as "CCD", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '063' as "CCD", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '064' as "CCD", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '065' as "CCD", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '071' as "CCD", 'Paris' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '072' as "CCD", 'Paris' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '073' as "CCD", 'Paris' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '074' as "CCD", 'Paris' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '075' as "CCD", 'Paris' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '091' as "CCD", 'Pays de Loire' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '092' as "CCD", 'Pays de Loire' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '093' as "CCD", 'Pays de Loire' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '094' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '095' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '096' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '097' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '121' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '122' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '124' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '125' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '142' as "CCD", 'Pays de Loire' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '143' as "CCD", 'Pays de Loire' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '144' as "CCD", 'Bretagne' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '145' as "CCD", 'Bretagne' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '146' as "CCD", 'Bretagne' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '147' as "CCD", 'Bretagne' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '148' as "CCD", 'Bretagne' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '151' as "CCD", 'Poitou Charentes' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '152' as "CCD", 'Poitou Charentes' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '154' as "CCD", 'Poitou Charentes' as "DR", 'Ouest' as "REG" FROM DUAL UNION ALL
	SELECT '155' as "CCD", 'Limousin' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '161' as "CCD", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '162' as "CCD", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '163' as "CCD", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '164' as "CCD", 'Pyrénées et Landes' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '165' as "CCD", 'Pyrénées et Landes' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '171' as "CCD", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '172' as "CCD", 'Auvergne et Limousin' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '173' as "CCD", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '175' as "CCD", 'Auvergne et Limousin' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '176' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '177' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '179' as "CCD", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '191' as "CCD", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '193' as "CCD", 'Alpes' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '194' as "CCD", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '195' as "CCD", 'Alpes' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '196' as "CCD", 'Alpes' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '197' as "CCD", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '198' as "CCD", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '199' as "CCD", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '211' as "CCD", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '212' as "CCD", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '213' as "CCD", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '214' as "CCD", 'IDF OUest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '215' as "CCD", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '221' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '222' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '223' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '224' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '225' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '231' as "CCD", 'Midi Pyrenées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '232' as "CCD", 'Midi Pyrenées Sud et Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '233' as "CCD", 'Midi Pyrenées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '234' as "CCD", 'Midi Pyrenées Sud et Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '235' as "CCD", 'Midi Pyrenées Sud et Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '241' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '242' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '243' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '245' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '251' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '252' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '253' as "CCD", 'Cote d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '254' as "CCD", 'Cote d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '256' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '258' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '259' as "CCD", 'Cote d''Azur' as "DR", 'MED' as "REG" FROM DUAL
)

, aff_130 as
(
	SELECT DISTINCT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE, dem.DEM_D_EFFET as DATE_EFFET
	, DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANG
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	WHERE 1=1
	AND nat.NAT_C_PRESTATION IN ('F130B')
	AND dem.DEM_R_STATUT IN ('AFF-ENCOURS')
)

, aff_BP as
(
	SELECT DISTINCT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE
	, CASE WHEN nat.NAT_C_PRESTATION = 'F800B' THEN 'LONG' ELSE 'COURT' END TYPE
	, DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANG
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	WHERE 1=1
	AND nat.NAT_C_PRESTATION IN ('F800B', 'F820')
	AND dem.DEM_ID_PRM NOT LIKE '00%'
	AND dem.DEM_R_STATUT <> 'AFF-ANNULEE'
)

SELECT DISTINCT POINT
, CODE_INSEE, CODE_DEPARTEMENT, COMMUNE, ccd_dr.DR, ccd_dr.REG
, SI, EN_SERVICE, OH
, CALENDRIER, CAL_LIBELLE_COMPTEUR, COMPTEUR, CPT_COMMUNIQUANT, CPT_ACCESSIBLE
, F130_EC, DATE_EFFET
, BP
FROM
(
	SELECT prm.PRM_ID as POINT
	, DECODE(situ.SCN_APP_APPLICATION_CODE
		, 'QETGC', 'DISCO'
		, situ.SCN_APP_APPLICATION_CODE) as SI
	, CASE WHEN prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC' THEN 'O' ELSE 'N' END EN_SERVICE
	, CASE WHEN prm.PRM_DG_NUMERO_CONTRAT = 'PROTOC-501' THEN 'O'  ELSE 'N' END as OH
	, situ.SCN_GF_CALENDRIER_FOURN_CODE as CALENDRIER
	, cal.CAL_LIBELLE_COMPTEUR
	, DECODE(scm.SCM_DC_STRUCTURE_COMPTAGE_CODE,
		'AMM', 'LINKY',
		'', 'SSCPT'
		,scm.SCM_DC_STRUCTURE_COMPTAGE_CODE
		) as COMPTEUR
	, CASE WHEN prm.PRM_DG_NIV_OUV_SERV > 0 THEN 'O' ELSE 'N' END CPT_COMMUNIQUANT
	, SUBSTR(prm.PRM_ID, 1, 3) CCD
		, DECODE(eqeCPT.EQE_ACCESSIBILITE
		, '0', 'N'
		, '1', 'O'
		, 'N'
		) CPT_ACCESSIBLE
	, prm.PRM_AI_CODE_INSEE CODE_INSEE, SUBSTR(prm.PRM_AI_CODE_INSEE, 1, 2) CODE_DEPARTEMENT, SUBSTR(prm.PRM_AIN_LIGNE6, 7) COMMUNE
	, aff_130.AFFAIRE F130_EC, aff_130.DATE_EFFET
	, aff_BP.TYPE as BP
	FROM SGEL_PRM_SCH.T_PRM prm
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
	LEFT JOIN SGEL_SCH.T_CALENDRIER cal ON situ.SCN_GF_CALENDRIER_FOURN_CODE = cal.CAL_CODE
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_COMPTAGE scm ON scm.SCM_ID = prm.SCM_ID
	LEFT JOIN SGEL_PRM_SCH.T_EQUIPEMENT eqeCPT ON eqeCPT.SCM_C_ID = prm.SCM_ID
	LEFT JOIN aff_130 aff_130 ON (prm.PRM_ID = aff_130.POINT AND aff_130.RANG = 1)
	LEFT JOIN aff_BP aff_BP ON (prm.PRM_ID = aff_BP.POINT AND aff_BP.RANG = 1)
	WHERE 1=1
	AND prm.PRM_ID IN @@IN1@@
	--AND prm.PRM_ID IN ('02444862487788', '19524167854286', '01100144557179', '01100289273089', '01140955125222')
	--AND prm.PRM_ID = '16491895731234'
) t
LEFT JOIN ccd_dr ON t.CCD = ccd_dr.CCD
--WHERE CPT_COMMUNIQUANT = 'N'