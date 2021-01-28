SELECT app.site as DIR,centre.code as CENTRE, pds.reference as PDS, pds.dateprochainerelevereelle as DTR, compteur.Type_compteur
, mgzr.libelle as MARCHE , DECODE (mgzr.MODECOLLECTERELEVE, 0, 'circuit', 1, 'liste de points ', 2, 'PI') AS "MODE COLLECTE"
, trim(GEO.COMMUNE) as COMMUNE_EDL, trim(lpad(GEO.CODE_POSTAL,5,'0')) as CODE_POSTAL_EDL
------------------------------------------------------------------------------------------------------------------------
FROM GAHFLD.tpointdeservice pds 
CROSS JOIN gahfld.TAPPLICATIONINFO app
INNER JOIN GAHFLD.trolefunctionalunit rolef ON (rolef.item_id = pds.id AND MOD(pds.EtatObjet, 2) = 0 and rolef.unit_role='com.hermes.ref.unitefonctionnelle.businessobject.PortefeuillePDS' )
INNER JOIN GAHFLD.tmodegestionzonedereleve mgzr ON (mgzr.PORTEFEUILLEPDSZONEDERELEVE_ID = rolef.unit_ID AND MOD(mgzr.EtatObjet, 2) = 0 
                                                    and mgzr.DATEDEBUT < pds.dateprochainerelevereelle and (mgzr.DATEFIN is null or mgzr.DATEFIN > pds.dateprochainerelevereelle )
                                                    and mgzr.MODECOLLECTERELEVE=2)
INNER join gahfld.TESPACEDELIVRAISON EDL ON EDL.ID = PDS.ESPACEDELIVRAISON_ID and mod(EDL.ETATOBJET, 2) = 0                                                     
INNER JOIN GAHFLD.EDL_DECOUPAGETERRITOIRE edl_secteur ON (edl.ID = edl_secteur.SOURCE)
INNER JOIN GAHFLD.TDECOUPAGETERRITOIRE secteur ON (edl_secteur.DEST = secteur.ID  AND secteur.TYPEDECOUPAGETERRITOIRE = 1)
INNER JOIN GAHFLD.DECTERRITOIRE_DECTERRITOIRE secteur_centre ON (secteur.ID = secteur_centre.SOURCE)
INNER JOIN GAHFLD.TDECOUPAGETERRITOIRE centre ON (secteur_centre.DEST = centre.ID  AND centre.TYPEDECOUPAGETERRITOIRE = 2)
INNER JOIN GAHFLD.VRS_DONNEEGEOGRAPHIQUE geo ON edl.ADRESSE_ID = geo.ID
INNER JOIN ( SELECT pam.affectation_id , DECODE(cpt.Role, 'com.hermes.ref.materiel.businessobject.CompteurAMMBleu', 'Linky'
                    , 'com.hermes.ref.materiel.businessobject.CompteurElectronique', 'CBE'
                    , 'com.hermes.ref.materiel.businessobject.CompteurElectromecanique', 'CBEM'
                    , NULL, NULL, cpt.Role || '-INCONNU') AS Type_compteur
			FROM gahfld.TPERIODEDACTIVITE pam
			INNER JOIN gahfld.TMATERIEL m on (m.id = pam.Materiel_ID and m.typemateriel_role LIKE 'com.hermes.ref.materiel.businessobject.TypeDeCompteurElectrique%')
			INNER JOIN gahfld.TCOMPTEUR cpt ON (cpt.ID = m.ID AND cpt.Role = m.Role)
			Where pam.Affectation_Role = 'com.hermes.ref.edl.businessobject.PointDeServiceElectricite' and pam.dateheurefin is null
			) compteur on (compteur.affectation_id = pds.id)
---------------------------------------------------------------------------------------------------------------------------
where 1=1 
and mod(pds.etatobjet,2)=0
and pds.etat<>5
and pds.etat<>1
and pds.sousetat=1
and pds.NIVEAUCOMMUNICABILITEAMM='NONOUVERT'
and mgzr.libelle<>'Var'
and mgzr.libelle<>'Lot'
and mgzr.libelle<>'Tarn et Garonne'