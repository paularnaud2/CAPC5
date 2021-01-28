WITH dep_dr as (
	SELECT '01' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '02' as "DEP", 'Picardie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '03' as "DEP", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '04' as "DEP", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '05' as "DEP", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '06' as "DEP", 'Cote d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '07' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '08' as "DEP", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '09' as "DEP", 'Midi Pyrenées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '10' as "DEP", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '11' as "DEP", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '12' as "DEP", 'Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '13' as "DEP", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '14' as "DEP", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '15' as "DEP", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '16' as "DEP", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '17' as "DEP", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '18' as "DEP", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '19' as "DEP", 'Limousin' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '21' as "DEP", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '22' as "DEP", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '23' as "DEP", 'Limousin' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '24' as "DEP", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '25' as "DEP", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '26' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '27' as "DEP", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '28' as "DEP", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '29' as "DEP", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '30' as "DEP", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '31' as "DEP", 'Midi Pyrenées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '32' as "DEP", 'Midi Pyrenées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '33' as "DEP", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '34' as "DEP", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '35' as "DEP", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '36' as "DEP", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '37' as "DEP", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '38' as "DEP", 'Alpes' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '39' as "DEP", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '40' as "DEP", 'Pyrénées et Landes' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '41' as "DEP", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '42' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '43' as "DEP", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '44' as "DEP", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '45' as "DEP", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '46' as "DEP", 'Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '47' as "DEP", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '48' as "DEP", 'Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '49' as "DEP", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '50' as "DEP", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '51' as "DEP", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '52' as "DEP", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '53' as "DEP", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '54' as "DEP", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '55' as "DEP", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '56' as "DEP", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '57' as "DEP", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '58' as "DEP", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '59' as "DEP", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '60' as "DEP", 'Picardie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '61' as "DEP", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '62' as "DEP", 'Nord - Pas de Calais' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '63' as "DEP", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '64' as "DEP", 'Pyrénées et Landes' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '65' as "DEP", 'Pyrénées et Landes' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '66' as "DEP", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '67' as "DEP", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '68' as "DEP", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '69' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '70' as "DEP", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '71' as "DEP", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '72' as "DEP", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '73' as "DEP", 'Alpes' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '74' as "DEP", 'Alpes' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '75' as "DEP", 'Paris' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '76' as "DEP", 'Normandie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '77' as "DEP", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '78' as "DEP", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '79' as "DEP", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '80' as "DEP", 'Picardie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '81' as "DEP", 'Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '82' as "DEP", 'Nord midi Pyrennées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '83' as "DEP", 'Cote d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '84' as "DEP", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '85' as "DEP", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '86' as "DEP", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '87' as "DEP", 'Limousin' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '88' as "DEP", 'Lorraine' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '89' as "DEP", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '90' as "DEP", 'Alsace Franche Comté' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '91' as "DEP", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '92' as "DEP", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '93' as "DEP", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '94' as "DEP", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '95' as "DEP", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL
)

, aff_130 as
(
	SELECT DISTINCT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE, dem.DEM_D_EFFET as DATE_EFFET
	, DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANG
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	WHERE 1=1
	AND nat.NAT_C_PRESTATION LIKE 'F130%'
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

SELECT POINT
, CODE_INSEE, CODE_DEPARTEMENT, CODE_CENTRE, dep_dr.DR, dep_dr.REG
, SI, EN_SERVICE, OH
, CALENDRIER, PS_MAX_KW, P_RAC_KW, COMPTEUR
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
	, aff_130.AFFAIRE F130_EC, aff_130.DATE_EFFET
	, aff_BP.TYPE as BP
	, situ.SCN_GF_CALENDRIER_FOURN_CODE as CALENDRIER
	, situ.SCN_ST_P_SOUSCRITE_MAX_V as PS_MAX_KW
	, talim.ALI_PUISS_RACCO_SOUTI_V as P_RAC_KW
	, cal.CAL_LIBELLE_COMPTEUR
	, DECODE(scm.SCM_DC_STRUCTURE_COMPTAGE_CODE,
		'AMM', 'LINKY',
		scm.SCM_DC_STRUCTURE_COMPTAGE_CODE
		) as COMPTEUR
	, prm.PRM_AI_CODE_INSEE CODE_INSEE, SUBSTR(prm.PRM_AI_CODE_INSEE, 1, 2) CODE_DEPARTEMENT, prm.PRM_DG_CENTRE_CODE CODE_CENTRE
	FROM SGEL_PRM_SCH.T_PRM prm
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
	LEFT JOIN SGEL_SCH.T_CALENDRIER cal ON situ.SCN_GF_CALENDRIER_FOURN_CODE = cal.CAL_CODE
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_COMPTAGE scm ON scm.SCM_ID = prm.SCM_ID
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_ALIMENTATION alim ON prm.SAL_ID = alim.SAL_ID
	LEFT JOIN SGEL_PRM_SCH.T_ALIMENTATION talim ON talim.ALI_ID = alim.ALI_PRINCIPALE_ID
	LEFT JOIN aff_130 aff_130 ON (prm.PRM_ID = aff_130.POINT AND aff_130.RANG = 1)
	LEFT JOIN aff_BP aff_BP ON (prm.PRM_ID = aff_BP.POINT AND aff_BP.RANG = 1)
	WHERE 1=1
	AND prm.PRM_ID IN @@IN1@@
	--AND prm.PRM_ID IN ('30000250132814', '30000250154857', '30000250164108')
) t
LEFT JOIN dep_dr ON t.CODE_DEPARTEMENT = dep_dr.DEP