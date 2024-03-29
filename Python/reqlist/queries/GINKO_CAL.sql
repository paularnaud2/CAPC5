SELECT POINT, CAL_GKO FROM
(
	SELECT pds.REFERENCE as POINT
	, cafo.REFERENCE as CAL_GKO
	, paca.DATEFIN
	, DENSE_RANK() OVER (PARTITION BY pds.REFERENCE ORDER BY paca.DATEFIN DESC) RANG
	FROM GAHFLD.TPOINTDESERVICE pds
	LEFT JOIN GAHFLD.TPACM pacm ON pds.ID = pacm.POINTDESERVICE_ID
	LEFT JOIN GAHFLD.TPACALENDRIER paca ON paca.PACM_ID = pacm.ID 
	LEFT JOIN GAHFLD.TCALENDRIERDESCRIPTIF cafo on cafo.ID = paca.CALENDRIERFOURNISSEUR_ID
	WHERE 1=1
	AND cafo.REFERENCE IS NOT NULL
	AND paca.ETATOBJET = 0
	AND pds.REFERENCE IN @@IN@@
)
WHERE RANG = '1'