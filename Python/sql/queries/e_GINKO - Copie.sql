SELECT pds.REFERENCE as POINT,
srv.PUISSANCESOUSCRITE1_VALUE as PUISSANCE_SOUSCRITE_VALEUR,
act.NOM as FOURNISSEUR,
DECODE(pds.ETAT,
		  '1', 'ne peut être mis en service',
		  '3', 'hors service',
		  '4', 'en service',
      '5', 'supprimé',
		  '12', 'non raccordable',
		  '13', 'raccordable',
		  'inconnu') as ETAT_PRM,
CASE WHEN srv.USAGE LIKE '%PART%' THEN 'PART' ELSE 'PRO' END CAT_CLIENT,
DECODE(pds.nature, '1', 'consommation', '2', 'production', pds.nature) AS NATURE,
CASE CPT.ROLE
  WHEN 'com.hermes.ref.materiel.businessobject.CompteurAMMBleu' THEN 'Linky'
  WHEN 'com.hermes.ref.materiel.businessobject.CompteurElectronique' THEN 'CBE'
  wHEN 'com.hermes.ref.materiel.businessobject.CompteurElectromecanique' THEN 'Electromécanique'
  ELSE NULL
END AS TYPECOMPTEUR
FROM GAHFLD.TESPACEDELIVRAISON edl
JOIN GAHFLD.TPOINTDESERVICE pds ON edl.ID = pds.ESPACEDELIVRAISON_ID
	JOIN GAHFLD.CONTRAT_ESPACESDELIVRAISON ce ON edl.ID = ce.DEST
	JOIN GAHFLD.TCONTRAT ctr ON ce.SOURCE = ctr.ID
	INNER JOIN GAHFLD.TSERVICESOUSCRIT srv ON ctr.ID = srv.CONTRAT_ID
  INNER JOIN GAHFLD.TPERIODEDACTIVITE PAM ON (PAM.AFFECTATION_ID = PDS.ID AND PAM.AFFECTATION_ROLE = 'com.hermes.ref.edl.businessobject.PointDeServiceElectricite')
  INNER JOIN GAHFLD.TMATERIEL mat ON (mat.ID = PAM.MATERIEL_ID )
  INNER JOIN GAHFLD.TCOMPTEUR CPT ON (CPT.ID = mat.ID AND CPT.ROLE = mat.ROLE)
  LEFT JOIN GAHFLD.TROLE rol ON ctr.TITULAIRE_ID = rol.ID
	LEFT JOIN GAHFLD.TACTEUR act ON rol.ACTEUR_ID = act.ID
WHERE 1=1
  AND pds.DATESUPPRESSION IS NULL
  AND pds.REFERENCE NOT LIKE '000%'
  AND ctr.DATEFIN IS NULL
--AND pds.REFERENCE = '21422141681829'
