SELECT POINT, PAS FROM
(
	SELECT pds.REFERENCE POINT
	, srv.LIBELLECOURT
	, substr(srv.LIBELLECOURT, 4, 2) as PAS
	, srvs.REFERENCE
	, srvs.STATUT
	, DECODE(srvs.STATUT,
		'0', 'souscription',
		'1', 'actif',
		'3', 'cessation',
		'4', 'cessé',
		'8', 'annulé',
		'inconnu') as STATUT
	, DENSE_RANK() OVER (PARTITION BY pds.REFERENCE ORDER BY srv.LIBELLECOURT, srvs.DATEEFFET DESC, srvs.REFERENCE DESC) as RANG
	FROM GAHFLD.TPOINTDESERVICE pds
	JOIN GAHFLD.TSERVICESOUSCRIT srvs ON pds.ID = srvs.POINTDESERVICE_ID
	JOIN GAHFLD.TSERVICE srv ON srvs.SERVICE_ID = srv.ID
	WHERE 1=1
	AND srvs.TYPEDEMANDEUR IS NOT NULL
	AND srv.LIBELLECOURT LIKE 'CDC%'
	AND srvs.STATUT IN ('0', '1')
	--AND pds.REFERENCE LIKE '211%'
	--AND pds.REFERENCE = '21128075229925'
)
WHERE RANG = 1