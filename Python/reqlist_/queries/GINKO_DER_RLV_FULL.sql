SELECT * FROM
(
	SELECT /*+ PARALLEL(8) ORDERED */ pds.Reference "PDS"
	, CASE  WHEN pds.Nature = 2 THEN 'Producteur en Totalité'
					  WHEN pds.ParticularitePDS = 1 THEN 'Producteur en Surplus'
					  WHEN pds.Nature = 1 THEN 'Consommation'
					  ELSE NULL END AS TypePDS
	, TO_CHAR(rel.DateReleve, 'DD/MM/YYYY') "DateRelève"
	, TO_CHAR(rel.DateReleve, 'HH24:MI') "HeureRelève"
	, DECODE(rel.STATUTRELEVE,1,'valide', 2, 'invalide', 3, 'en cours de traitement', NULL, NULL, rel.STATUTRELEVE || '-INCONNU') AS statut_releve
	, DECODE(rel.FactureGRD, 0, 'NON Facturée', 1, 'Facturée') AS FactureGRD
	, DECODE(rel.TYPERELEVE, '1','récurrente', '21','de régularisation avec index', '22','de régularisation sans index', '3','sur événement') AS TYPERELEVE
	, DECODE(rel.TYPEEVENEMENT, '1','souscription', '11','reprise changement de fournisseur', '12','rectification', '13','mise en service', '14','mise hors service', '15','coupure pour non paiement', '16','prépose de matériel', '17','lecture d''index', '18','échange', '19','vérification', '2','cessation', '20','mesurage', '21','replombage', '22','dépose', '23','raccordement d''asservissement', '24','raccordement de téléreport', '25','mise à jour heure légale', '26','mise en service suite à coupure', '27','enquête', '28','contrôle qualité tension', '29','dépannage mise hors service', '3','modification contrat', '30','dépannage échange', '31','dépannage divers', '32','marche/arrêt chauffage', '33','intervention sur télérelève', '34','appel pompiers', '35','coupure technique', '36','réglage', '37','coupure absence relève', '38','fiabilisation', '39','Import base SI AMM', '4','reprise', '40','Limitation pour non paiement', '5','sans objet', '6','souscription libre service', '7','cessation libre service', '8','souscription changement de fournisseur', '9','cessation changement de fournisseur') AS TYPEEVENEMENT
	, DECODE(rel.NATURERELEVE, '1','réelle', '2','estimé suite à absence client', '3','estimé entre 2 relèves réelles', '4','absence à la relève', '5','estimé','6','evt réelle','41','avec idx réelle','42','avec idx estimée','51','sans idx réelle','52','sans idx estimée','7','absence relève','9','evt estimée') AS NATURERELEVE 
	, DECODE(rel.AUTORELEVE,0,'NON',1,'OUI') AS AUTORELEVE
	, LEAD (rel.DateReleve, 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Date Relève précédente"
	, LEAD (DECODE(rel.STATUTRELEVE,1,'valide', 2, 'invalide', 3, 'en cours de traitement', NULL, NULL, rel.STATUTRELEVE || '-INCONNU'), 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Statut Relève précédente"
	, LEAD (DECODE(rel.FactureGRD, 0, 'NON Facturée', 1, 'Facturée'), 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Relève précédente Facturé"
	, LEAD (DECODE(rel.TYPERELEVE, '1','récurrente', '21','de régularisation avec index', '22','de régularisation sans index', '3','sur événement'), 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Type Relève précédente"
	, LEAD (DECODE(rel.TYPEEVENEMENT, '1','souscription', '11','reprise changement de fournisseur', '12','rectification', '13','mise en service', '14','mise hors service', '15','coupure pour non paiement', '16','prépose de matériel', '17','lecture d''index', '18','échange', '19','vérification', '2','cessation', '20','mesurage', '21','replombage', '22','dépose', '23','raccordement d''asservissement', '24','raccordement de téléreport', '25','mise à jour heure légale', '26','mise en service suite à coupure', '27','enquête', '28','contrôle qualité tension', '29','dépannage mise hors service', '3','modification contrat', '30','dépannage échange', '31','dépannage divers', '32','marche/arrêt chauffage', '33','intervention sur télérelève', '34','appel pompiers', '35','coupure technique', '36','réglage', '37','coupure absence relève', '38','fiabilisation', '39','Import base SI AMM', '4','reprise', '40','Limitation pour non paiement', '5','sans objet', '6','souscription libre service', '7','cessation libre service', '8','souscription changement de fournisseur', '9','cessation changement de fournisseur'), 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Type Evé. Relève précédente"
	, LEAD (DECODE(rel.NATURERELEVE, '1','réelle', '2','estimé suite à absence client', '3','estimé entre 2 relèves réelles', '4','absence à la relève', '5','estimé','6','evt réelle','41','avec idx réelle','42','avec idx estimée','51','sans idx réelle','52','sans idx estimée','7','absence relève','9','evt estimée'), 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Nature Relève précédente"
	, LEAD (DECODE(rel.AUTORELEVE,0,'NON',1,'OUI'), 1) OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS "Autorelevé précédent"
	, gp.*
	--, prel.DateReleve, pgp.*
	, DENSE_RANK() OVER (PARTITION BY pds.ID ORDER BY pacm.DateDebut DESC NULLS LAST, rel.DateReleve DESC NULLS LAST) AS Rang
	FROM gahfld.TPOINTDESERVICE pds
	INNER JOIN gahfld.TPACM pacm ON (pacm.PointDeService_ID = pds.ID)
	--INNER JOIN gahfld.TCONFIGURATIONMATI
	LEFT JOIN gahfld.TRELEVE rel ON (rel.Pacm_ID = pacm.ID)
	LEFT JOIN
	(
		SELECT gpD.Releve_ID, COUNT(1) AS Total
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_D1', gpD.Valeur, NULL)) AS D1, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_D2', gpD.Valeur, NULL)) AS D2
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_D3', gpD.Valeur, NULL)) AS D3, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_D4', gpD.Valeur, NULL)) AS D4
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F1', gpD.Valeur, NULL)) AS F1, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F2', gpD.Valeur, NULL)) AS F2
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F3', gpD.Valeur, NULL)) AS F3, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F4', gpD.Valeur, NULL)) AS F4
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F6', gpD.Valeur, NULL)) AS F6, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F7', gpD.Valeur, NULL)) AS F7
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F8', gpD.Valeur, NULL)) AS F8, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F9', gpD.Valeur, NULL)) AS F9
		, MAX(DECODE(mgpD.Mnemo, 'IDX_EAS_F10', gpD.Valeur, NULL)) AS F10
		FROM gahfld.TMODELEGRANDEURPHYSIQUE mgpD --ON (gpD.Releve_ID = rel.ID AND )
		INNER JOIN gahfld.TGRANDEURPHYSIQUEGENERALE gpD ON (gpD.ModeleGrandeurPhysique_ID = mgpD.ID AND gpD.Role = 'G'  AND MOD(gpD.EtatObjet, 2) = 0)
		WHERE SUBSTR(mgpD.Mnemo, 1, 9) IN ('IDX_EAS_D', 'IDX_EAS_F')
		GROUP BY gpD.Releve_ID
	) gp ON (gp.Releve_ID = rel.ID)
	WHERE 1 = 1
	AND pds.Reference IN ('01485383451176')
)
WHERE d.Rang = 1;