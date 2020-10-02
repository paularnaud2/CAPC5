SELECT COUNT(*) VOL, TYPEPDS, ETAT, SOUSETAT, COUPE FROM(
	SELECT pds.REFERENCE as PDS
	, CASE
		WHEN pds.Nature = 2 THEN 'Producteur en Totalité'
		WHEN pds.ParticularitePDS = 1 THEN 'Producteur en Surplus'
		WHEN pds.Nature = 1 THEN 'Consommation'
		ELSE NULL
		END AS TypePDS
	, DECODE(pds.ETAT,
			  '1', 'ne peut être mis en service',
			  '3', 'hors service',
			  '4', 'en service',
			  '5', 'supprimé',
			  '12', 'non raccordable',
			  '13', 'raccordable',
			  'inconnu') as ETAT
	, DECODE(pds.SOUSETAT,
			  '1', 'actif',
			  '2', 'libre service',
			  '3', 'depose',
			  '4', 'debranche',
			  '5', 'debranche au branchement',
			  '6', 'sans objet',
			  '7', 'debranche au CCPI',
			  '8', 'organe compteur ouvert') as SOUSETAT
	, pds.COUPE
	FROM GAHFLD.TPOINTDESERVICE pds
	WHERE 1=1
	AND pds.ETAT <> '5'
	AND pds.DATESUPPRESSION IS NULL
	AND pds.REFERENCE NOT LIKE '000%'
	AND pds.NATURE = '1'
	AND ROWNUM <= 1000
)
GROUP BY TYPEPDS, ETAT, SOUSETAT, COUPE