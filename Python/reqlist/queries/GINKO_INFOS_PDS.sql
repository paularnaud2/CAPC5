--SELECT *
SELECT POINT
, DATE_DEBUT_SCN_GKO
, DATE_MODIF_GKO
--, FTA_GKO, PS_GKO
, FRN_GKO
FROM
(
	SELECT pds.REFERENCE as POINT
		, TO_CHAR(ctr.DATEEFFET, 'DD/MM/YYYY') DATE_DEBUT_SCN_GKO
		, TO_CHAR(pds.DATEMODIFICATION, 'DD/MM/YYYY') DATE_MODIF_GKO
		, SUBSTR(pds.PALIERTECHNIQUE, 4, 2)  P_RAC
		, DECODE(ctr.EXTRAITSERVICESSOUSCRIT
			, 'CUSDT', 'CUST'
			, 'MUADT', 'MUDT'
			, 'MUADT2', 'MUDT'
			, 'LUSDT', 'LU'
			, 'CUADT4', 'CU4'
			, 'MUADT4', 'MU4')as FTA_GKO
		, DECODE(ctr.STATUTEXTRAIT,
		  '0', 'en cours de souscription',
		  '1', 'actif',
		  '2', 'en cours de modification',
		  '3', 'en cours de cessation',
		  '4', 'cessé',
		  '5', 'cessation partielle',
		  '8', 'annulé',
		  'inconnu') as STATUT
		, REPLACE(srv.PUISSANCESOUSCRITE1_VALUE,'.',',') PS
		, act.NOM FRN_GKO
		, DENSE_RANK() OVER (PARTITION BY pds.REFERENCE ORDER BY ctr.STATUTEXTRAIT, srv.STATUT) as RANG
	FROM GAHFLD.TESPACEDELIVRAISON edl
		JOIN GAHFLD.TPOINTDESERVICE pds ON edl.ID = pds.ESPACEDELIVRAISON_ID
		JOIN GAHFLD.CONTRAT_ESPACESDELIVRAISON ce ON edl.ID = ce.DEST
		JOIN GAHFLD.TCONTRAT ctr ON ce.SOURCE = ctr.ID
		JOIN GAHFLD.TSERVICESOUSCRIT srv ON ctr.ID = srv.CONTRAT_ID
		LEFT JOIN GAHFLD.TROLE rol ON ctr.TITULAIRE_ID = rol.ID
		LEFT JOIN GAHFLD.TACTEUR act ON rol.ACTEUR_ID = act.ID
	WHERE 1=1
		AND pds.ETATOBJET = '0'
		AND pds.ETAT <> '5'
		AND pds.DATESUPPRESSION IS NULL
		AND pds.REFERENCE NOT LIKE '000%'
		AND pds.NATURE = '1'
		AND ctr.DATEFIN IS NULL
		AND ctr.STATUTEXTRAIT IN ('1', '2', '3')
		AND ctr.EXTRAITSERVICESSOUSCRIT <> 'injection'
		AND srv.DATEFIN IS NULL
		AND srv.ROLE = 'com.hermes.crm.contrat.businessobject.ServiceSouscritAcheminementElecBTInf36'
		AND pds.REFERENCE IN @@IN@@
		--AND pds.REFERENCE IN ('22234876949527', '22565412341065', '22452677208285', '21178002857066', '22118813260640', '21247177850967', '21241823422616', '21230680057978', '21573371796674', '22579305248513')
		--AND pds.REFERENCE LIKE '211%'
)
WHERE RANG = '1'