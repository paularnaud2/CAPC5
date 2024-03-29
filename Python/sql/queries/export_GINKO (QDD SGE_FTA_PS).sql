--SELECT *
SELECT POINT, FTA, PS
FROM
(
	SELECT pds.REFERENCE as POINT
		, DECODE(ctr.EXTRAITSERVICESSOUSCRIT
			, 'CUSDT', 'CUST'
			, 'MUADT', 'MUDT'
			, 'MUADT2', 'MUDT'
			, 'LUSDT', 'LU'
			, 'CUADT4', 'CU4'
			, 'MUADT4', 'MU4')as FTA
		, srv.PUISSANCESOUSCRITE1_VALUE as PS
		, DENSE_RANK() OVER (PARTITION BY pds.REFERENCE ORDER BY ctr.STATUTEXTRAIT, srv.STATUT) as RANG
	FROM GAHFLD.TESPACEDELIVRAISON edl
		JOIN GAHFLD.TPOINTDESERVICE pds ON edl.ID = pds.ESPACEDELIVRAISON_ID
		JOIN GAHFLD.CONTRAT_ESPACESDELIVRAISON ce ON edl.ID = ce.DEST
		JOIN GAHFLD.TCONTRAT ctr ON ce.SOURCE = ctr.ID
		JOIN GAHFLD.TSERVICESOUSCRIT srv ON ctr.ID = srv.CONTRAT_ID
	WHERE 1=1
		AND pds.ETAT <> '5'
		AND pds.DATESUPPRESSION IS NULL
		AND pds.REFERENCE NOT LIKE '000%'
		AND pds.NATURE = '1'
		AND ctr.DATEFIN IS NULL
		AND ctr.STATUTEXTRAIT IN ('1', '2', '3')
		AND ctr.EXTRAITSERVICESSOUSCRIT <> 'injection'
		AND srv.DATEFIN IS NULL
		AND srv.ROLE = 'com.hermes.crm.contrat.businessobject.ServiceSouscritAcheminementElecBTInf36'
		--AND ctr.EXTRAITSERVICESSOUSCRIT = 'LUSDT'
		--AND srv.USAGE = 'PARTSEC'
		--AND pds.REFERENCE IN ('09364978239832')
		AND pds.REFERENCE LIKE '211%'
		--AND ROWNUM < 11
)
WHERE RANG = '1'
AND FTA IS NOT NULL