WITH t as (
	SELECT '011' as "CCD", 'MMN' as "DR", 'Nord - Pas de Calais' as "DIR" FROM DUAL UNION ALL
	SELECT '012' as "CCD", 'MMN' as "DR", 'Nord - Pas de Calais' as "DIR" FROM DUAL UNION ALL
	SELECT '013' as "CCD", 'MMN' as "DR", 'Nord - Pas de Calais' as "DIR" FROM DUAL UNION ALL
	SELECT '014' as "CCD", 'MMN' as "DR", 'Nord - Pas de Calais' as "DIR" FROM DUAL UNION ALL
	SELECT '015' as "CCD", 'MMN' as "DR", 'Nord - Pas de Calais' as "DIR" FROM DUAL UNION ALL
	SELECT '016' as "CCD", 'MMN' as "DR", 'Picardie' as "DIR" FROM DUAL UNION ALL
	SELECT '021' as "CCD", 'MMN' as "DR", 'Normandie' as "DIR" FROM DUAL UNION ALL
	SELECT '022' as "CCD", 'MMN' as "DR", 'Normandie' as "DIR" FROM DUAL UNION ALL
	SELECT '023' as "CCD", 'MMN' as "DR", 'Normandie' as "DIR" FROM DUAL UNION ALL
	SELECT '024' as "CCD", 'MMN' as "DR", 'Normandie' as "DIR" FROM DUAL UNION ALL
	SELECT '025' as "CCD", 'MMN' as "DR", 'Normandie' as "DIR" FROM DUAL UNION ALL
	SELECT '026' as "CCD", 'MMN' as "DR", 'Normandie' as "DIR" FROM DUAL UNION ALL
	SELECT '041' as "CCD", 'MMN' as "DR", 'Picardie' as "DIR" FROM DUAL UNION ALL
	SELECT '042' as "CCD", 'EST' as "DR", 'Champagne Ardennes' as "DIR" FROM DUAL UNION ALL
	SELECT '043' as "CCD", 'EST' as "DR", 'Champagne Ardennes' as "DIR" FROM DUAL UNION ALL
	SELECT '045' as "CCD", 'EST' as "DR", 'Champagne Ardennes' as "DIR" FROM DUAL UNION ALL
	SELECT '051' as "CCD", 'EST' as "DR", 'Lorraine' as "DIR" FROM DUAL UNION ALL
	SELECT '052' as "CCD", 'EST' as "DR", 'Champagne Ardennes' as "DIR" FROM DUAL UNION ALL
	SELECT '054' as "CCD", 'EST' as "DR", 'Lorraine' as "DIR" FROM DUAL UNION ALL
	SELECT '055' as "CCD", 'EST' as "DR", 'Lorraine' as "DIR" FROM DUAL UNION ALL
	SELECT '056' as "CCD", 'EST' as "DR", 'Lorraine' as "DIR" FROM DUAL UNION ALL
	SELECT '063' as "CCD", 'EST' as "DR", 'Alsace Franche Comté' as "DIR" FROM DUAL UNION ALL
	SELECT '064' as "CCD", 'EST' as "DR", 'Alsace Franche Comté' as "DIR" FROM DUAL UNION ALL
	SELECT '065' as "CCD", 'EST' as "DR", 'Alsace Franche Comté' as "DIR" FROM DUAL UNION ALL
	SELECT '071' as "CCD", 'IDF' as "DR", 'Paris' as "DIR" FROM DUAL UNION ALL
	SELECT '072' as "CCD", 'IDF' as "DR", 'Paris' as "DIR" FROM DUAL UNION ALL
	SELECT '073' as "CCD", 'IDF' as "DR", 'Paris' as "DIR" FROM DUAL UNION ALL
	SELECT '074' as "CCD", 'IDF' as "DR", 'Paris' as "DIR" FROM DUAL UNION ALL
	SELECT '075' as "CCD", 'IDF' as "DR", 'Paris' as "DIR" FROM DUAL UNION ALL
	SELECT '091' as "CCD", 'Ouest' as "DR", 'Pays de Loire' as "DIR" FROM DUAL UNION ALL
	SELECT '092' as "CCD", 'Ouest' as "DR", 'Pays de Loire' as "DIR" FROM DUAL UNION ALL
	SELECT '093' as "CCD", 'Ouest' as "DR", 'Pays de Loire' as "DIR" FROM DUAL UNION ALL
	SELECT '094' as "CCD", 'ACL' as "DR", 'Centre' as "DIR" FROM DUAL UNION ALL
	SELECT '095' as "CCD", 'ACL' as "DR", 'Centre' as "DIR" FROM DUAL UNION ALL
	SELECT '096' as "CCD", 'ACL' as "DR", 'Centre' as "DIR" FROM DUAL UNION ALL
	SELECT '097' as "CCD", 'ACL' as "DR", 'Centre' as "DIR" FROM DUAL UNION ALL
	SELECT '121' as "CCD", 'RAB' as "DR", 'Bourgogne' as "DIR" FROM DUAL UNION ALL
	SELECT '122' as "CCD", 'RAB' as "DR", 'Bourgogne' as "DIR" FROM DUAL UNION ALL
	SELECT '124' as "CCD", 'RAB' as "DR", 'Bourgogne' as "DIR" FROM DUAL UNION ALL
	SELECT '125' as "CCD", 'RAB' as "DR", 'Bourgogne' as "DIR" FROM DUAL UNION ALL
	SELECT '142' as "CCD", 'Ouest' as "DR", 'Pays de Loire' as "DIR" FROM DUAL UNION ALL
	SELECT '143' as "CCD", 'Ouest' as "DR", 'Pays de Loire' as "DIR" FROM DUAL UNION ALL
	SELECT '144' as "CCD", 'Ouest' as "DR", 'Bretagne' as "DIR" FROM DUAL UNION ALL
	SELECT '145' as "CCD", 'Ouest' as "DR", 'Bretagne' as "DIR" FROM DUAL UNION ALL
	SELECT '146' as "CCD", 'Ouest' as "DR", 'Bretagne' as "DIR" FROM DUAL UNION ALL
	SELECT '147' as "CCD", 'Ouest' as "DR", 'Bretagne' as "DIR" FROM DUAL UNION ALL
	SELECT '148' as "CCD", 'Ouest' as "DR", 'Bretagne' as "DIR" FROM DUAL UNION ALL
	SELECT '151' as "CCD", 'Ouest' as "DR", 'Poitou Charentes' as "DIR" FROM DUAL UNION ALL
	SELECT '152' as "CCD", 'Ouest' as "DR", 'Poitou Charentes' as "DIR" FROM DUAL UNION ALL
	SELECT '154' as "CCD", 'Ouest' as "DR", 'Poitou Charentes' as "DIR" FROM DUAL UNION ALL
	SELECT '155' as "CCD", 'ACL' as "DR", 'Limousin Auvergne' as "DIR" FROM DUAL UNION ALL
	SELECT '161' as "CCD", 'SO' as "DR", 'Aquitaine Nord' as "DIR" FROM DUAL UNION ALL
	SELECT '162' as "CCD", 'SO' as "DR", 'Aquitaine Nord' as "DIR" FROM DUAL UNION ALL
	SELECT '163' as "CCD", 'SO' as "DR", 'Aquitaine Nord' as "DIR" FROM DUAL UNION ALL
	SELECT '164' as "CCD", 'SO' as "DR", 'Aquitaine Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '165' as "CCD", 'SO' as "DR", 'Aquitaine Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '171' as "CCD", 'ACL' as "DR", 'Auvergne' as "DIR" FROM DUAL UNION ALL
	SELECT '172' as "CCD", 'ACL' as "DR", 'Auvergne' as "DIR" FROM DUAL UNION ALL
	SELECT '173' as "CCD", 'ACL' as "DR", 'Auvergne' as "DIR" FROM DUAL UNION ALL
	SELECT '175' as "CCD", 'ACL' as "DR", 'Limousin Auvergne' as "DIR" FROM DUAL UNION ALL
	SELECT '176' as "CCD", 'ACL' as "DR", 'Centre' as "DIR" FROM DUAL UNION ALL
	SELECT '177' as "CCD", 'ACL' as "DR", 'Centre' as "DIR" FROM DUAL UNION ALL
	SELECT '179' as "CCD", 'ACL' as "DR", 'Auvergne' as "DIR" FROM DUAL UNION ALL
	SELECT '191' as "CCD", 'RAB' as "DR", 'Sillon Rhodanien' as "DIR" FROM DUAL UNION ALL
	SELECT '193' as "CCD", 'RAB' as "DR", 'Alpes' as "DIR" FROM DUAL UNION ALL
	SELECT '194' as "CCD", 'RAB' as "DR", 'Sillon Rhodanien' as "DIR" FROM DUAL UNION ALL
	SELECT '195' as "CCD", 'RAB' as "DR", 'Alpes' as "DIR" FROM DUAL UNION ALL
	SELECT '196' as "CCD", 'RAB' as "DR", 'Alpes' as "DIR" FROM DUAL UNION ALL
	SELECT '197' as "CCD", 'RAB' as "DR", 'Sillon Rhodanien' as "DIR" FROM DUAL UNION ALL
	SELECT '198' as "CCD", 'RAB' as "DR", 'Sillon Rhodanien' as "DIR" FROM DUAL UNION ALL
	SELECT '199' as "CCD", 'RAB' as "DR", 'Sillon Rhodanien' as "DIR" FROM DUAL UNION ALL
	SELECT '211' as "CCD", 'IDF' as "DR", 'IDF Ouest' as "DIR" FROM DUAL UNION ALL
	SELECT '212' as "CCD", 'IDF' as "DR", 'IDF Ouest' as "DIR" FROM DUAL UNION ALL
	SELECT '213' as "CCD", 'IDF' as "DR", 'IDF Ouest' as "DIR" FROM DUAL UNION ALL
	SELECT '214' as "CCD", 'IDF' as "DR", 'IDF Ouest' as "DIR" FROM DUAL UNION ALL
	SELECT '215' as "CCD", 'IDF' as "DR", 'IDF Ouest' as "DIR" FROM DUAL UNION ALL
	SELECT '221' as "CCD", 'IDF' as "DR", 'IDF Est' as "DIR" FROM DUAL UNION ALL
	SELECT '222' as "CCD", 'IDF' as "DR", 'IDF Est' as "DIR" FROM DUAL UNION ALL
	SELECT '223' as "CCD", 'IDF' as "DR", 'IDF Est' as "DIR" FROM DUAL UNION ALL
	SELECT '224' as "CCD", 'IDF' as "DR", 'IDF Est' as "DIR" FROM DUAL UNION ALL
	SELECT '225' as "CCD", 'IDF' as "DR", 'IDF Est' as "DIR" FROM DUAL UNION ALL
	SELECT '231' as "CCD", 'SO' as "DR", 'Midi Pyrenées Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '232' as "CCD", 'SO' as "DR", 'Midi Pyrenées Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '233' as "CCD", 'SO' as "DR", 'Midi Pyrenées Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '234' as "CCD", 'SO' as "DR", 'Midi Pyrenées Nord' as "DIR" FROM DUAL UNION ALL
	SELECT '235' as "CCD", 'SO' as "DR", 'Midi Pyrenées Nord' as "DIR" FROM DUAL UNION ALL
	SELECT '241' as "CCD", 'MED' as "DR", 'LARO' as "DIR" FROM DUAL UNION ALL
	SELECT '242' as "CCD", 'MED' as "DR", 'LARO' as "DIR" FROM DUAL UNION ALL
	SELECT '243' as "CCD", 'MED' as "DR", 'LARO' as "DIR" FROM DUAL UNION ALL
	SELECT '245' as "CCD", 'MED' as "DR", 'LARO' as "DIR" FROM DUAL UNION ALL
	SELECT '251' as "CCD", 'MED' as "DR", 'Provence Alpes du Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '252' as "CCD", 'MED' as "DR", 'Provence Alpes du Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '253' as "CCD", 'MED' as "DR", 'Cote d''Azur' as "DIR" FROM DUAL UNION ALL
	SELECT '254' as "CCD", 'MED' as "DR", 'Cote d''Azur' as "DIR" FROM DUAL UNION ALL
	SELECT '256' as "CCD", 'MED' as "DR", 'Provence Alpes du Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '258' as "CCD", 'MED' as "DR", 'Provence Alpes du Sud' as "DIR" FROM DUAL UNION ALL
	SELECT '259' as "CCD", 'MED' as "DR", 'Cote d''Azur' as "DIR" FROM DUAL
)

SELECT POINT, SI
, t.DR, t.DIR
FROM (
	SELECT prm.PRM_ID as POINT
	, SUBSTR(prm.PRM_ID, 1, 3) CCD
	, CASE WHEN prm.PRM_DG_APP_INSTANCE_SI IS NULL THEN 'DISCO' ELSE 'GINKO' END as SI
	FROM SGEL_PRM_SCH.T_PRM prm
	WHERE 1=1
	AND prm.PRM_SC_SEGMENT = 'C5'
	AND prm.PRM_ID IN @@IN1@@
) prm
LEFT JOIN t ON prm.CCD = t.CCD