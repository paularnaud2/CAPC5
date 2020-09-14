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
	SELECT '091' as "CCD", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '092' as "CCD", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '093' as "CCD", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '094' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '095' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '096' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '097' as "CCD", 'Centre' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '121' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '122' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '124' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '125' as "CCD", 'Bourgogne' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '142' as "CCD", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '143' as "CCD", 'Pays de Loire' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '144' as "CCD", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '145' as "CCD", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '146' as "CCD", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '147' as "CCD", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '148' as "CCD", 'Bretagne' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '151' as "CCD", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '152' as "CCD", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
	SELECT '154' as "CCD", 'Poitou Charentes' as "DR", 'OUEST' as "REG" FROM DUAL UNION ALL
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
	SELECT '214' as "CCD", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '215' as "CCD", 'IDF Ouest' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '221' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '222' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '223' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '224' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '225' as "CCD", 'IDF Est' as "DR", 'IDF' as "REG" FROM DUAL UNION ALL
	SELECT '231' as "CCD", 'Midi Pyrénées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '232' as "CCD", 'Midi Pyrénées Sud et Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '233' as "CCD", 'Midi Pyrénées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '234' as "CCD", 'Midi Pyrénées Sud et Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '235' as "CCD", 'Midi Pyrénées Sud et Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '241' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '242' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '243' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '245' as "CCD", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '251' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '252' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '253' as "CCD", 'Côte d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '254' as "CCD", 'Côte d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '256' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '258' as "CCD", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '259' as "CCD", 'Côte d''Azur' as "DR", 'MED' as "REG" FROM DUAL
)

, dep_dr as (
	SELECT '01' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '02' as "DEP", 'Picardie' as "DR", 'MMN' as "REG" FROM DUAL UNION ALL
	SELECT '03' as "DEP", 'Auvergne' as "DR", 'ACL' as "REG" FROM DUAL UNION ALL
	SELECT '04' as "DEP", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '05' as "DEP", 'Provence Alpes du Sud' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '06' as "DEP", 'Côte d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '07' as "DEP", 'Sillon Rhodanien' as "DR", 'RAB' as "REG" FROM DUAL UNION ALL
	SELECT '08' as "DEP", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '09' as "DEP", 'Midi Pyrénées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '10' as "DEP", 'Champagne Ardennes' as "DR", 'EST' as "REG" FROM DUAL UNION ALL
	SELECT '11' as "DEP", 'LARO' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
	SELECT '12' as "DEP", 'Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
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
	SELECT '31' as "DEP", 'Midi Pyrénées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '32' as "DEP", 'Midi Pyrénées Sud' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
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
	SELECT '46' as "DEP", 'Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '47' as "DEP", 'Aquitaine Nord' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '48' as "DEP", 'Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
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
	SELECT '81' as "DEP", 'Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '82' as "DEP", 'Nord midi Pyrénées' as "DR", 'SO' as "REG" FROM DUAL UNION ALL
	SELECT '83' as "DEP", 'Côte d''Azur' as "DR", 'MED' as "REG" FROM DUAL UNION ALL
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

, aff_130 as (
	SELECT DISTINCT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE, dem.DEM_D_EFFET as DATE_EFFET
	, DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANG
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	WHERE 1=1
	AND nat.NAT_C_PRESTATION IN ('F130B')
	AND dem.DEM_R_STATUT IN ('AFF-ENCOURS')
)

, aff_BP as (
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

SELECT DISTINCT POINT PRM, SEG
, CODE_INSEE, CODE_DEPARTEMENT, t.CCD, COMMUNE
, CASE WHEN ccd_dr.DR IS NOT NULL THEN ccd_dr.DR ELSE dep_dr.DR END DR
, CASE WHEN ccd_dr.REG IS NOT NULL THEN ccd_dr.REG ELSE dep_dr.REG END REG
, SI, EN_SERVICE
, CASE WHEN TYPE_OFFRE_SCN IS NULL THEN TYPE_OFFRE_CTR ELSE TYPE_OFFRE_SCN END TYPE_OFFRE
, CALENDRIER, CAL_LIBELLE_COMPTEUR
, PS_MAX_KW, P_RAC_KW
, COMPTEUR, CPT_COMMUNIQUANT, CPT_TO, CPT_ACCESSIBLE, MODE_RLV, MEDIA
, F130_EC, DATE_EFFET
, BP
, COLOC
FROM
(
	SELECT prm.PRM_ID as POINT
	, prm.PRM_SC_SEGMENT SEG
	, DECODE(situ.SCN_APP_APPLICATION_CODE
		, 'QETGC', 'DISCO'
		, situ.SCN_APP_APPLICATION_CODE) as SI
	, CASE WHEN prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC' THEN 'O' ELSE 'N' END EN_SERVICE
	, prm.PRM_DG_NUMERO_CONTRAT CONTRAT
	, situ.SCN_ST_TYPE_OFFRE_CODE TYPE_OFFRE_SCN
	, CASE WHEN prm.PRM_DG_NUMERO_CONTRAT = 'PROTOC-501' THEN 'OH' ELSE 'NO' END as TYPE_OFFRE_CTR
	, situ.SCN_GF_CALENDRIER_FOURN_CODE as CALENDRIER
	, situ.SCN_ST_P_SOUSCRITE_MAX_V as PS_MAX_KW
	, talim.ALI_PUISS_RACCO_SOUTI_V as P_RAC_KW
	, cal.CAL_LIBELLE_COMPTEUR
	, DECODE(scm.SCM_DC_STRUCTURE_COMPTAGE_CODE,
		'AMM', 'LINKY',
		'', 'SSCPT'
		,scm.SCM_DC_STRUCTURE_COMPTAGE_CODE
		) as COMPTEUR
	, scm.SCM_MODE_RELEVE_CODE MODE_RLV
	, scm.SCM_MEDIA_CODE MEDIA
	, CASE WHEN prm.PRM_DG_NIV_OUV_SERV > 0 THEN 'O'
			WHEN scm.SCM_MODE_RELEVE_CODE = 'TRLV' THEN 'O'
			ELSE 'N' END CPT_COMMUNIQUANT
	, CASE WHEN situ.SCN_APP_APPLICATION_CODE IN ('QETGC', 'GINKO') THEN CASE WHEN scm.SCM_TELEOPERABLE = '1' THEN 'O' ELSE 'N' END
			ELSE NULL END CPT_TO
	, DECODE(eqeCPT.EQE_ACCESSIBILITE
		, '0', 'N'
		, '1', 'O'
		, 'N'
		) CPT_ACCESSIBLE
	, prm.PRM_AI_CODE_INSEE CODE_INSEE
	, CASE WHEN SUBSTR(prm.PRM_ID, 1, 3) LIKE '500%' OR SUBSTR(prm.PRM_ID, 1, 3) LIKE '300%'
		THEN prm.PRM_DG_CENTRE_CODE ELSE SUBSTR(prm.PRM_ID, 1, 3)
		END CCD
	, SUBSTR(prm.PRM_AI_CODE_INSEE, 1, 2) CODE_DEPARTEMENT
	, SUBSTR(prm.PRM_AIN_LIGNE6, 7) COMMUNE
	, aff_130.AFFAIRE F130_EC, aff_130.DATE_EFFET
	, aff_BP.TYPE as BP
	, CASE WHEN cf.PRS_MOR_ACTIVITE = 'COLOC' THEN 'O' ELSE 'N' END COLOC
	FROM SGEL_PRM_SCH.T_PRM prm
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
	LEFT JOIN SGEL_SCH.T_CALENDRIER cal ON situ.SCN_GF_CALENDRIER_FOURN_CODE = cal.CAL_CODE
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_COMPTAGE scm ON scm.SCM_ID = prm.SCM_ID
	LEFT JOIN SGEL_PRM_SCH.T_EQUIPEMENT eqeCPT ON eqeCPT.SCM_C_ID = prm.SCM_ID
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_ALIMENTATION alim ON prm.SAL_ID = alim.SAL_ID
	LEFT JOIN SGEL_PRM_SCH.T_ALIMENTATION talim ON talim.ALI_ID = alim.ALI_PRINCIPALE_ID
	LEFT JOIN SGEL_PRM_SCH.T_PERSONNE cf ON situ.SCN_CLIENT_FINAL_ID = cf.PRS_ID
	LEFT JOIN aff_130 aff_130 ON (prm.PRM_ID = aff_130.POINT AND aff_130.RANG = 1)
	LEFT JOIN aff_BP aff_BP ON (prm.PRM_ID = aff_BP.POINT AND aff_BP.RANG = 1)
	WHERE 1=1
	AND prm.PRM_ID IN @@IN1@@
	-- AND prm.PRM_ID IN ('22177279218565', '02444862487788', '19524167854286', '01100144557179', '01100289273089', '30000110326267', '30000751220199', '30002130773580')
	-- AND prm.PRM_ID = '22177279218565'
) t
LEFT JOIN ccd_dr ccd_dr ON t.CCD = ccd_dr.CCD
LEFT JOIN dep_dr dep_dr ON t.CODE_DEPARTEMENT = dep_dr.DEP
-- WHERE CPT_COMMUNIQUANT = 'N'
-- ORDER BY POINT