WITH 
	FUNCTION get_liste_jours_feries(annee NUMBER) RETURN VARCHAR2
    AS  
        jours_fixes VARCHAR2(100) := '''01/01'', ''01/05'', ''08/05'', ''14/07'', ''15/08'', ''01/11'', ''11/11'', ''25/12''';
        jours_mobiles VARCHAR2(100) := '';
        minute NUMBER;
        jour NUMBER;
        dimanche_paques DATE;
    BEGIN
        SELECT (extract (minute from (cast(trunc(sysdate) + numtodsinterval(24*60*60 * ((annee/38) - floor(annee/38)), 'second') AS TIMESTAMP)))) / 2 +56 AS minute INTO minute FROM dual;
        IF floor(minute) = 60 THEN
            minute := 29;
        ELSIF minute > 60 THEN
            minute := minute - 1;
        END IF;
        SELECT extract (DAY FROM date'1899-12-31' + numtodsinterval(minute, 'DAY') ) AS jour INTO jour FROM dual;
        SELECT next_day(to_date(to_char(jour) || '/05/' || to_char(annee), 'dd/MM/yyyy'), to_char(trunc(sysdate, 'iw')+5, 'DAY')) - 7 -interval '34' day AS jour INTO dimanche_paques FROM dual;
        jours_mobiles := jours_mobiles || ', ''' || to_char(dimanche_paques + interval '1' day, 'dd/MM') || '''';
        jours_mobiles := jours_mobiles || ', ''' || to_char(dimanche_paques + interval '39' day, 'dd/MM') || '''';
        jours_mobiles := jours_mobiles || ', ''' || to_char(dimanche_paques + interval '50' day, 'dd/MM') || '''';
        RETURN jours_fixes || jours_mobiles;
    END;
    
liste_jours_ouvres AS (SELECT /*+ RESULT_CACHE */ jour, est_ouvre, diff, nb_jours, nb_jours_ouvres FROM (
				SELECT jour, diff, est_ouvre, nb_jours,
		CASE WHEN (est_ouvre = 0) THEN (- SUM(est_ouvre) OVER (ORDER BY jour desc)) ELSE (- SUM(est_ouvre) OVER (ORDER BY jour desc)) + 1 END AS nb_jours_ouvres
        FROM (
            SELECT jour, diff, nb_jours,
            CASE WHEN (1 + trunc(jour) - trunc(jour, 'IW') IN (6, 7) OR  get_liste_jours_feries(extract (year from jour)) LIKE '%' || to_char(trunc(jour), 'dd/MM') || '%') THEN 0 ELSE 1 END AS est_ouvre
            FROM (
                SELECT add_months(trunc(sysdate), -6) + level AS jour,
                (add_months(trunc(sysdate),-6) + level) - trunc(sysdate) AS diff,
                1-ROW_NUMBER() OVER (ORDER BY level desc) AS nb_jours
                FROM dual
                CONNECT BY level < trunc(sysdate) - add_months(trunc(sysdate),-6) + 1
            )
        )
				UNION
				SELECT jour, diff, est_ouvre, nb_jours,
		(SUM(jour_a_compter) OVER (ORDER BY jour)) AS nb_jours_ouvres
        FROM (
			SELECT jour, diff, est_ouvre, nb_jours,
			CASE WHEN (diff = 0) THEN 0 ELSE est_ouvre END AS jour_a_compter
			FROM (
				SELECT jour, diff, nb_jours,
				CASE WHEN (1 + trunc(jour) - trunc(jour, 'IW') IN (6, 7) OR get_liste_jours_feries(extract (year from jour)) LIKE '%' || to_char(trunc(jour), 'dd/MM') || '%') THEN 0 ELSE 1 END AS est_ouvre
				FROM (
					SELECT add_months(trunc(sysdate), +12) - level as jour,
					add_months(trunc(sysdate), 12) - level - trunc(sysdate) AS diff,
					ROW_NUMBER() OVER (ORDER BY level desc) - 1 AS nb_jours
					FROM dual
					CONNECT BY level < add_months(trunc(sysdate),12) + 1 -  trunc(sysdate)
				)
			)
        )
        
			) t0
			ORDER BY jour desc),
hierarchie_geo AS (
SELECT /*+ INLINE */ ID, ETATOBJET, RANG, TYPEDONNEEGEO, LIBELLE, NUMERO_COMPLEMENT, CODE_HIERARCHIE, MNEMONIQUE_HIERARCHIE, LIBELLE_HIERARCHIE, LIBELLEABREGE_HIERARCHIE, CODEINSEE_HIERARCHIE, MATRICULEVOIE_HIERARCHIE, RANG_HIERARCHIE, TYPEDONNEEGEO_HIERARCHIE, COMPLEMENTNUMERO_HIERARCHIE, TYPEDG_HIERARCHIE, CP_ID_HIERARCHIE, CP_HIERARCHIE, QUALITEDG_HIERARCHIE,
length(hgeo.LIBELLE_HIERARCHIE) - length(replace(hgeo.LIBELLE_HIERARCHIE, '|', null)) AS no_niveau
FROM gahfld.MV_BATCH_HIERARCHIE_DGEO hgeo
WHERE rang = 6),
edp_campagnes_en_cours_cat AS (SELECT t4.id_campagne, t4.id_edp_releve, t4.id_releve, t4."Date théorique relève", t4."Campagne", t4."Statut Campagne", t4."Communicant", t4."Technologie Compteur", t4.Instance, t4.code, t4.DR, t4."Libellé zone relève", t4."Date fin réelle échéance", t4."Date théorique proch. relève", t4."Statut EDP Relève", t4."ACR", t4."Date fin prévue échéance", t4."Statut Relève", t4.message_id, t4."Date déb. mode gest. zone rel.", t4."Date fin mode gest. zone rel.", t4.rang_pacm_desc, t4."Référence relève", t4."Référence PDS", t4."Accès compteur", t4."Numéro voie edl", t4."Complé de localisation edl", t4."Type voie edl", t4."Voie edl", t4."Commune edl", t4."Code postal edl", t4."Code INSEE", t4."Lot", t4."Mode collecte relève", t4."Libellé prestataire", t4."Référence prestataire", t4."Date relève programmée", t4."Ecart DTR-auj. en jours cal.", t4."Ecart DTR-auj. en jours ouvrés", t4.ecart_aujourd_hui_proch_DTR_jo, t4.type_date, t4.rang_dtr_depasse, t4.rang_dtr_a_venir, t4.rang_dtr_depasse_unqmt, t4.rang_dtr_a_venir_unqmt, t4.num_categorie, CASE WHEN (num_categorie < -1) THEN 'DTR plus suivie'
        WHEN (num_categorie = -1) THEN '5ème DTR (8 jo dépassés)'
        WHEN (num_categorie = 1) THEN '4ème DTR'
        WHEN (num_categorie = 2) THEN '3ème DTR'
        WHEN (num_categorie = 3) THEN '2ème DTR'
        WHEN (num_categorie = 4) THEN '1ère DTR'
        WHEN (num_categorie > 4) THEN 'DTR à venir'
        ELSE null END
         AS categorie_ecart_auj_DTR_jo, CASE WHEN (num_categorie < -1) THEN to_date('01/01/0001', 'dd/MM/yyyy')
        WHEN (num_categorie > 4) THEN to_date('31/12/9999', 'dd/MM/yyyy')
        ELSE "Date théorique relève" END
         AS date_cat_ecart_auj_DTR_jo
            FROM (SELECT t3.id_campagne, t3.id_edp_releve, t3.id_releve, t3."Date théorique relève", t3."Campagne", t3."Statut Campagne", t3."Communicant", t3."Technologie Compteur", t3.Instance, t3.code, t3.DR, t3."Libellé zone relève", t3."Date fin réelle échéance", t3."Date théorique proch. relève", t3."Statut EDP Relève", t3."ACR", t3."Date fin prévue échéance", t3."Statut Relève", t3.message_id, t3."Date déb. mode gest. zone rel.", t3."Date fin mode gest. zone rel.", t3.rang_pacm_desc, t3."Référence relève", t3."Référence PDS", t3."Accès compteur", t3."Numéro voie edl", t3."Complé de localisation edl", t3."Type voie edl", t3."Voie edl", t3."Commune edl", t3."Code postal edl", t3."Code INSEE", t3."Lot", t3."Mode collecte relève", t3."Libellé prestataire", t3."Référence prestataire", t3."Date relève programmée", t3."Ecart DTR-auj. en jours cal.", t3."Ecart DTR-auj. en jours ouvrés", t3.ecart_aujourd_hui_proch_DTR_jo, t3.type_date, t3.rang_dtr_depasse, t3.rang_dtr_a_venir, t3.rang_dtr_depasse_unqmt, t3.rang_dtr_a_venir_unqmt, coalesce(rang_dtr_a_venir_unqmt, - rang_dtr_depasse_unqmt) AS num_categorie
            FROM (SELECT t2.id_campagne, t2.id_edp_releve, t2.id_releve, t2."Date théorique relève", t2."Campagne", t2."Statut Campagne", t2."Communicant", t2."Technologie Compteur", t2.Instance, t2.code, t2.DR, t2."Libellé zone relève", t2."Date fin réelle échéance", t2."Date théorique proch. relève", t2."Statut EDP Relève", t2."ACR", t2."Date fin prévue échéance", t2."Statut Relève", t2.message_id, t2."Date déb. mode gest. zone rel.", t2."Date fin mode gest. zone rel.", t2.rang_pacm_desc, t2."Référence relève", t2."Référence PDS", t2."Accès compteur", t2."Numéro voie edl", t2."Complé de localisation edl", t2."Type voie edl", t2."Voie edl", t2."Commune edl", t2."Code postal edl", t2."Code INSEE", t2."Lot", t2."Mode collecte relève", t2."Libellé prestataire", t2."Référence prestataire", t2."Date relève programmée", t2."Ecart DTR-auj. en jours cal.", t2."Ecart DTR-auj. en jours ouvrés", t2.ecart_aujourd_hui_proch_DTR_jo, t2.type_date, t2.rang_dtr_depasse, t2.rang_dtr_a_venir, CASE WHEN (type_date = 'depasse') THEN rang_dtr_depasse ELSE null END AS rang_dtr_depasse_unqmt, CASE WHEN (type_date = 'non depasse') THEN rang_dtr_a_venir ELSE null END AS rang_dtr_a_venir_unqmt
            FROM (SELECT t1.id_campagne, t1.id_edp_releve, t1.id_releve, t1."Date théorique relève", t1."Campagne", t1."Statut Campagne", t1."Communicant", t1."Technologie Compteur", t1.Instance, t1.code, t1.DR, t1."Libellé zone relève", t1."Date fin réelle échéance", t1."Date théorique proch. relève", t1."Statut EDP Relève", t1."ACR", t1."Date fin prévue échéance", t1."Statut Relève", t1.message_id, t1."Date déb. mode gest. zone rel.", t1."Date fin mode gest. zone rel.", t1.rang_pacm_desc, t1."Référence relève", t1."Référence PDS", t1."Accès compteur", t1."Numéro voie edl", t1."Complé de localisation edl", t1."Type voie edl", t1."Voie edl", t1."Commune edl", t1."Code postal edl", t1."Code INSEE", t1."Lot", t1."Mode collecte relève", t1."Libellé prestataire", t1."Référence prestataire", t1."Date relève programmée", t1."Ecart DTR-auj. en jours cal.", t1."Ecart DTR-auj. en jours ouvrés", t1.ecart_aujourd_hui_proch_DTR_jo, t1.type_date, DENSE_RANK() OVER (PARTITION BY type_date ORDER BY "Date théorique relève" DESC) AS rang_dtr_depasse, DENSE_RANK() OVER (PARTITION BY type_date ORDER BY "Date théorique relève") AS rang_dtr_a_venir
                FROM (SELECT t0.id_campagne, t0.id_edp_releve, t0.id_releve, t0."Date théorique relève", t0."Campagne", t0."Statut Campagne", t0."Communicant", t0."Technologie Compteur", t0.Instance, t0.code, t0.DR, t0."Libellé zone relève", t0."Date fin réelle échéance", t0."Date théorique proch. relève", t0."Statut EDP Relève", t0."ACR", t0."Date fin prévue échéance", t0."Statut Relève", t0.message_id, t0."Date déb. mode gest. zone rel.", t0."Date fin mode gest. zone rel.", t0.rang_pacm_desc, t0."Référence relève", t0."Référence PDS", t0."Accès compteur", t0."Numéro voie edl", t0."Complé de localisation edl", t0."Type voie edl", t0."Voie edl", t0."Commune edl", t0."Code postal edl", t0."Code INSEE", t0."Lot", t0."Mode collecte relève", t0."Libellé prestataire", t0."Référence prestataire", t0."Date relève programmée", t0."Ecart DTR-auj. en jours cal.", t0."Ecart DTR-auj. en jours ouvrés", t0.ecart_aujourd_hui_proch_DTR_jo, CASE WHEN ("Ecart DTR-auj. en jours ouvrés" < -8) THEN 'depasse' ELSE 'non depasse' END AS type_date
                FROM (SELECT id_campagne, id_edp_releve, id_releve, "Date théorique relève", "Campagne", "Statut Campagne", "Communicant", "Technologie Compteur", Instance, code, DR, "Libellé zone relève", "Date fin réelle échéance", "Date théorique proch. relève", "Statut EDP Relève", "ACR", "Date fin prévue échéance", "Statut Relève", message_id, "Date déb. mode gest. zone rel.", "Date fin mode gest. zone rel.", rang_pacm_desc, "Référence relève", "Référence PDS", "Accès compteur", "Numéro voie edl", "Complé de localisation edl", "Type voie edl", "Voie edl", "Commune edl", "Code postal edl", "Code INSEE", "Lot", "Mode collecte relève", "Libellé prestataire", "Référence prestataire", "Date relève programmée",
                    
	(trunc("Date théorique relève") - trunc(sysdate)) AS "Ecart DTR-auj. en jours cal.", (SELECT nb_jours_ouvres FROM liste_jours_ouvres WHERE jour = "Date théorique relève") AS "Ecart DTR-auj. en jours ouvrés", (SELECT nb_jours_ouvres FROM liste_jours_ouvres WHERE jour = "Date théorique proch. relève") AS ecart_aujourd_hui_proch_DTR_jo
                    FROM (SELECT /*+ PARALLEL(8) LEADING(lot, campagne, echeance, edp_releve, pds, paacr, acr, modele_acr, donnees_prog) USE_NL(edp_releve pds) PUSH_PRED(donnees_prog) */
             campagne.ID AS id_campagne, edp_releve.ID AS id_edp_releve, releve.ID AS id_releve, CASE WHEN (lot.MODELEDELOT_ROLE = 'com.hermes.itv.releve.businessobject.ModeleDeLotDeReleveParTSP') THEN
			echeance.DATEEXECUTIONPREVUE + 18
		ELSE
			echeance.DATEEXECUTIONPREVUE + 2
		END AS "Date théorique relève", campagne.LIBELLE AS "Campagne", DECODE(campagne.STATUT, 0, 'en cours',
		1, 'fermé',
		2, 'annulé',
		3, 'suspendu',
		4, 'suppression en cours',
		'inconnu') AS "Statut Campagne", CASE WHEN (config_materielle.TECHNOLOGIE = 5 AND pds.NIVEAUCOMMUNICABILITEAMM IN ('OUVERT', 'OUVERTNIV1', 'OUVERTNIV2')) THEN 'Communicant' ELSE 'Non Communicant' END AS "Communicant", CASE config_materielle.TECHNOLOGIE
WHEN 1 THEN
		'CBE'
WHEN 2 THEN
		'CBEM'
WHEN 5 THEN
		CASE WHEN pds.NIVEAUCOMMUNICABILITEAMM IN ('OUVERT', 'OUVERTNIV1', 'OUVERTNIV2') THEN
			'LKY C'
		ELSE
			'LKY NC'
		END
ELSE
		'autre'
END AS "Technologie Compteur", decode(dir.CODE, '0328', 'ACL','0323','EST','0321','IDF','0325','MED', '0322', 'MMN',
				'0327', 'OUE', '0324', 'RAB', '0326', 'SUO', 'autre') AS Instance, dr.CODE AS code, substr(dr.LIBELLE, 20) AS DR, mode_gestion_zone_releve.LIBELLE AS "Libellé zone relève", echeance.DATEFINREELLE AS "Date fin réelle échéance", pds.DATEPROCHAINERELEVEREELLE AS "Date théorique proch. relève", DECODE(edp_releve.STATUT,
		0, 'sélectionné',
		1, 'écarté',
		2, 'en cours relève',
		3, 'relevé',
		4, 'absent relève',
		8, 'absent relève technique',
		5, 'traité',
		6, 'à estimer',
		7, 'estimé',
		10, 'complément à estimer',
		11, 'relevé et estimé complémentaire',
		999, 'mis en lot d’isolés') AS "Statut EDP Relève", acr.LIBELLE AS "ACR", echeance.DATEFINPREVUE AS "Date fin prévue échéance", DECODE(releve.STATUTRELEVE,
1, 'valide',
2, 'invalide',
3, 'En cours de traitement') AS "Statut Relève", edp_releve.MESSAGE_ID AS message_id, mode_gestion_zone_releve.DATEDEBUT AS "Date déb. mode gest. zone rel.", mode_gestion_zone_releve.DATEFIN AS "Date fin mode gest. zone rel.", DENSE_RANK() OVER (PARTITION BY pds.ID ORDER BY pacm.DATEFIN DESC, pacm.DATEDEBUT DESC, pacm.STATUTVALIDE DESC) AS rang_pacm_desc, '032'||substr(dr.CODE, 3, 1)||'_'||releve.ID AS "Référence relève", pds.REFERENCE AS "Référence PDS", decode(pds.COMPTEURACCESSIBLE,
    0, 'non', 1, 'oui') AS "Accès compteur", replace(reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1) , instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 2) )), '|', '') AS "Numéro voie edl", replace(replace(hgeo.COMPLEMENTNUMERO_HIERARCHIE, '|', ''), 'VIDE', '') AS "Complé de localisation edl", replace(replace(hgeo.TYPEDONNEEGEO_HIERARCHIE, '-', ''), 'VIDE', '') AS "Type voie edl", reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 2) + 1, (instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 3) - instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 2) -1))) AS "Voie edl", CASE WHEN (no_niveau = 6) THEN
        reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 3) + 1, (instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 4) - instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 3) -1)))
    ELSE
        reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 4) + 1, (instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 5) - instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 4) -1)))
    END AS "Commune edl", replace(replace(hgeo.CP_HIERARCHIE, '-', ''), 'VIDE', '') AS "Code postal edl", substr(replace(replace(hgeo.CODEINSEE_HIERARCHIE, '-', ''), 'VIDE', ''), 1, 5) AS "Code INSEE", lot.LIBELLE AS "Lot", mode_gestion_zone_releve.MODECOLLECTERELEVE AS "Mode collecte relève", mode_gestion_zone_releve.REFERENCEPRESTATAIRE AS "Libellé prestataire", mode_gestion_zone_releve.REFERENCEMARCHEPRESTATAIRE AS "Référence prestataire", donnees_prog."Date relève programmée"
            FROM gahfld.TELEMENTDEPOPULATIONRELEVE edp_releve
JOIN gahfld.TPOINTDESERVICE pds ON edp_releve.POINTDESERVICE_ID = pds.ID
  AND mod(pds.ETATOBJET,2) = 0
JOIN gahfld.TLOT lot ON edp_releve.LOT_ID = lot.ID
  AND mod(edp_releve.ETATOBJET,2) = 0
JOIN gahfld.TCAMPAGNE campagne ON lot.CAMPAGNE_ID = campagne.ID
  AND mod(campagne.ETATOBJET,2) = 0
JOIN gahfld.TECHEANCE echeance ON campagne.ECHEANCEDECLENCHEE_ID = echeance.ID
  AND mod(echeance.ETATOBJET,2) = 0
JOIN gahfld.TPAABONNEMENTCYCLIQUERELEVE paacr ON pds.ID = paacr.POINTDESERVICE_ID
  AND paacr.ETATPERIODEACTIVITEACR = 1
  AND mod(paacr.ETATOBJET,2) = 0
JOIN gahfld.TABONNEMENTCYCLIQUERELEVE acr ON paacr.ABONNEMENTCYCLIQUERELEVE_ID = acr.ID
  AND mod(paacr.ETATOBJET,2) = 0
JOIN gahfld.TMODELEACR modele_acr ON acr.MODELEACR_ID = modele_acr.ID
  AND modele_acr.TYPE = 0
JOIN gahfld.TPACM pacm ON pds.ID = pacm.POINTDESERVICE_ID
JOIN gahfld.TCONFIGURATIONMATERIELLE config_materielle ON pacm.CONFIGURATIONMATERIELLE_ID = config_materielle.ID
  AND mod(pacm.ETATOBJET,2) = 0
JOIN gahfld.TESPACEDELIVRAISON edl ON pds.ESPACEDELIVRAISON_ID = edl.ID
JOIN gahfld.EDL_DECOUPAGETERRITOIRE edl_dr ON edl.ID = edl_dr.SOURCE
JOIN gahfld.TDECOUPAGETERRITOIRE dr ON edl_dr.DEST = dr.ID
  AND mod(dr.ETATOBJET,2) = 0
  AND dr.TYPEDECOUPAGETERRITOIRE = 3
  AND dr.CODE = dr.CODE
JOIN gahfld.DECTERRITOIRE_DECTERRITOIRE dr_dir ON dr.ID = dr_dir.SOURCE
JOIN gahfld.TDECOUPAGETERRITOIRE dir ON dr_dir.DEST = dir.ID
JOIN gahfld.TROLEFUNCTIONALUNIT role_unite_fonctionnelle ON pds.ID = role_unite_fonctionnelle.ITEM_ID
JOIN gahfld.TMODEGESTIONZONEDERELEVE mode_gestion_zone_releve ON role_unite_fonctionnelle.UNIT_ID = mode_gestion_zone_releve.PORTEFEUILLEPDSZONEDERELEVE_ID
  AND mod(mode_gestion_zone_releve.ETATOBJET,2) = 0
LEFT JOIN gahfld.TRELEVE releve ON edp_releve.RELEVE_ID = releve.ID
  AND mod(releve.ETATOBJET,2) = 0
LEFT JOIN (SELECT /*+ LEADING(pds) USE_NL(pds edp_wkf donnees_prog_releve) */ pds.ID AS id_pds, edp_wkf.OBJETTRAITE_ID AS objettraite_id, donnees_prog_releve.DATERELEVEPROGRAMMEE AS "Date relève programmée", donnees_prog_releve.HEUREDEBUTPLAGEPASSAGERELEVEUR AS "Heure déb. plage passage relv", donnees_prog_releve.HEUREFINPLAGEPASSAGERELEVEUR AS "Heure fin plage passage relv", edp_wkf.ETATOBJET AS etatobjet
FROM gahfld.TPOINTDESERVICE pds
JOIN gahfld.TELEMENTDEPOPULATIONWKF edp_wkf ON pds.ID = edp_wkf.OBJETTRAITE_ID
  AND mod(pds.ETATOBJET,2) = 0
  AND mod(edp_wkf.ETATOBJET,2) = 0
JOIN gahfld.TDONNEESPROGRAMMATIONRELEVE donnees_prog_releve ON edp_wkf.OBJETCONNEXE_ID = donnees_prog_releve.ID) donnees_prog ON pds.ID = donnees_prog.id_pds
LEFT JOIN hierarchie_geo hgeo ON edl.ADRESSE_ID = hgeo.id
            WHERE (lot.MODELEDELOT_ROLE = 'com.hermes.itv.releve.businessobject.ModeleDeLotDeReleveParTSP')
            AND mode_gestion_zone_releve.MODECOLLECTERELEVE = 0
            AND 
	(CASE WHEN (campagne.STATUT = 0) THEN 1
	 ELSE
		CASE WHEN (campagne.STATUT = 1) THEN
			CASE WHEN (trunc(sysdate) - trunc(echeance.DATEFINPREVUE) <= 100 ) THEN
				1
			ELSE
				0
			END
		ELSE
			0
		END
	END) = 1
            AND dr.CODE = dr.code) edp_base
                    WHERE rang_pacm_desc = 1
                    AND "Date théorique relève" >= nvl("Date déb. mode gest. zone rel.", to_date('01/01/0001', 'dd/MM/yyyy'))
                    AND "Date théorique relève" < nvl("Date fin mode gest. zone rel.", to_date('31/12/9999', 'dd/MM/yyyy'))) t0
                WHERE 
	(CASE WHEN ("Communicant" = 'Communicant') THEN 1 ELSE CASE WHEN (ecart_aujourd_hui_proch_DTR_jo > 41) THEN
		1
	ELSE
		0
	END END) = 1
            ) t1
            ) t2
            ) t3
            ) t4
			),
groupe_dates_repasse AS (SELECT categorie_ecart_auj_DTR_jo,
            LISTAGG(date_cat_ecart_auj_DTR_jo, ', ') WITHIN GROUP (ORDER BY date_cat_ecart_auj_DTR_jo) AS date_DTR_jo_agg
            FROM (
                SELECT DISTINCT categorie_ecart_auj_DTR_jo, date_cat_ecart_auj_DTR_jo
                FROM edp_campagnes_en_cours_cat edps
            )
            GROUP BY categorie_ecart_auj_DTR_jo
            ),
edp_campagnes_en_cours AS (SELECT edp_campagnes_en_cours_cat.*, groupe_dates_repasse.date_DTR_jo_agg
            FROM edp_campagnes_en_cours_cat
JOIN groupe_dates_repasse ON edp_campagnes_en_cours_cat.categorie_ecart_auj_DTR_jo = groupe_dates_repasse.categorie_ecart_auj_DTR_jo
            ),
edp_isoles_camp_en_cours_cat AS (SELECT t4.id_campagne, t4.id_edp_releve, t4.id_releve, t4."Date théorique relève", t4."Campagne", t4."Statut Campagne", t4."Communicant", t4."Technologie Compteur", t4.Instance, t4.code, t4.DR, t4."Libellé zone relève", t4."Date fin réelle échéance", t4."Date théorique proch. relève", t4."Statut EDP Relève", t4."ACR", t4."Date fin prévue échéance", t4."Statut Relève", t4.message_id, t4."Date déb. mode gest. zone rel.", t4."Date fin mode gest. zone rel.", t4.rang_pacm_desc, t4."Référence relève", t4."Référence PDS", t4."Accès compteur", t4."Numéro voie edl", t4."Complé de localisation edl", t4."Type voie edl", t4."Voie edl", t4."Commune edl", t4."Code postal edl", t4."Code INSEE", t4."Lot", t4."Mode collecte relève", t4."Libellé prestataire", t4."Référence prestataire", t4."Date relève programmée", t4."Ecart DTR-auj. en jours cal.", t4."Ecart DTR-auj. en jours ouvrés", t4.ecart_aujourd_hui_proch_DTR_jo, t4.type_date, t4.rang_dtr_depasse, t4.rang_dtr_a_venir, t4.rang_dtr_depasse_unqmt, t4.rang_dtr_a_venir_unqmt, t4.num_categorie, CASE WHEN (num_categorie < -1) THEN 'DTR plus suivie'
        WHEN (num_categorie = -1) THEN '5ème DTR (8 jo dépassés)'
        WHEN (num_categorie = 1) THEN '4ème DTR'
        WHEN (num_categorie = 2) THEN '3ème DTR'
        WHEN (num_categorie = 3) THEN '2ème DTR'
        WHEN (num_categorie = 4) THEN '1ère DTR'
        WHEN (num_categorie > 4) THEN 'DTR à venir'
        ELSE null END
         AS categorie_ecart_auj_DTR_jo, CASE WHEN (num_categorie < -1) THEN to_date('01/01/0001', 'dd/MM/yyyy')
        WHEN (num_categorie > 4) THEN to_date('31/12/9999', 'dd/MM/yyyy')
        ELSE "Date théorique relève" END
         AS date_cat_ecart_auj_DTR_jo
            FROM (SELECT t3.id_campagne, t3.id_edp_releve, t3.id_releve, t3."Date théorique relève", t3."Campagne", t3."Statut Campagne", t3."Communicant", t3."Technologie Compteur", t3.Instance, t3.code, t3.DR, t3."Libellé zone relève", t3."Date fin réelle échéance", t3."Date théorique proch. relève", t3."Statut EDP Relève", t3."ACR", t3."Date fin prévue échéance", t3."Statut Relève", t3.message_id, t3."Date déb. mode gest. zone rel.", t3."Date fin mode gest. zone rel.", t3.rang_pacm_desc, t3."Référence relève", t3."Référence PDS", t3."Accès compteur", t3."Numéro voie edl", t3."Complé de localisation edl", t3."Type voie edl", t3."Voie edl", t3."Commune edl", t3."Code postal edl", t3."Code INSEE", t3."Lot", t3."Mode collecte relève", t3."Libellé prestataire", t3."Référence prestataire", t3."Date relève programmée", t3."Ecart DTR-auj. en jours cal.", t3."Ecart DTR-auj. en jours ouvrés", t3.ecart_aujourd_hui_proch_DTR_jo, t3.type_date, t3.rang_dtr_depasse, t3.rang_dtr_a_venir, t3.rang_dtr_depasse_unqmt, t3.rang_dtr_a_venir_unqmt, coalesce(rang_dtr_a_venir_unqmt, - rang_dtr_depasse_unqmt) AS num_categorie
            FROM (SELECT t2.id_campagne, t2.id_edp_releve, t2.id_releve, t2."Date théorique relève", t2."Campagne", t2."Statut Campagne", t2."Communicant", t2."Technologie Compteur", t2.Instance, t2.code, t2.DR, t2."Libellé zone relève", t2."Date fin réelle échéance", t2."Date théorique proch. relève", t2."Statut EDP Relève", t2."ACR", t2."Date fin prévue échéance", t2."Statut Relève", t2.message_id, t2."Date déb. mode gest. zone rel.", t2."Date fin mode gest. zone rel.", t2.rang_pacm_desc, t2."Référence relève", t2."Référence PDS", t2."Accès compteur", t2."Numéro voie edl", t2."Complé de localisation edl", t2."Type voie edl", t2."Voie edl", t2."Commune edl", t2."Code postal edl", t2."Code INSEE", t2."Lot", t2."Mode collecte relève", t2."Libellé prestataire", t2."Référence prestataire", t2."Date relève programmée", t2."Ecart DTR-auj. en jours cal.", t2."Ecart DTR-auj. en jours ouvrés", t2.ecart_aujourd_hui_proch_DTR_jo, t2.type_date, t2.rang_dtr_depasse, t2.rang_dtr_a_venir, CASE WHEN (type_date = 'depasse') THEN rang_dtr_depasse ELSE null END AS rang_dtr_depasse_unqmt, CASE WHEN (type_date = 'non depasse') THEN rang_dtr_a_venir ELSE null END AS rang_dtr_a_venir_unqmt
            FROM (SELECT t1.id_campagne, t1.id_edp_releve, t1.id_releve, t1."Date théorique relève", t1."Campagne", t1."Statut Campagne", t1."Communicant", t1."Technologie Compteur", t1.Instance, t1.code, t1.DR, t1."Libellé zone relève", t1."Date fin réelle échéance", t1."Date théorique proch. relève", t1."Statut EDP Relève", t1."ACR", t1."Date fin prévue échéance", t1."Statut Relève", t1.message_id, t1."Date déb. mode gest. zone rel.", t1."Date fin mode gest. zone rel.", t1.rang_pacm_desc, t1."Référence relève", t1."Référence PDS", t1."Accès compteur", t1."Numéro voie edl", t1."Complé de localisation edl", t1."Type voie edl", t1."Voie edl", t1."Commune edl", t1."Code postal edl", t1."Code INSEE", t1."Lot", t1."Mode collecte relève", t1."Libellé prestataire", t1."Référence prestataire", t1."Date relève programmée", t1."Ecart DTR-auj. en jours cal.", t1."Ecart DTR-auj. en jours ouvrés", t1.ecart_aujourd_hui_proch_DTR_jo, t1.type_date, DENSE_RANK() OVER (PARTITION BY type_date ORDER BY "Date théorique relève" DESC) AS rang_dtr_depasse, DENSE_RANK() OVER (PARTITION BY type_date ORDER BY "Date théorique relève") AS rang_dtr_a_venir
                FROM (SELECT t0.id_campagne, t0.id_edp_releve, t0.id_releve, t0."Date théorique relève", t0."Campagne", t0."Statut Campagne", t0."Communicant", t0."Technologie Compteur", t0.Instance, t0.code, t0.DR, t0."Libellé zone relève", t0."Date fin réelle échéance", t0."Date théorique proch. relève", t0."Statut EDP Relève", t0."ACR", t0."Date fin prévue échéance", t0."Statut Relève", t0.message_id, t0."Date déb. mode gest. zone rel.", t0."Date fin mode gest. zone rel.", t0.rang_pacm_desc, t0."Référence relève", t0."Référence PDS", t0."Accès compteur", t0."Numéro voie edl", t0."Complé de localisation edl", t0."Type voie edl", t0."Voie edl", t0."Commune edl", t0."Code postal edl", t0."Code INSEE", t0."Lot", t0."Mode collecte relève", t0."Libellé prestataire", t0."Référence prestataire", t0."Date relève programmée", t0."Ecart DTR-auj. en jours cal.", t0."Ecart DTR-auj. en jours ouvrés", t0.ecart_aujourd_hui_proch_DTR_jo, CASE WHEN ("Ecart DTR-auj. en jours ouvrés" < -8) THEN 'depasse' ELSE 'non depasse' END AS type_date
                FROM (SELECT id_campagne, id_edp_releve, id_releve, "Date théorique relève", "Campagne", "Statut Campagne", "Communicant", "Technologie Compteur", Instance, code, DR, "Libellé zone relève", "Date fin réelle échéance", "Date théorique proch. relève", "Statut EDP Relève", "ACR", "Date fin prévue échéance", "Statut Relève", message_id, "Date déb. mode gest. zone rel.", "Date fin mode gest. zone rel.", rang_pacm_desc, "Référence relève", "Référence PDS", "Accès compteur", "Numéro voie edl", "Complé de localisation edl", "Type voie edl", "Voie edl", "Commune edl", "Code postal edl", "Code INSEE", "Lot", "Mode collecte relève", "Libellé prestataire", "Référence prestataire", "Date relève programmée",
                    
	(trunc("Date théorique relève") - trunc(sysdate)) AS "Ecart DTR-auj. en jours cal.", (SELECT nb_jours_ouvres FROM liste_jours_ouvres WHERE jour = "Date théorique relève") AS "Ecart DTR-auj. en jours ouvrés", (SELECT nb_jours_ouvres FROM liste_jours_ouvres WHERE jour = "Date théorique proch. relève") AS ecart_aujourd_hui_proch_DTR_jo
                    FROM (SELECT /*+ LEADING(modele_lot_releve) USE_NL(edp_releve pds) PUSH_PRED(donnees_prog) */
				campagne.ID AS id_campagne, edp_releve.ID AS id_edp_releve, releve.ID AS id_releve, CASE WHEN (lot.MODELEDELOT_ROLE = 'com.hermes.itv.releve.businessobject.ModeleDeLotDeReleveParTSP') THEN
			echeance.DATEEXECUTIONPREVUE + 18
		ELSE
			echeance.DATEEXECUTIONPREVUE + 2
		END AS "Date théorique relève", campagne.LIBELLE AS "Campagne", DECODE(campagne.STATUT, 0, 'en cours',
		1, 'fermé',
		2, 'annulé',
		3, 'suspendu',
		4, 'suppression en cours',
		'inconnu') AS "Statut Campagne", CASE WHEN (config_materielle.TECHNOLOGIE = 5 AND pds.NIVEAUCOMMUNICABILITEAMM IN ('OUVERT', 'OUVERTNIV1', 'OUVERTNIV2')) THEN 'Communicant' ELSE 'Non Communicant' END AS "Communicant", CASE config_materielle.TECHNOLOGIE
WHEN 1 THEN
		'CBE'
WHEN 2 THEN
		'CBEM'
WHEN 5 THEN
		CASE WHEN pds.NIVEAUCOMMUNICABILITEAMM IN ('OUVERT', 'OUVERTNIV1', 'OUVERTNIV2') THEN
			'LKY C'
		ELSE
			'LKY NC'
		END
ELSE
		'autre'
END AS "Technologie Compteur", decode(dir.CODE, '0328', 'ACL','0323','EST','0321','IDF','0325','MED', '0322', 'MMN',
				'0327', 'OUE', '0324', 'RAB', '0326', 'SUO', 'autre') AS Instance, dr.CODE AS code, substr(dr.LIBELLE, 20) AS DR, mode_gestion_zone_releve.LIBELLE AS "Libellé zone relève", echeance.DATEFINREELLE AS "Date fin réelle échéance", pds.DATEPROCHAINERELEVEREELLE AS "Date théorique proch. relève", DECODE(edp_releve.STATUT,
		0, 'sélectionné',
		1, 'écarté',
		2, 'en cours relève',
		3, 'relevé',
		4, 'absent relève',
		8, 'absent relève technique',
		5, 'traité',
		6, 'à estimer',
		7, 'estimé',
		10, 'complément à estimer',
		11, 'relevé et estimé complémentaire',
		999, 'mis en lot d’isolés') AS "Statut EDP Relève", acr.LIBELLE AS "ACR", echeance.DATEFINPREVUE AS "Date fin prévue échéance", DECODE(releve.STATUTRELEVE,
1, 'valide',
2, 'invalide',
3, 'En cours de traitement') AS "Statut Relève", edp_releve.MESSAGE_ID AS message_id, mode_gestion_zone_releve.DATEDEBUT AS "Date déb. mode gest. zone rel.", mode_gestion_zone_releve.DATEFIN AS "Date fin mode gest. zone rel.", DENSE_RANK() OVER (PARTITION BY pds.ID ORDER BY pacm.DATEFIN DESC, pacm.DATEDEBUT DESC, pacm.STATUTVALIDE DESC) AS rang_pacm_desc, '032'||substr(dr.CODE, 3, 1)||'_'||releve.ID AS "Référence relève", pds.REFERENCE AS "Référence PDS", decode(pds.COMPTEURACCESSIBLE,
    0, 'non', 1, 'oui') AS "Accès compteur", replace(reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1) , instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 2) )), '|', '') AS "Numéro voie edl", replace(replace(hgeo.COMPLEMENTNUMERO_HIERARCHIE, '|', ''), 'VIDE', '') AS "Complé de localisation edl", replace(replace(hgeo.TYPEDONNEEGEO_HIERARCHIE, '-', ''), 'VIDE', '') AS "Type voie edl", reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 2) + 1, (instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 3) - instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 2) -1))) AS "Voie edl", CASE WHEN (no_niveau = 6) THEN
        reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 3) + 1, (instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 4) - instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 3) -1)))
    ELSE
        reverse(substr(reverse(hgeo.LIBELLE_HIERARCHIE), instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 4) + 1, (instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 5) - instr(reverse(hgeo.LIBELLE_HIERARCHIE), '|', 1, 4) -1)))
    END AS "Commune edl", replace(replace(hgeo.CP_HIERARCHIE, '-', ''), 'VIDE', '') AS "Code postal edl", substr(replace(replace(hgeo.CODEINSEE_HIERARCHIE, '-', ''), 'VIDE', ''), 1, 5) AS "Code INSEE", lot.LIBELLE AS "Lot", mode_gestion_zone_releve.MODECOLLECTERELEVE AS "Mode collecte relève", mode_gestion_zone_releve.REFERENCEPRESTATAIRE AS "Libellé prestataire", mode_gestion_zone_releve.REFERENCEMARCHEPRESTATAIRE AS "Référence prestataire", donnees_prog."Date relève programmée"
				FROM gahfld.TPOINTDESERVICE pds
JOIN gahfld.TELEMENTDEPOPULATIONRELEVE edp_releve ON pds.ID = edp_releve.POINTDESERVICE_ID
  AND mod(pds.ETATOBJET,2) = 0
JOIN gahfld.TLOT lot ON edp_releve.LOT_ID = lot.ID
  AND mod(edp_releve.ETATOBJET,2) = 0
  AND edp_releve.LOTORIGINE_ID IS NOT NULL
JOIN gahfld.TMODELEDELOTRELEVE modele_lot_releve ON lot.MODELEDELOT_ID = modele_lot_releve.ID
  AND modele_lot_releve.LOTISOLE = 1
JOIN gahfld.TLOT lot_origine ON edp_releve.LOTORIGINE_ID = lot_origine.ID
JOIN gahfld.TCAMPAGNE campagne ON lot_origine.CAMPAGNE_ID = campagne.ID
  AND mod(campagne.ETATOBJET,2) = 0
JOIN gahfld.TECHEANCE echeance ON campagne.ECHEANCEDECLENCHEE_ID = echeance.ID
  AND mod(echeance.ETATOBJET,2) = 0
LEFT JOIN gahfld.TRELEVE releve ON edp_releve.RELEVE_ID = releve.ID
  AND mod(releve.ETATOBJET,2) = 0
JOIN gahfld.TPAABONNEMENTCYCLIQUERELEVE paacr ON pds.ID = paacr.POINTDESERVICE_ID
  AND paacr.ETATPERIODEACTIVITEACR = 1
  AND mod(paacr.ETATOBJET,2) = 0
JOIN gahfld.TABONNEMENTCYCLIQUERELEVE acr ON paacr.ABONNEMENTCYCLIQUERELEVE_ID = acr.ID
  AND mod(paacr.ETATOBJET,2) = 0
JOIN gahfld.TMODELEACR modele_acr ON acr.MODELEACR_ID = modele_acr.ID
  AND modele_acr.TYPE = 0
JOIN gahfld.TPACM pacm ON pds.ID = pacm.POINTDESERVICE_ID
JOIN gahfld.TCONFIGURATIONMATERIELLE config_materielle ON pacm.CONFIGURATIONMATERIELLE_ID = config_materielle.ID
  AND mod(pacm.ETATOBJET,2) = 0
JOIN gahfld.TESPACEDELIVRAISON edl ON pds.ESPACEDELIVRAISON_ID = edl.ID
JOIN gahfld.EDL_DECOUPAGETERRITOIRE edl_dr ON edl.ID = edl_dr.SOURCE
JOIN gahfld.TDECOUPAGETERRITOIRE dr ON edl_dr.DEST = dr.ID
  AND mod(dr.ETATOBJET,2) = 0
  AND dr.TYPEDECOUPAGETERRITOIRE = 3
  AND dr.CODE = dr.CODE
JOIN gahfld.DECTERRITOIRE_DECTERRITOIRE dr_dir ON dr.ID = dr_dir.SOURCE
JOIN gahfld.TDECOUPAGETERRITOIRE dir ON dr_dir.DEST = dir.ID
JOIN gahfld.TROLEFUNCTIONALUNIT role_unite_fonctionnelle ON pds.ID = role_unite_fonctionnelle.ITEM_ID
JOIN gahfld.TMODEGESTIONZONEDERELEVE mode_gestion_zone_releve ON role_unite_fonctionnelle.UNIT_ID = mode_gestion_zone_releve.PORTEFEUILLEPDSZONEDERELEVE_ID
  AND mod(mode_gestion_zone_releve.ETATOBJET,2) = 0
LEFT JOIN gahfld.TRELEVE releve ON edp_releve.RELEVE_ID = releve.ID
  AND mod(releve.ETATOBJET,2) = 0
LEFT JOIN (SELECT /*+ LEADING(pds) USE_NL(pds edp_wkf donnees_prog_releve) */ pds.ID AS id_pds, edp_wkf.OBJETTRAITE_ID AS objettraite_id, donnees_prog_releve.DATERELEVEPROGRAMMEE AS "Date relève programmée", donnees_prog_releve.HEUREDEBUTPLAGEPASSAGERELEVEUR AS "Heure déb. plage passage relv", donnees_prog_releve.HEUREFINPLAGEPASSAGERELEVEUR AS "Heure fin plage passage relv", edp_wkf.ETATOBJET AS etatobjet
FROM gahfld.TPOINTDESERVICE pds
JOIN gahfld.TELEMENTDEPOPULATIONWKF edp_wkf ON pds.ID = edp_wkf.OBJETTRAITE_ID
  AND mod(pds.ETATOBJET,2) = 0
  AND mod(edp_wkf.ETATOBJET,2) = 0
JOIN gahfld.TDONNEESPROGRAMMATIONRELEVE donnees_prog_releve ON edp_wkf.OBJETCONNEXE_ID = donnees_prog_releve.ID) donnees_prog ON pds.ID = donnees_prog.id_pds
LEFT JOIN hierarchie_geo hgeo ON edl.ADRESSE_ID = hgeo.id
				WHERE (lot.MODELEDELOT_ROLE = 'com.hermes.itv.releve.businessobject.ModeleDeLotDeReleveParTSP')
                AND mode_gestion_zone_releve.MODECOLLECTERELEVE = 0
				AND 
	(CASE WHEN (campagne.STATUT = 0) THEN 1
	 ELSE
		CASE WHEN (campagne.STATUT = 1) THEN
			CASE WHEN (trunc(sysdate) - trunc(echeance.DATEFINPREVUE) <= 100 ) THEN
				1
			ELSE
				0
			END
		ELSE
			0
		END
	END) = 1
				AND dr.CODE = dr.code) edp_isoles_base
                    WHERE rang_pacm_desc = 1
                    AND "Date théorique relève" >= nvl("Date déb. mode gest. zone rel.", to_date('01/01/0001', 'dd/MM/yyyy'))
                    AND "Date théorique relève" < nvl("Date fin mode gest. zone rel.", to_date('31/12/9999', 'dd/MM/yyyy'))) t0
                WHERE 
	(CASE WHEN ("Communicant" = 'Communicant') THEN 1 ELSE CASE WHEN (ecart_aujourd_hui_proch_DTR_jo > 41) THEN
		1
	ELSE
		0
	END END) = 1
            ) t1
            ) t2
            ) t3
            ) t4
			),
groupe_dates_repasse_isoles AS (SELECT categorie_ecart_auj_DTR_jo,
            LISTAGG(date_cat_ecart_auj_DTR_jo, ', ') WITHIN GROUP (ORDER BY date_cat_ecart_auj_DTR_jo) AS date_DTR_jo_agg
            FROM (
                SELECT DISTINCT categorie_ecart_auj_DTR_jo, date_cat_ecart_auj_DTR_jo
                FROM edp_isoles_camp_en_cours_cat edps
            )
            GROUP BY categorie_ecart_auj_DTR_jo
            ),
edp_lot_isoles_camp_en_cours AS (SELECT edp_isoles_camp_en_cours_cat.*, groupe_dates_repasse_isoles.date_DTR_jo_agg
            FROM edp_isoles_camp_en_cours_cat
JOIN groupe_dates_repasse_isoles ON edp_isoles_camp_en_cours_cat.categorie_ecart_auj_DTR_jo = groupe_dates_repasse_isoles.categorie_ecart_auj_DTR_jo
            ),
taches_perimetre AS (
		SELECT /*+ LEADING(type_role_metier, tache) INLINE */ tache.ID AS id_tache, tache.REFERENCE AS "Référence tâche", tache.ELEMENTDETRAVAIL_ID AS elementdetravail_id, tache.OBJETMAITRE_ID AS objetmaitre_id, gt.LIBELLE AS "Libellé GT", liste_gestion.LIBELLE AS "Libellé liste de gestion", nature_action_tache.LIBELLE AS "Libellé nature de tâche", nature_tache.LIBELLETACHE AS "Libellé tâche", famille_tache.LONGLABEL AS "Famille de tâche", type_gt.LIBELLE AS "Libellé type GT", gt_pere.LIBELLE AS "Libellé GT père", CASE WHEN (lower(type_gt.LIBELLE)) like '%ach%' THEN 'Acheminement'
     WHEN (lower(type_gt.LIBELLE)) like '%linky%' THEN 'ACHT'
     WHEN (lower(type_gt.LIBELLE)) like '%pilotage%' THEN 'GPIL'
     WHEN (lower(type_gt.LIBELLE)) like '%cpa%' THEN 'GPIL'
     WHEN (lower(type_gt.LIBELLE)) like '%relevé%' THEN 'CPR'
     END AS "Type d'agence", DECODE(tache.STATUT,
	0, 'à faire',
	1, 'en cours',
	2, 'clotûrée') AS "Statut tâche", tache.DATECREATION AS "Date création tâche", tache.DATEECHEANCE AS "Date échéance tâche", tache.DATEFIN AS "Date fin tâche", tache.ELEMENTDETRAVAIL_ROLE AS elementdetravail_role, tache.POSTEDETRAVAIL_ID AS postedetravail_id, type_role_metier.LIBELLE AS "Libellé Type Rôle Métier", 
CASE WHEN (tache.ELEMENTDETRAVAIL_ROLE = 'AN') THEN 
	'tâche liée à une anomalie' 
ELSE 
	'tâche liée à un EDP' 
END AS "Rôle tâche", 
CASE WHEN (tache.STATUT <> 2) THEN 
	CASE WHEN (trunc(sysdate) > trunc(tache.DATEECHEANCE)) THEN 
		'oui'
	ELSE 
		'non'
	END 
ELSE 
	CASE WHEN (tache.DATEFIN > tache.DATEECHEANCE) THEN 
		'oui'
	ELSE 
		'non'
	END 
END
 AS "Tâche en retard", trunc(sysdate) - trunc(tache.DATEECHEANCE) AS "Nb. jours de retard", 
CASE WHEN tache.STATUT IN (0, 1) THEN 
	'pas traitée'
ELSE 
	CASE nvl(tache.ACTEURCLOTURE_ID, 'absent')
	WHEN ('BGF|B-GF-ERDF|batch') THEN 
		'traitée par batch'
	WHEN ('absent') THEN
		'absence donnée'
	ELSE 'traitée par agent'
	END
END AS "Acteur clôture tâche"
		FROM gahfld.TTACHE tache
JOIN gahfld.TTYPEDEROLEMETIER type_role_metier ON tache.TYPEDEROLEMETIER_ID = type_role_metier.ID
  AND mod(tache.ETATOBJET, 2) = 0
  AND mod(type_role_metier.ETATOBJET, 2) = 0
JOIN gahfld.TNATUREACTION nature_action_tache ON tache.NATUREDETACHE_ID = nature_action_tache.ID
JOIN gahfld.TNATUREDETACHE nature_tache ON nature_action_tache.ID = nature_tache.ID
LEFT JOIN gahfld.TENUM famille_tache ON nature_tache.FAMILLEDETACHE = famille_tache.CODE
  AND famille_tache.TYPE = 'FAMTACHE'
  AND mod(famille_tache.ETATOBJET, 2) = 0
JOIN gahfld.TLISTEDEGESTION liste_gestion ON tache.LISTEDEGESTION_ID = liste_gestion.ID
  AND mod(liste_gestion.ETATOBJET, 2) = 0
JOIN gahfld.TGROUPEDETRAVAIL gt ON liste_gestion.GROUPEDETRAVAIL_ID = gt.ID
  AND mod(gt.ETATOBJET, 2) = 0
LEFT JOIN gahfld.TGROUPEDETRAVAIL gt_pere ON gt.GROUPEDETRAVAILPERE_ID = gt_pere.ID
  AND mod(gt_pere.ETATOBJET, 2) = 0
LEFT JOIN gahfld.TTYPEDEGROUPEDETRAVAIL type_gt ON gt.TYPEDEGROUPEDETRAVAIL_ID = type_gt.ID
  AND mod(type_gt.ETATOBJET, 2) = 0
		WHERE (CASE WHEN (tache.STATUT IN (0, 1)) THEN 1 ELSE CASE WHEN (trunc(tache.DATEFIN) = trunc(sysdate)) THEN 1 ELSE 0 END END) = 1
		AND nature_action_tache.LIBELLE IN ('Compteur bloqué ou HS et endommagé',
'Compteur déposé',
'Ecart accessibilité',
'Ecart matricule compteur',
'Ecart nombre de cadrans',
'PNT ou suspicion',
'Compteur introuvable',
'Défaut matériel hors compteur',
'Information pour relevé futur',
'Refus client accès compteur'
)
		AND NOT (gt.LIBELLE = 'Administration fonctionnelle'))

		SELECT id_campagne, id_edp_releve, id_releve, "Date théorique relève", "Campagne", "Statut Campagne", "Communicant", "Technologie Compteur", Instance, code, DR, "Libellé zone relève", "Date fin réelle échéance", "Date théorique proch. relève", "Statut EDP Relève", "ACR", "Date fin prévue échéance", "Statut Relève", message_id, "Date déb. mode gest. zone rel.", "Date fin mode gest. zone rel.", rang_pacm_desc, "Référence relève", "Référence PDS", "Accès compteur", "Numéro voie edl", "Complé de localisation edl", "Type voie edl", "Voie edl", "Commune edl", "Code postal edl", "Code INSEE", "Lot", "Mode collecte relève", "Libellé prestataire", "Référence prestataire", "Date relève programmée", "Ecart DTR-auj. en jours cal.", "Ecart DTR-auj. en jours ouvrés", ecart_aujourd_hui_proch_DTR_jo, type_date, rang_dtr_depasse, rang_dtr_a_venir, rang_dtr_depasse_unqmt, rang_dtr_a_venir_unqmt, num_categorie, categorie_ecart_auj_DTR_jo, date_cat_ecart_auj_DTR_jo, date_DTR_jo_agg, id_tache, "Référence tâche", elementdetravail_id, objetmaitre_id, "Libellé GT", "Libellé liste de gestion", "Libellé nature de tâche", "Libellé tâche", "Famille de tâche", "Libellé type GT", "Libellé GT père", "Type d'agence", "Statut tâche", "Date création tâche", "Date échéance tâche", "Date fin tâche", elementdetravail_role, postedetravail_id, "Libellé Type Rôle Métier", "Rôle tâche", "Tâche en retard", "Nb. jours de retard", "Acteur clôture tâche", id_anomalie, "Anomalie Bloquante", "Date création anomalie", "Date levée ou levée forcée", "NNI agent levée", "Agent levée", "Statut anomalie", "Type d'anomalie", "Code anomalie flux Mars",
        CASE WHEN (rang_campagne = 1) THEN 1 ELSE 0 END AS premiere_campagne,
CASE WHEN ("Statut Campagne" = 'en cours') THEN 1 ELSE 0 END AS "Campagne est ouverte",
CASE WHEN (trunc("Date fin réelle échéance") = trunc(sysdate)) THEN 1 ELSE 0 END AS "Campagne clôturée auj.",
CASE WHEN (rang_edp = 1) THEN 1 ELSE 0 END AS premier_edp,
CASE WHEN (rang_tache = 1) THEN 1 ELSE 0 END AS premiere_tache,
CASE WHEN ("Statut tâche" IN ('à faire', 'en cours')) THEN 1 ELSE 0 END AS tache_a_traiter,
CASE WHEN ("Statut tâche" = 'à faire') THEN 1 ELSE 0 END AS tache_a_faire,
CASE WHEN (trunc("Date création tâche") = trunc(sysdate)) THEN 1 ELSE 0 END AS tache_creee_aujourd_hui,
CASE WHEN (trunc("Date échéance tâche") = trunc(sysdate)) THEN 1 ELSE 0 END AS tache_a_traiter_aujourd_hui,
CASE WHEN (trunc("Date fin tâche") = trunc(sysdate)) THEN 1 ELSE 0 END AS tache_cloturee_aujourd_hui,
CASE WHEN (trunc("Date échéance tâche") < trunc(sysdate)) THEN 1 ELSE 0 END AS tache_est_en_retard,
CASE WHEN (((
	CASE WHEN elementdetravail_role = 'AN' THEN
		CASE WHEN ("Anomalie Bloquante" = 1) THEN 1
		ELSE 0
		END
	ELSE
		1
	END
	) = 1)
	) THEN 1 ELSE 0 END AS "Tâche bloquante",
CASE WHEN (postedetravail_id IS NOT NULL) THEN 1 ELSE 0 END AS "Tâche affectée",
CASE WHEN (rang_acr = 1) THEN 1 ELSE 0 END AS premier_acr,
CASE WHEN ("Ecart DTR-auj. en jours ouvrés" <= 5) THEN 1 ELSE 0 END AS "Ancienn. camp. inf. eg. 5 jo",
CASE WHEN ("Libellé nature de tâche" IN ('Ecart matricule compteur',
	'Ecart nombre de cadrans',
	'Compteur introuvable',
	'Refus client accès compteur')) THEN 1 ELSE 0 END AS "Tac. a trait. av. fin camp.",
CASE WHEN (trunc(sysdate) <= "Date fin prévue échéance") THEN 1 ELSE 0 END AS "Fin théo. camp. non dépassée",
CASE WHEN (ecart_aujourd_hui_proch_DTR_jo <= 51) THEN 1 ELSE 0 END AS moins_2_sem_av_proc_prog,
CASE WHEN ("Statut EDP Relève" = 'traité'
            AND "Statut Relève" = 'valide') THEN 1 ELSE 0 END AS releve_perim_cpr_traitee,
CASE WHEN (NOT "Statut EDP Relève" IN ('écarté', 'traité', 'estimé', 'relevé et estimé complémentaire') 
            AND "Statut Relève" = 'En cours de traitement') THEN 1 ELSE 0 END AS releve_sur_site_en_cours_trait,
CASE WHEN ("Communicant" = 'Communicant') THEN 1 ELSE 0 END AS "Est communicant",
CASE WHEN ("Statut EDP Relève" = 'traité'
            AND "Statut Relève" = 'valide' AND "Edp avec code ano flux Mars" = 1) THEN 1 ELSE 0 END AS "CR Mars reçu"
        
        
        , "Edp avec code ano flux Mars"
		FROM (
			SELECT id_campagne, id_edp_releve, id_releve, "Date théorique relève", "Campagne", "Statut Campagne", "Communicant", "Technologie Compteur", Instance, code, DR, "Libellé zone relève", "Date fin réelle échéance", "Date théorique proch. relève", "Statut EDP Relève", "ACR", "Date fin prévue échéance", "Statut Relève", message_id, "Date déb. mode gest. zone rel.", "Date fin mode gest. zone rel.", rang_pacm_desc, "Référence relève", "Référence PDS", "Accès compteur", "Numéro voie edl", "Complé de localisation edl", "Type voie edl", "Voie edl", "Commune edl", "Code postal edl", "Code INSEE", "Lot", "Mode collecte relève", "Libellé prestataire", "Référence prestataire", "Date relève programmée", "Ecart DTR-auj. en jours cal.", "Ecart DTR-auj. en jours ouvrés", ecart_aujourd_hui_proch_DTR_jo, type_date, rang_dtr_depasse, rang_dtr_a_venir, rang_dtr_depasse_unqmt, rang_dtr_a_venir_unqmt, num_categorie, categorie_ecart_auj_DTR_jo, date_cat_ecart_auj_DTR_jo, date_DTR_jo_agg, id_tache, "Référence tâche", elementdetravail_id, objetmaitre_id, "Libellé GT", "Libellé liste de gestion", "Libellé nature de tâche", "Libellé tâche", "Famille de tâche", "Libellé type GT", "Libellé GT père", "Type d'agence", "Statut tâche", "Date création tâche", "Date échéance tâche", "Date fin tâche", elementdetravail_role, postedetravail_id, "Libellé Type Rôle Métier", "Rôle tâche", "Tâche en retard", "Nb. jours de retard", "Acteur clôture tâche", id_anomalie, "Anomalie Bloquante", "Date création anomalie", "Date levée ou levée forcée", "NNI agent levée", "Agent levée", "Statut anomalie", "Type d'anomalie", "Code anomalie flux Mars",
			ROW_NUMBER() OVER
(PARTITION BY "Date théorique relève"
ORDER BY id_edp_releve, id_tache, id_anomalie) AS rang_acr, ROW_NUMBER() OVER (PARTITION BY "Date théorique relève", "Campagne" ORDER BY id_edp_releve, id_tache, id_anomalie) AS rang_campagne, ROW_NUMBER() OVER (PARTITION BY id_edp_releve ORDER BY id_tache, id_anomalie) AS rang_edp, ROW_NUMBER() OVER (PARTITION BY id_tache ORDER BY id_anomalie) AS rang_tache, MAX("Code anomalie flux Mars") OVER (PARTITION BY id_edp_releve) AS "Edp avec code ano flux Mars"
            
            
			FROM (
				(
            SELECT /*+ LEADING(edp_campagnes_en_cours) */
            edp_campagnes_en_cours.id_campagne, edp_campagnes_en_cours.id_edp_releve, edp_campagnes_en_cours.id_releve, edp_campagnes_en_cours."Date théorique relève", edp_campagnes_en_cours."Campagne", edp_campagnes_en_cours."Statut Campagne", edp_campagnes_en_cours."Communicant", edp_campagnes_en_cours."Technologie Compteur", edp_campagnes_en_cours.Instance, edp_campagnes_en_cours.code, edp_campagnes_en_cours.DR, edp_campagnes_en_cours."Libellé zone relève", edp_campagnes_en_cours."Date fin réelle échéance", edp_campagnes_en_cours."Date théorique proch. relève", edp_campagnes_en_cours."Statut EDP Relève", edp_campagnes_en_cours."ACR", edp_campagnes_en_cours."Date fin prévue échéance", edp_campagnes_en_cours."Statut Relève", edp_campagnes_en_cours.message_id, edp_campagnes_en_cours."Date déb. mode gest. zone rel.", edp_campagnes_en_cours."Date fin mode gest. zone rel.", edp_campagnes_en_cours.rang_pacm_desc, edp_campagnes_en_cours."Référence relève", edp_campagnes_en_cours."Référence PDS", edp_campagnes_en_cours."Accès compteur", edp_campagnes_en_cours."Numéro voie edl", edp_campagnes_en_cours."Complé de localisation edl", edp_campagnes_en_cours."Type voie edl", edp_campagnes_en_cours."Voie edl", edp_campagnes_en_cours."Commune edl", edp_campagnes_en_cours."Code postal edl", edp_campagnes_en_cours."Code INSEE", edp_campagnes_en_cours."Lot", edp_campagnes_en_cours."Mode collecte relève", edp_campagnes_en_cours."Libellé prestataire", edp_campagnes_en_cours."Référence prestataire", edp_campagnes_en_cours."Date relève programmée", edp_campagnes_en_cours."Ecart DTR-auj. en jours cal.", edp_campagnes_en_cours."Ecart DTR-auj. en jours ouvrés", edp_campagnes_en_cours.ecart_aujourd_hui_proch_DTR_jo, edp_campagnes_en_cours.type_date, edp_campagnes_en_cours.rang_dtr_depasse, edp_campagnes_en_cours.rang_dtr_a_venir, edp_campagnes_en_cours.rang_dtr_depasse_unqmt, edp_campagnes_en_cours.rang_dtr_a_venir_unqmt, edp_campagnes_en_cours.num_categorie, edp_campagnes_en_cours.categorie_ecart_auj_DTR_jo, edp_campagnes_en_cours.date_cat_ecart_auj_DTR_jo, edp_campagnes_en_cours.date_DTR_jo_agg, taches_perimetre.id_tache, taches_perimetre."Référence tâche", taches_perimetre.elementdetravail_id, taches_perimetre.objetmaitre_id, taches_perimetre."Libellé GT", taches_perimetre."Libellé liste de gestion", taches_perimetre."Libellé nature de tâche", taches_perimetre."Libellé tâche", taches_perimetre."Famille de tâche", taches_perimetre."Libellé type GT", taches_perimetre."Libellé GT père", taches_perimetre."Type d'agence", taches_perimetre."Statut tâche", taches_perimetre."Date création tâche", taches_perimetre."Date échéance tâche", taches_perimetre."Date fin tâche", taches_perimetre.elementdetravail_role, taches_perimetre.postedetravail_id, taches_perimetre."Libellé Type Rôle Métier", taches_perimetre."Rôle tâche", taches_perimetre."Tâche en retard", taches_perimetre."Nb. jours de retard", taches_perimetre."Acteur clôture tâche", anomalie.ID AS id_anomalie, type_anomalie.ANOMALIEBLOQUANTE AS "Anomalie Bloquante", anomalie.DATECREATION AS "Date création anomalie", anomalie.DATELEVEEOULEVEEFORCEE AS "Date levée ou levée forcée", CASE WHEN (lower(anomalie.AGENTLEVEE_ID) LIKE '%batch%') THEN 'batch' ELSE substr(anomalie.AGENTLEVEE_ID, 1, instr(anomalie.AGENTLEVEE_ID, '|') -1 ) END AS "NNI agent levée", substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|') + 1, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) - instr(anomalie.AGENTLEVEE_ID, '|') - 1) || ' ' || substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) + 1) AS "Agent levée", decode(anomalie.STATUTANOMALIE, 0, 'en cours', 1, 'levée', 2, 'levée forcée', 3, 'annulée', 4, 'sans action') AS "Statut anomalie", type_anomalie.LIBELLELONG AS "Type d'anomalie", CASE WHEN (type_anomalie.CODETYPEANOMALIE IN ('220', '581', '1534', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1535', '1536', '1523', '1524', '1537', '1525', '1526', '1528', '1529', '1530', '1531', '1511', '1512', '1513', '1514', '1515', '1516', '1518', '1519', '1520', '1521', '1522')) THEN 1 ELSE 0 END AS "Code anomalie flux Mars"
            
            FROM edp_campagnes_en_cours, taches_perimetre, gahfld.TANOMALIE anomalie, gahfld.TPARAMTYPEANOMALIE type_anomalie
WHERE edp_campagnes_en_cours.id_edp_releve = taches_perimetre.elementdetravail_id(+)
AND edp_campagnes_en_cours.id_edp_releve = anomalie.ELEMENTPOPULATION_ID(+)
AND mod(anomalie.ETATOBJET,2) = 0
AND anomalie.TYPEANOMALIE = type_anomalie.CODETYPEANOMALIE(+)
AND anomalie.TYPEANOMALIE_ROLE = type_anomalie.CLASSETYPEANOMALIE(+)
AND mod(type_anomalie.ETATOBJET(+),2) = 0

            
            UNION
            
            SELECT /*+ LEADING(edp_lot_isoles_camp_en_cours) */
            edp_lot_isoles_camp_en_cours.id_campagne, edp_lot_isoles_camp_en_cours.id_edp_releve, edp_lot_isoles_camp_en_cours.id_releve, edp_lot_isoles_camp_en_cours."Date théorique relève", edp_lot_isoles_camp_en_cours."Campagne", edp_lot_isoles_camp_en_cours."Statut Campagne", edp_lot_isoles_camp_en_cours."Communicant", edp_lot_isoles_camp_en_cours."Technologie Compteur", edp_lot_isoles_camp_en_cours.Instance, edp_lot_isoles_camp_en_cours.code, edp_lot_isoles_camp_en_cours.DR, edp_lot_isoles_camp_en_cours."Libellé zone relève", edp_lot_isoles_camp_en_cours."Date fin réelle échéance", edp_lot_isoles_camp_en_cours."Date théorique proch. relève", edp_lot_isoles_camp_en_cours."Statut EDP Relève", edp_lot_isoles_camp_en_cours."ACR", edp_lot_isoles_camp_en_cours."Date fin prévue échéance", edp_lot_isoles_camp_en_cours."Statut Relève", edp_lot_isoles_camp_en_cours.message_id, edp_lot_isoles_camp_en_cours."Date déb. mode gest. zone rel.", edp_lot_isoles_camp_en_cours."Date fin mode gest. zone rel.", edp_lot_isoles_camp_en_cours.rang_pacm_desc, edp_lot_isoles_camp_en_cours."Référence relève", edp_lot_isoles_camp_en_cours."Référence PDS", edp_lot_isoles_camp_en_cours."Accès compteur", edp_lot_isoles_camp_en_cours."Numéro voie edl", edp_lot_isoles_camp_en_cours."Complé de localisation edl", edp_lot_isoles_camp_en_cours."Type voie edl", edp_lot_isoles_camp_en_cours."Voie edl", edp_lot_isoles_camp_en_cours."Commune edl", edp_lot_isoles_camp_en_cours."Code postal edl", edp_lot_isoles_camp_en_cours."Code INSEE", edp_lot_isoles_camp_en_cours."Lot", edp_lot_isoles_camp_en_cours."Mode collecte relève", edp_lot_isoles_camp_en_cours."Libellé prestataire", edp_lot_isoles_camp_en_cours."Référence prestataire", edp_lot_isoles_camp_en_cours."Date relève programmée", edp_lot_isoles_camp_en_cours."Ecart DTR-auj. en jours cal.", edp_lot_isoles_camp_en_cours."Ecart DTR-auj. en jours ouvrés", edp_lot_isoles_camp_en_cours.ecart_aujourd_hui_proch_DTR_jo, edp_lot_isoles_camp_en_cours.type_date, edp_lot_isoles_camp_en_cours.rang_dtr_depasse, edp_lot_isoles_camp_en_cours.rang_dtr_a_venir, edp_lot_isoles_camp_en_cours.rang_dtr_depasse_unqmt, edp_lot_isoles_camp_en_cours.rang_dtr_a_venir_unqmt, edp_lot_isoles_camp_en_cours.num_categorie, edp_lot_isoles_camp_en_cours.categorie_ecart_auj_DTR_jo, edp_lot_isoles_camp_en_cours.date_cat_ecart_auj_DTR_jo, edp_lot_isoles_camp_en_cours.date_DTR_jo_agg, taches_perimetre.id_tache, taches_perimetre."Référence tâche", taches_perimetre.elementdetravail_id, taches_perimetre.objetmaitre_id, taches_perimetre."Libellé GT", taches_perimetre."Libellé liste de gestion", taches_perimetre."Libellé nature de tâche", taches_perimetre."Libellé tâche", taches_perimetre."Famille de tâche", taches_perimetre."Libellé type GT", taches_perimetre."Libellé GT père", taches_perimetre."Type d'agence", taches_perimetre."Statut tâche", taches_perimetre."Date création tâche", taches_perimetre."Date échéance tâche", taches_perimetre."Date fin tâche", taches_perimetre.elementdetravail_role, taches_perimetre.postedetravail_id, taches_perimetre."Libellé Type Rôle Métier", taches_perimetre."Rôle tâche", taches_perimetre."Tâche en retard", taches_perimetre."Nb. jours de retard", taches_perimetre."Acteur clôture tâche", anomalie.ID AS id_anomalie, type_anomalie.ANOMALIEBLOQUANTE AS "Anomalie Bloquante", anomalie.DATECREATION AS "Date création anomalie", anomalie.DATELEVEEOULEVEEFORCEE AS "Date levée ou levée forcée", CASE WHEN (lower(anomalie.AGENTLEVEE_ID) LIKE '%batch%') THEN 'batch' ELSE substr(anomalie.AGENTLEVEE_ID, 1, instr(anomalie.AGENTLEVEE_ID, '|') -1 ) END AS "NNI agent levée", substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|') + 1, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) - instr(anomalie.AGENTLEVEE_ID, '|') - 1) || ' ' || substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) + 1) AS "Agent levée", decode(anomalie.STATUTANOMALIE, 0, 'en cours', 1, 'levée', 2, 'levée forcée', 3, 'annulée', 4, 'sans action') AS "Statut anomalie", type_anomalie.LIBELLELONG AS "Type d'anomalie", CASE WHEN (type_anomalie.CODETYPEANOMALIE IN ('220', '581', '1534', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1535', '1536', '1523', '1524', '1537', '1525', '1526', '1528', '1529', '1530', '1531', '1511', '1512', '1513', '1514', '1515', '1516', '1518', '1519', '1520', '1521', '1522')) THEN 1 ELSE 0 END AS "Code anomalie flux Mars"
            
            FROM edp_lot_isoles_camp_en_cours
LEFT JOIN taches_perimetre ON edp_lot_isoles_camp_en_cours.id_edp_releve = taches_perimetre.elementdetravail_id
LEFT JOIN gahfld.TANOMALIE anomalie ON edp_lot_isoles_camp_en_cours.id_edp_releve = anomalie.ELEMENTPOPULATION_ID
  AND mod(anomalie.ETATOBJET,2) = 0
LEFT JOIN gahfld.TPARAMTYPEANOMALIE type_anomalie ON anomalie.TYPEANOMALIE = type_anomalie.CODETYPEANOMALIE
  AND mod(type_anomalie.ETATOBJET,2) = 0
  AND anomalie.TYPEANOMALIE_ROLE = type_anomalie.CLASSETYPEANOMALIE
  AND mod(type_anomalie.ETATOBJET,2) = 0
            
            UNION

            SELECT /*+ LEADING(edp_campagnes_en_cours) */
            edp_campagnes_en_cours.id_campagne, edp_campagnes_en_cours.id_edp_releve, edp_campagnes_en_cours.id_releve, edp_campagnes_en_cours."Date théorique relève", edp_campagnes_en_cours."Campagne", edp_campagnes_en_cours."Statut Campagne", edp_campagnes_en_cours."Communicant", edp_campagnes_en_cours."Technologie Compteur", edp_campagnes_en_cours.Instance, edp_campagnes_en_cours.code, edp_campagnes_en_cours.DR, edp_campagnes_en_cours."Libellé zone relève", edp_campagnes_en_cours."Date fin réelle échéance", edp_campagnes_en_cours."Date théorique proch. relève", edp_campagnes_en_cours."Statut EDP Relève", edp_campagnes_en_cours."ACR", edp_campagnes_en_cours."Date fin prévue échéance", edp_campagnes_en_cours."Statut Relève", edp_campagnes_en_cours.message_id, edp_campagnes_en_cours."Date déb. mode gest. zone rel.", edp_campagnes_en_cours."Date fin mode gest. zone rel.", edp_campagnes_en_cours.rang_pacm_desc, edp_campagnes_en_cours."Référence relève", edp_campagnes_en_cours."Référence PDS", edp_campagnes_en_cours."Accès compteur", edp_campagnes_en_cours."Numéro voie edl", edp_campagnes_en_cours."Complé de localisation edl", edp_campagnes_en_cours."Type voie edl", edp_campagnes_en_cours."Voie edl", edp_campagnes_en_cours."Commune edl", edp_campagnes_en_cours."Code postal edl", edp_campagnes_en_cours."Code INSEE", edp_campagnes_en_cours."Lot", edp_campagnes_en_cours."Mode collecte relève", edp_campagnes_en_cours."Libellé prestataire", edp_campagnes_en_cours."Référence prestataire", edp_campagnes_en_cours."Date relève programmée", edp_campagnes_en_cours."Ecart DTR-auj. en jours cal.", edp_campagnes_en_cours."Ecart DTR-auj. en jours ouvrés", edp_campagnes_en_cours.ecart_aujourd_hui_proch_DTR_jo, edp_campagnes_en_cours.type_date, edp_campagnes_en_cours.rang_dtr_depasse, edp_campagnes_en_cours.rang_dtr_a_venir, edp_campagnes_en_cours.rang_dtr_depasse_unqmt, edp_campagnes_en_cours.rang_dtr_a_venir_unqmt, edp_campagnes_en_cours.num_categorie, edp_campagnes_en_cours.categorie_ecart_auj_DTR_jo, edp_campagnes_en_cours.date_cat_ecart_auj_DTR_jo, edp_campagnes_en_cours.date_DTR_jo_agg, taches_perimetre.id_tache, taches_perimetre."Référence tâche", taches_perimetre.elementdetravail_id, taches_perimetre.objetmaitre_id, taches_perimetre."Libellé GT", taches_perimetre."Libellé liste de gestion", taches_perimetre."Libellé nature de tâche", taches_perimetre."Libellé tâche", taches_perimetre."Famille de tâche", taches_perimetre."Libellé type GT", taches_perimetre."Libellé GT père", taches_perimetre."Type d'agence", taches_perimetre."Statut tâche", taches_perimetre."Date création tâche", taches_perimetre."Date échéance tâche", taches_perimetre."Date fin tâche", taches_perimetre.elementdetravail_role, taches_perimetre.postedetravail_id, taches_perimetre."Libellé Type Rôle Métier", taches_perimetre."Rôle tâche", taches_perimetre."Tâche en retard", taches_perimetre."Nb. jours de retard", taches_perimetre."Acteur clôture tâche", anomalie.ID AS id_anomalie, type_anomalie.ANOMALIEBLOQUANTE AS "Anomalie Bloquante", anomalie.DATECREATION AS "Date création anomalie", anomalie.DATELEVEEOULEVEEFORCEE AS "Date levée ou levée forcée", CASE WHEN (lower(anomalie.AGENTLEVEE_ID) LIKE '%batch%') THEN 'batch' ELSE substr(anomalie.AGENTLEVEE_ID, 1, instr(anomalie.AGENTLEVEE_ID, '|') -1 ) END AS "NNI agent levée", substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|') + 1, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) - instr(anomalie.AGENTLEVEE_ID, '|') - 1) || ' ' || substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) + 1) AS "Agent levée", decode(anomalie.STATUTANOMALIE, 0, 'en cours', 1, 'levée', 2, 'levée forcée', 3, 'annulée', 4, 'sans action') AS "Statut anomalie", type_anomalie.LIBELLELONG AS "Type d'anomalie", CASE WHEN (type_anomalie.CODETYPEANOMALIE IN ('220', '581', '1534', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1535', '1536', '1523', '1524', '1537', '1525', '1526', '1528', '1529', '1530', '1531', '1511', '1512', '1513', '1514', '1515', '1516', '1518', '1519', '1520', '1521', '1522')) THEN 1 ELSE 0 END AS "Code anomalie flux Mars"
            
            FROM edp_campagnes_en_cours
LEFT JOIN gahfld.TANOMALIE anomalie ON edp_campagnes_en_cours.id_edp_releve = anomalie.ELEMENTPOPULATION_ID
  AND mod(anomalie.ETATOBJET,2) = 0
LEFT JOIN gahfld.TPARAMTYPEANOMALIE type_anomalie ON anomalie.TYPEANOMALIE = type_anomalie.CODETYPEANOMALIE
  AND mod(type_anomalie.ETATOBJET,2) = 0
  AND anomalie.TYPEANOMALIE_ROLE = type_anomalie.CLASSETYPEANOMALIE
  AND mod(type_anomalie.ETATOBJET,2) = 0
LEFT JOIN taches_perimetre ON anomalie.ID = taches_perimetre.elementdetravail_id
            
            UNION
            
            SELECT /*+ LEADING(edp_lot_isoles_camp_en_cours) */
            edp_lot_isoles_camp_en_cours.id_campagne, edp_lot_isoles_camp_en_cours.id_edp_releve, edp_lot_isoles_camp_en_cours.id_releve, edp_lot_isoles_camp_en_cours."Date théorique relève", edp_lot_isoles_camp_en_cours."Campagne", edp_lot_isoles_camp_en_cours."Statut Campagne", edp_lot_isoles_camp_en_cours."Communicant", edp_lot_isoles_camp_en_cours."Technologie Compteur", edp_lot_isoles_camp_en_cours.Instance, edp_lot_isoles_camp_en_cours.code, edp_lot_isoles_camp_en_cours.DR, edp_lot_isoles_camp_en_cours."Libellé zone relève", edp_lot_isoles_camp_en_cours."Date fin réelle échéance", edp_lot_isoles_camp_en_cours."Date théorique proch. relève", edp_lot_isoles_camp_en_cours."Statut EDP Relève", edp_lot_isoles_camp_en_cours."ACR", edp_lot_isoles_camp_en_cours."Date fin prévue échéance", edp_lot_isoles_camp_en_cours."Statut Relève", edp_lot_isoles_camp_en_cours.message_id, edp_lot_isoles_camp_en_cours."Date déb. mode gest. zone rel.", edp_lot_isoles_camp_en_cours."Date fin mode gest. zone rel.", edp_lot_isoles_camp_en_cours.rang_pacm_desc, edp_lot_isoles_camp_en_cours."Référence relève", edp_lot_isoles_camp_en_cours."Référence PDS", edp_lot_isoles_camp_en_cours."Accès compteur", edp_lot_isoles_camp_en_cours."Numéro voie edl", edp_lot_isoles_camp_en_cours."Complé de localisation edl", edp_lot_isoles_camp_en_cours."Type voie edl", edp_lot_isoles_camp_en_cours."Voie edl", edp_lot_isoles_camp_en_cours."Commune edl", edp_lot_isoles_camp_en_cours."Code postal edl", edp_lot_isoles_camp_en_cours."Code INSEE", edp_lot_isoles_camp_en_cours."Lot", edp_lot_isoles_camp_en_cours."Mode collecte relève", edp_lot_isoles_camp_en_cours."Libellé prestataire", edp_lot_isoles_camp_en_cours."Référence prestataire", edp_lot_isoles_camp_en_cours."Date relève programmée", edp_lot_isoles_camp_en_cours."Ecart DTR-auj. en jours cal.", edp_lot_isoles_camp_en_cours."Ecart DTR-auj. en jours ouvrés", edp_lot_isoles_camp_en_cours.ecart_aujourd_hui_proch_DTR_jo, edp_lot_isoles_camp_en_cours.type_date, edp_lot_isoles_camp_en_cours.rang_dtr_depasse, edp_lot_isoles_camp_en_cours.rang_dtr_a_venir, edp_lot_isoles_camp_en_cours.rang_dtr_depasse_unqmt, edp_lot_isoles_camp_en_cours.rang_dtr_a_venir_unqmt, edp_lot_isoles_camp_en_cours.num_categorie, edp_lot_isoles_camp_en_cours.categorie_ecart_auj_DTR_jo, edp_lot_isoles_camp_en_cours.date_cat_ecart_auj_DTR_jo, edp_lot_isoles_camp_en_cours.date_DTR_jo_agg, taches_perimetre.id_tache, taches_perimetre."Référence tâche", taches_perimetre.elementdetravail_id, taches_perimetre.objetmaitre_id, taches_perimetre."Libellé GT", taches_perimetre."Libellé liste de gestion", taches_perimetre."Libellé nature de tâche", taches_perimetre."Libellé tâche", taches_perimetre."Famille de tâche", taches_perimetre."Libellé type GT", taches_perimetre."Libellé GT père", taches_perimetre."Type d'agence", taches_perimetre."Statut tâche", taches_perimetre."Date création tâche", taches_perimetre."Date échéance tâche", taches_perimetre."Date fin tâche", taches_perimetre.elementdetravail_role, taches_perimetre.postedetravail_id, taches_perimetre."Libellé Type Rôle Métier", taches_perimetre."Rôle tâche", taches_perimetre."Tâche en retard", taches_perimetre."Nb. jours de retard", taches_perimetre."Acteur clôture tâche", anomalie.ID AS id_anomalie, type_anomalie.ANOMALIEBLOQUANTE AS "Anomalie Bloquante", anomalie.DATECREATION AS "Date création anomalie", anomalie.DATELEVEEOULEVEEFORCEE AS "Date levée ou levée forcée", CASE WHEN (lower(anomalie.AGENTLEVEE_ID) LIKE '%batch%') THEN 'batch' ELSE substr(anomalie.AGENTLEVEE_ID, 1, instr(anomalie.AGENTLEVEE_ID, '|') -1 ) END AS "NNI agent levée", substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|') + 1, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) - instr(anomalie.AGENTLEVEE_ID, '|') - 1) || ' ' || substr(anomalie.AGENTLEVEE_ID, instr(anomalie.AGENTLEVEE_ID, '|', 1, 2) + 1) AS "Agent levée", decode(anomalie.STATUTANOMALIE, 0, 'en cours', 1, 'levée', 2, 'levée forcée', 3, 'annulée', 4, 'sans action') AS "Statut anomalie", type_anomalie.LIBELLELONG AS "Type d'anomalie", CASE WHEN (type_anomalie.CODETYPEANOMALIE IN ('220', '581', '1534', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1535', '1536', '1523', '1524', '1537', '1525', '1526', '1528', '1529', '1530', '1531', '1511', '1512', '1513', '1514', '1515', '1516', '1518', '1519', '1520', '1521', '1522')) THEN 1 ELSE 0 END AS "Code anomalie flux Mars"
            
            FROM edp_lot_isoles_camp_en_cours
LEFT JOIN gahfld.TANOMALIE anomalie ON edp_lot_isoles_camp_en_cours.id_edp_releve = anomalie.ELEMENTPOPULATION_ID
  AND mod(anomalie.ETATOBJET,2) = 0
LEFT JOIN gahfld.TPARAMTYPEANOMALIE type_anomalie ON anomalie.TYPEANOMALIE = type_anomalie.CODETYPEANOMALIE
  AND mod(type_anomalie.ETATOBJET,2) = 0
  AND anomalie.TYPEANOMALIE_ROLE = type_anomalie.CLASSETYPEANOMALIE
  AND mod(type_anomalie.ETATOBJET,2) = 0
LEFT JOIN taches_perimetre ON anomalie.ID = taches_perimetre.elementdetravail_id

            
            
		) edp_releve_et_taches
			)
		)
		

