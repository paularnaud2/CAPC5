--SELECT *
SELECT POINT
FROM
(
	SELECT pds.REFERENCE as POINT
		, DENSE_RANK() OVER (PARTITION BY pds.REFERENCE ORDER BY ctr.STATUTEXTRAIT, srv.STATUT) as RANG
		--, srv.ID ID_SRV, ctr.ID ID_CTR, paca.ID ID_PACA, cafo.ID ID_CAFO
		--, paca.*
	FROM GAHFLD.TESPACEDELIVRAISON edl
		JOIN GAHFLD.TPOINTDESERVICE pds ON edl.ID = pds.ESPACEDELIVRAISON_ID
		JOIN GAHFLD.CONTRAT_ESPACESDELIVRAISON ce ON edl.ID = ce.DEST
		JOIN GAHFLD.TCONTRAT ctr ON ce.SOURCE = ctr.ID
		JOIN GAHFLD.TSERVICESOUSCRIT srv ON ctr.ID = srv.CONTRAT_ID
	WHERE 1=1
		AND pds.ETAT <> '5'
		AND pds.DATESUPPRESSION IS NULL
		AND pds.REFERENCE NOT LIKE '000%'
		AND pds.NATURE = '2'
		AND ctr.DATEFIN IS NULL
		AND ctr.STATUTEXTRAIT IN ('1', '2', '3')
		AND ctr.EXTRAITSERVICESSOUSCRIT = 'injection'
		AND srv.DATEFIN IS NULL
		AND srv.ROLE = 'com.hermes.crm.contrat.businessobject.ServiceSouscritAcheminementElecBTInf36'
		--AND ctr.EXTRAITSERVICESSOUSCRIT = 'LUSDT'
		--AND srv.USAGE = 'PARTSEC'
		--AND pds.REFERENCE IN ('21154847994199', '21135889968033')
		--AND pds.REFERENCE LIKE '211%'
		--AND ROWNUM < 11
)
WHERE RANG = '1'