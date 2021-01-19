SELECT POINT, ETAT_ADAM, ID, DATE_DEBUT, DATE_FIN, PAS, TYPE FROM
(
	SELECT seg.PRM_ID POINT
	, SUBSTR(mes.PAS, 3, 2) as PAS
	, srv.SERVICE_ID ID
	, srv.SERVICE_TYPE TYPE
	, srv.ETAT_CODE ETAT_ADAM
	, srv.DATE_DEBUT
	, srv.DATE_FIN
	, DENSE_RANK() OVER (PARTITION BY seg.PRM_ID ORDER BY mes.PAS, srv.SERVICE_TYPE DESC, srv.ETAT_CODE, srv.DATE_DEBUT DESC, srv.SERVICE_ID DESC) as RANG
	FROM ADA_SCH.SERVICE_SOUSCRIT srv
	LEFT JOIN ADA_SCH.PRM_SEGMENT seg ON srv.PRM_SEGMENT_ID = seg.ID
	LEFT JOIN ADA_SCH.MESURE mes ON srv.MESURE_ID = mes.ID
	WHERE 1=1
	AND srv.ETAT_CODE IN ('ACTIF', 'DEMANDE')
	AND seg.SEGMENT = 'C5'
	AND srv.SERVICE_TYPE IN ('TRANSREC', 'CCDC')
	AND mes.TYPE_CODE = 'CDC'
	AND seg.PRM_ID IN @@IN@@
)
WHERE RANG = 1