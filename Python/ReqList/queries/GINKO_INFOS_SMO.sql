SELECT POINT, TYPE_SRV_GINKO, DATE_DEBUT_GINKO, DATE_FIN_GINKO, TYPE_DEMANDEUR_GINKO
FROM
(
	SELECT pds.REFERENCE POINT, srv.LIBELLECOURT TYPE_SRV_GINKO, srvs.DATEDEBUTPREVUE DATE_DEBUT_GINKO, srvs.DATEFINPREVUE DATE_FIN_GINKO
	, DECODE (srvs.TYPEDEMANDEUR,
		 0, 'Fournisseur',
		 1, 'Fournisseur Tiers',
		 2, 'Client',
		 3, 'Interne',
		 4, 'Tiers autorisé',
		 srvs.TYPEDEMANDEUR
		) TYPE_DEMANDEUR_GINKO
	, DENSE_RANK() OVER (PARTITION BY pds.REFERENCE ORDER BY srv.LIBELLECOURT, srvs.DATEDEBUTPREVUE, srvs.TYPEDEMANDEUR) RANG
	FROM GAHFLD.TPOINTDESERVICE pds
	JOIN GAHFLD.TSERVICESOUSCRIT srvs ON pds.ID = srvs.POINTDESERVICE_ID
	JOIN GAHFLD.TSERVICE srv ON srvs.SERVICE_ID = srv.ID
	WHERE 1=1
	AND srvs.TYPEDEMANDEUR IS NOT NULL
	AND srv.LIBELLECOURT LIKE 'CDC%'
	AND srvs.DATEFIN IS NULL
	--AND pds.REFERENCE IN ('50092131995305', '01100144558519', '01100144564042', '50090976744268')
	--AND pds.REFERENCE = '01101157583189'
	AND pds.REFERENCE IN @@IN@@
)
WHERE RANG = 1