--Motifs refus F200B
SELECT DISTINCT info.VAR_T_DATA, ee.EST_T_ETAT
FROM SUIVI.DEMANDE dem
JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
WHERE (dem.DEM_K_NAT = '8500' OR dem.DEM_K_NAT = '9906' OR dem.DEM_K_NAT = '8501' OR dem.DEM_K_NAT = '8502' OR dem.DEM_K_NAT = '8503' OR dem.DEM_K_NAT = '8504' OR dem.DEM_K_NAT = '8505' OR dem.DEM_K_NAT = '8506')
AND info.VAR_ID = '200049' -- R_MOTIF_NON_RECEVABLE
AND dem.DEM_D_DEMANDE > '01/05/2015'
ORDER BY EST_T_ETAT, VAR_T_DATA
;

--F120B1 LU DIST
SELECT * FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat on dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID 
JOIN AFFAIRE.VARIABLE var ON info.VAR_ID = var.VAR_ID
WHERE 1=1
AND DEM_B_IS_SGEL = 'N'
AND NAT_C_TYPE = 'F120B'
AND NAT_C_SOUS_TYPE = 'F120B1'
AND DEM_K_MODALITE_RDV = '1'
AND DEM_R_MEDIA_RECEPTION = 'B2B'
AND DEM_D_DEMANDE > '01/01/2016'
AND var.VAR_C_CODE = 'R_FORMULE_TARIFAIRE'
AND info.VAR_T_DATA = 'LU'
ORDER BY DEM_D_DEMANDE DESC
;

--Retour 456/457 (PDL en cours de migration)
SELECT AFF_T_DISCO FROM
 (
  SELECT AFF_T_DISCO,
  MAX(CASE WHEN info.VAR_ID = 200117 THEN info.VAR_T_DATA END) as K_RETOUR_DISWS
  FROM SUIVI.DEMANDE dem
  JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID 
  WHERE 1=1
  AND DEM_K_NAT IN (8634, 8635, 8642, 8643 ,8644, 8646, 8647,8624, 8625, 8500,8502, 8503,8505)
  AND info.VAR_ID =  200117
  AND DEM_D_DEMANDE > '01/01/2016'
  --AND DEM_D_DEMANDE < '01/10/2016'
  GROUP BY AFF_T_DISCO
 )
WHERE K_RETOUR_DISWS IN ('456', '457')
;

--Changement SI contractuel
SELECT SCN_APP_APPLICATION_CODE FROM T_SITUATION_CONTRACTUELLE
WHERE SCN_APP_REF_POINT = '19100144582481'
AND SCN_SITU_TYPE = 'C'
;

UPDATE T_SITUATION_CONTRACTUELLE SET SCN_APP_APPLICATION_CODE = 'QETGC'
WHERE SCN_APP_REF_POINT = '19100144582481'
AND SCN_SITU_TYPE = 'C'
;

--Suivi, taches, info var, dates (analyse pb migration)
SELECT * FROM
  (SELECT DISTINCT AFF_T_DISCO FROM SUIVI.DEMANDE dem
  JOIN SUIVI.NATURE nat on dem.DEM_K_NAT = nat.NAT_ID
  JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
  JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID 
  JOIN AFFAIRE.VARIABLE var ON info.VAR_ID = var.VAR_ID
  JOIN AFFAIRE.TACHE tac ON tac.AFF_ID = dem.DEM_ID
  JOIN AFFAIRE.ETAPE etp ON tac.ETP_ID = etp.ETP_ID
  JOIN AFFAIRE.STATUT sta ON tac.STA_ID = sta.STA_ID
  WHERE 1=1
  AND DEM_B_IS_SGEL = 'N'
  AND NAT_C_TYPE LIKE 'M0%'
  --AND NAT_C_SOUS_TYPE = 'F200BR'
  AND DEM_R_STATUT = 'AFF-ENCOURS'
  --AND DEM_K_MODALITE_RDV = '1'
  AND TRUNC(DEM_D_DEMANDE) = '13/05/2016'
  --AND dem.DEM_D_CLOTURE > '14/05/2016'
  --AND etp.ETP_C_CODE = 'F200B-UH-C5-R05-E5'
  --AND sta.STA_T_LIB = 'Terminée'
  --AND var.VAR_C_CODE = 'K_RETOUR_DISB2B'
  --AND info.VAR_T_DATA = 'SGE229'
  )
;

--Récuperation du code tarif d'un point à partir de la dernière souscription / modification contractuelle
SELECT VAR_T_DATA FROM
AFFAIRE.INFO_VARIABLE info
JOIN AFFAIRE.VARIABLE var ON info.VAR_ID = var.VAR_ID
WHERE AFF_ID IN (
SELECT DEM_ID FROM (
  SELECT DEM_ID, AFF_T_DISCO, DEM_ID_PRM, DEM_R_STATUT, DEM_D_DEMANDE, DEM_K_NAT
  FROM SUIVI.DEMANDE dem
  WHERE 1=1
  AND DEM_K_NAT IN ('8629','8634','8635','8636','8642','8643','8644','8645','8624','8625','8626')
  AND DEM_R_STATUT = 'AFF-TERMINEE'
  AND DEM_ID_PRM = '14408827703047'
  ORDER BY DEM_D_DEMANDE DESC
  )
WHERE ROWNUM <= 1
)
AND VAR_C_CODE IN ('N_CODE_TARIF_REAL', 'N_CODE_TARIF')
AND ROWNUM <=1
;
--F180B1 passantes sur tarifs manuels avec mailles
SELECT dem.AFF_T_DISCO, dem.DEM_ID_PRM, mai.MAI_T_REGION, mai.MAI_T_COMPTAGE
FROM SUIVI.DEMANDE dem
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
JOIN SUIVI.NATURE nat on dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID 
JOIN AFFAIRE.VARIABLE var ON info.VAR_ID = var.VAR_ID
WHERE 1=1
AND DEM_B_IS_SGEL = 'N'
AND NAT_C_TYPE = 'F180'
AND NAT_C_SOUS_TYPE = 'F180B1'
AND DEM_R_STATUT = 'AFF-TERMINEE'
AND ee.EST_T_ETAT LIKE '%réalisée%'
AND DEM_D_DEMANDE > TO_DATE('01/03/15', 'DD/MM/YY')
AND var.VAR_C_CODE = 'N_CODE_TARIF'
AND info.VAR_T_DATA IN ('6130', '6150', '6160', '6180', '6700', '6720')
--AND frn.FRN_C_ACTEUR = 'ACM_030'
--AND dem.DEM_ID_PRM LIKE '015%'
;

-- Volumétrie 16/05
SELECT TRUNC(dem.DEM_D_DEMANDE),  COUNT(*)
FROM SUIVI.DEMANDE dem
WHERE 1=1
AND dem.DEM_D_DEMANDE > '10/05/2016'
AND DEM_D_DEMANDE < '20/05/2016'
AND dem.DEM_K_NAT IN (8635,8643, 8647, 8625)
AND dem.DEM_B_IS_SGEL = 'N'
GROUP BY TRUNC(dem.DEM_D_DEMANDE)
ORDER BY 1
;

--Demande avec rdv après 21h
SELECT COUNT(1) FROM(
SELECT DISTINCT tac.AFF_ID, TO_CHAR(tac.TAC_D_CREATION, 'HH24') HEURE
FROM AFFAIRE.TACHE tac
JOIN SUIVI.DEMANDE dem On dem.DEM_ID = tac.AFF_ID
WHERE ETP_ID IN
(
SELECT ETP_ID FROM AFFAIRE.ETAPE
WHERE ETP_C_CODE  = 'F120B-UH-C5-R02-D2'
)
--AND TO_CHAR(tac.TAC_D_CREATION, 'HH24') >= '21'
--AND TO_CHAR(tac.TAC_D_CREATION, 'HH24') <= '04'
AND dem.DEM_K_NAT IN
(
SELECT nat.NAT_ID FROM SUIVI.NATURE nat
WHERE 1=1
AND nat.NAT_C_TYPE = 'F120B'
AND nat.NAT_C_SOUS_TYPE = 'F120B1'
)
--AND dem.DEM_K_MODALITE_RDV = '2'
AND dem.DEM_D_DEMANDE > TO_DATE('01/06/2016', 'DD/MM/YYYY')
)
;

--Utilisation des WS par FRN
SELECT PRS, T_CME_VERSION, FRN, COUNT(1) as VOLUMETRIE FROM
(
SELECT DISTINCT dem.AFF_T_DISCO as AFF, dem.DEM_ID_PRM as PDL, dem.DEM_D_DEMANDE as DATE_DEM, frn.FRN_T_ACTEUR as FRN, nat.NAT_C_PRESTATION as PRS,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_CME_VERSION'
) THEN info.VAR_T_DATA END) as T_CME_VERSION
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID
WHERE 1=1
AND dem.DEM_B_IS_SGEL = 'N'
AND dem.DEM_R_MEDIA_RECEPTION = 'B2B'
AND dem.DEM_D_DEMANDE > TO_DATE('01/01/2017', 'DD/MM/YYYY')
AND nat.NAT_C_PRESTATION IN ('F100B', 'F120B', 'F130B', 'F140', 'F180')
AND info.VAR_ID IN (SELECT VAR_ID FROM AFFAIRE.VARIABLE WHERE VAR_C_CODE IN ('T_CME_VERSION'))
GROUP BY dem.AFF_T_DISCO, dem.DEM_ID_PRM, dem.DEM_D_DEMANDE, frn.FRN_T_ACTEUR, nat.NAT_C_PRESTATION
)
GROUP BY T_CME_VERSION, FRN, PRS
ORDER BY 1
;

--Catégorie client
SELECT * FROM
(
SELECT DISTINCT dem.AFF_T_DISCO as AFF, dem.DEM_ID_PRM as PDL, dem.DEM_R_MEDIA_RECEPTION, nat.NAT_C_PRESTATION, nat.NAT_C_SOUS_TYPE,  dem.DEM_D_DEMANDE as DATE_DEM,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'K_RETOUR_DISB2B'
) THEN info.VAR_T_DATA END) as K_RETOUR_DISB2B,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_RETOUR_DISB2B'
) THEN info.VAR_T_DATA END) as T_RETOUR_DISB2B,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'K_COURANT_CAT_CLIENT'
) THEN info.VAR_T_DATA END) as K_COURANT_CAT_CLIENT,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'R_CLIENT_CATEGORIE'
) THEN info.VAR_T_DATA END) as R_CLIENT_CATEGORIE
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID
WHERE 1=1
AND dem.DEM_B_IS_SGEL = 'N'
AND dem.DEM_D_DEMANDE > TO_DATE('01/01/2016', 'DD/MM/YYYY')
AND dem.DEM_D_DEMANDE < TO_DATE('01/06/2016', 'DD/MM/YYYY')
AND frn.FRN_T_ACTEUR = 'EDF Commerce'
AND nat.NAT_C_PRESTATION IN ('F100B', 'F120B', 'F130B', 'F140', 'F180', 'F200B', 'M007')
AND info.VAR_ID IN (SELECT VAR_ID FROM AFFAIRE.VARIABLE WHERE VAR_C_CODE IN ('K_RETOUR_DISB2B', 'T_RETOUR_DISB2B', 'K_COURANT_CAT_CLIENT', 'R_CLIENT_CATEGORIE'))
GROUP BY dem.AFF_T_DISCO, dem.DEM_ID_PRM, dem.DEM_D_DEMANDE, dem.DEM_R_MEDIA_RECEPTION, nat.NAT_C_PRESTATION, nat.NAT_C_SOUS_TYPE
)
WHERE 1=1
AND K_RETOUR_DISB2B IN ('SGE431', 'SGE479', 'SGE484', 'SGE4A1', 'SGE4B8', 'SGE4B9', 'SGE4D3')
;

--Afficher les caractéristiques d'un PDL
SELECT COUNT(*), SI FROM(
SELECT DISTINCT prm.PRM_ID as PDL, situ.SCN_APP_APPLICATION_CODE as SI
/*
,scm.SCM_DC_STRUCTURE_COMPTAGE_CODE, situ.SCN_APP_APPLICATION_CODE as SI, prm.PRM_DG_NUMERO_CONTRAT as FRN, situ.SCN_ST_TYPE_OFFRE_CODE "TYPE OFFRE", prm.PRM_SC_ETAT_CONTRACTUEL_CODE as SCN,
situ.SCN_ST_FORM_TARIF_ACHEMIN as FTA, situ.SCN_CF_CATEGORIE_CODE as CAT, alim.SAL_ETAT_ALIM_CODE as SAL, SCN_ST_CODE_TARIF_ACH_DISCO as TARIF, eqeCPT.EQE_MC_NB_CADRANS as NB_CADRANS,
situ.SCN_GF_CALENDRIER_FOURN_CODE as CALENDRIER, situ.SCN_ST_P_SOUSCRITE_MAX_V as PS, talim.ALI_PUISS_RACCO_SOUTI_V as P_RAC, eqeDJ.EQE_DJ_INT_REGLAGE_V as PDJ, eqeDJ.EQE_DJ_CALIBRE_CODE as CDJ,
eqeCPT.EQE_CP_NB_FILS as NB_FILS, prm.PRM_DG_COMMENTAIRE as FLAG, prm.PRM_TECH_DATE_MAJ,
prm.PRM_AIN_LIGNE2 as LIGNE2, prm.PRM_AIN_LIGNE3 as LIGNE3, prm.PRM_AIN_LIGNE4 as LIGNE4, prm.PRM_AIN_LIGNE5 as LIGNE5, prm.PRM_AIN_LIGNE6 as LIGNE6
*/
FROM SGEL_PRM_SCH.T_PRM prm
LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
--LEFT JOIN SGEL_PRM_SCH.T_SITUATION_ALIMENTATION alim ON prm.SAL_ID = alim.SAL_ID
--LEFT JOIN SGEL_PRM_SCH.T_ALIMENTATION talim ON talim.ALI_ID = alim.ALI_PRINCIPALE_ID
--LEFT JOIN SGEL_PRM_SCH.T_SITUATION_COMPTAGE scm ON scm.SCM_ID = prm.SCM_ID
--LEFT JOIN SGEL_PRM_SCH.T_EQUIPEMENT eqeCPT ON eqeCPT.SCM_C_ID = prm.SCM_ID
--LEFT JOIN SGEL_PRM_SCH.T_EQUIPEMENT eqeDJ ON eqeDJ.EQE_ID = scm.EQE_DISJONCTEUR_ID
WHERE 1=1
--AND prm.PRM_ID = '09700144658747'
AND situ.SCN_ST_P_SOUSCRITE_MAX_V > '12'
--AND scm.SCM_DC_STRUCTURE_COMPTAGE_CODE = 'AMM'
--AND situ.SCN_APP_APPLICATION_CODE = 'GINKO'
--AND talim.ALI_PUISS_RACCO_SOUTI_V > '12'
--AND eqeCPT.EQE_CP_NB_FILS IN ('2', '3')
--AND eqeDJ.EQE_DJ_INT_REGLAGE_V > '60'
)
GROUP BY SI
;

--Date dernière MES
SELECT COUNT(*) FROM SGEL_PRM_SCH.T_PRM prm
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
WHERE PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC'
AND PRM_SC_DATE_DER_MES IS NULL
AND situ.SCN_APP_APPLICATION_CODE = 'GINKO'
--AND PRM_SC_DATE_PREMIERE_MES IS NOT NULL
AND PRM_SC_SEGMENT = 'C5'
;

--Replanifs BC5
SELECT COUNT(1) FROM C5.EME_CRT_AVA_PRS evt
JOIN C5.NOTIF_FIN_TRT notif ON notif.NFT_ID = evt.NFT_ID
WHERE EME_K_WKF = 'F120B-UH-C5-R02'
AND EME_C_CODE = 'PRS_MRDV'
AND notif.NFT_B_STATUT_SAF = 'OK'
AND evt.EME_D_CREATION > '01/01/16'
AND evt.EME_D_CREATION < '01/01/17'
;

--Nombre de compteurs déposés sans pose
SELECT TO_CHAR(EDI_D_CREATION, 'YYYY/MM/DD') as DATE_VOL, COUNT(1) as VOLUMETRIE
--SELECT *
FROM C5.CE12 ce12
WHERE CE12_T_INDEVT5 = 'D'
AND (
  SELECT T_IDPDL FROM C5.CE12 ce12_2
  WHERE ce12_2.T_IDPDL = ce12.T_IDPDL
  AND ce12_2.CE12_T_INDEVT5 IN ('P', 'C')
  AND ce12_2.EDI_D_CREATION >= ce12.EDI_D_CREATION
  AND ROWNUM < 2
)
IS NULL
AND ce12.EDI_D_CREATION > '01/04/2017'
GROUP BY TO_CHAR(EDI_D_CREATION, 'YYYY/MM/DD')
;

SELECT * FROM C5.CE12 ce12_2
WHERE ce12_2.T_IDPDL = 25857308247828
AND ce12_2.CE12_T_INDEVT5 IN ('P', 'C')
AND ce12_2.EDI_D_CREATION >= '30/05/17 02:39:36'
;

--Ecart date d'effet / date demande prestas Ginko téléop
SELECT DATE_ECART, COUNT(1) as VOLUMETRIE FROM (
SELECT DISTINCT dem.AFF_T_DISCO as AFFAIRE, TRUNC(dem.DEM_D_EFFET - dem.DEM_D_DEMANDE) as DATE_ECART
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN SGEL_IAP_SCH.T_AFFAIRE aff ON aff.AFF_ID = dem.AFF_T_DISCO
JOIN SGEL_IAP_SCH.T_PRESTATION t_pres ON t_pres.AFF_ID_SEQUENCE = aff.AFF_ID_SEQUENCE
JOIN SGEL_IAP_SCH.T_INTERVENTION_AFFAIRE ia ON ia.AFF_ID = dem.AFF_T_DISCO
JOIN SGEL_IAP_SCH.T_INTERVENTION t_inte ON ia.INT_ID = t_inte.INT_ID
JOIN SGEL_IAP_SCH.T_DEMANDE t_dema ON t_inte.INT_DEM_ID = t_dema.INT_DEM_ID
JOIN SGEL_IAP_SCH.T_PLANIFICATION t_plan ON t_inte.PLA_ID =  t_plan.PLA_ID
JOIN SGEL_IAP_SCH.T_STRUCTURE_TARIFAIRE t_stru ON t_stru.STR_TAR_ID = t_pres.PRE_DEM_STR_TAR_ID
JOIN SGEL_IAP_SCH.T_RECEVABILITE t_rece ON t_rece.PRE_REC_ID = t_pres.PRE_REC_ID
WHERE 1=1
AND dem.DEM_B_IS_SGEL IN ('O')
AND dem.DEM_B_IS_GINKO IN ('O')
AND dem.DEM_D_DEMANDE >= TO_DATE('01/01/2017', 'DD/MM/YYYY')
AND INT_DEM_MODEREA_CODE IN ('DIST')
)
GROUP BY DATE_ECART
ORDER BY 1
;

--Ecart date d'annulation / date demande
SELECT DATE_ECART, COUNT(1) as VOLUMETRIE FROM (
SELECT DATE_ANNULATION - TRUNC(DATE_DEMANDE) as DATE_ECART, AFFAIRE FROM (
SELECT DISTINCT dem.AFF_T_DISCO as AFFAIRE, dem.DEM_D_DEMANDE as DATE_DEMANDE, dem.DEM_D_EFFET as DATE_EFFET, TRUNC(tac.TAC_D_CREATION) as DATE_ANNULATION
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN SGEL_IAP_SCH.T_AFFAIRE aff ON aff.AFF_ID = dem.AFF_T_DISCO
JOIN SGEL_IAP_SCH.T_PRESTATION t_pres ON t_pres.AFF_ID_SEQUENCE = aff.AFF_ID_SEQUENCE
JOIN SGEL_IAP_SCH.T_INTERVENTION_AFFAIRE ia ON ia.AFF_ID = dem.AFF_T_DISCO
JOIN SGEL_IAP_SCH.T_INTERVENTION t_inte ON ia.INT_ID = t_inte.INT_ID
JOIN SGEL_IAP_SCH.T_DEMANDE t_dema ON t_inte.INT_DEM_ID = t_dema.INT_DEM_ID
JOIN SGEL_IAP_SCH.T_PLANIFICATION t_plan ON t_inte.PLA_ID =  t_plan.PLA_ID
JOIN SGEL_IAP_SCH.T_STRUCTURE_TARIFAIRE t_stru ON t_stru.STR_TAR_ID = t_pres.PRE_DEM_STR_TAR_ID
JOIN SGEL_IAP_SCH.T_RECEVABILITE t_rece ON t_rece.PRE_REC_ID = t_pres.PRE_REC_ID
JOIN AFFAIRE.TACHE tac ON tac.AFF_ID = dem.DEM_ID
JOIN AFFAIRE.ETAPE etp ON tac.ETP_ID = etp.ETP_ID
JOIN AFFAIRE.STATUT sta ON tac.STA_ID = sta.STA_ID
WHERE 1=1
AND dem.DEM_B_IS_SGEL IN ('O')
AND dem.DEM_R_STATUT IN ('AFF-ANNULEE')
AND dem.DEM_D_DEMANDE >= TO_DATE('01/01/2017', 'DD/MM/YYYY')
AND AFF_ANN_MOTIF IN ('DEMFRN')
AND INT_DEM_MODEREA_CODE IN ('DIST')
AND etp.ETP_C_CODE LIKE '%A1%'
AND sta.STA_T_LIB = 'Terminée'
)
)
GROUP BY DATE_ECART
ORDER BY 1;

--Nombre de demandes srv STM modifierDemandePublication avec plus d'un jour de délais sur mai et juin 
SELECT DELAIS, COUNT(3) as VOLUMETRIE FROM (
/*SELECT TO_CHAR(MAX(DATE_ECHANGE)-MIN(DATE_ECHANGE), 'YYYY/MM/DD HH24'), COUNT(1) as NOMBRE_TENTATIVES, PDL FROM (*/
SELECT TRUNC(MAX(DATE_ECHANGE))-TRUNC(MIN(DATE_ECHANGE)) as DELAIS, COUNT(1) as NOMBRE_TENTATIVES, PDL FROM (
SELECT /*+ORDERED_PREDICATES*/ DISTINCT msg.ID_ECHANGE as ECH, MAX(CASE WHEN obj.ID_TYPE_OBJET = 1 THEN obj.ID_OBJET END) as PDL, msg.DT_ECHANGE as DATE_ECHANGE
FROM TUBE.TUBE_MESSAGE msg
LEFT JOIN TUBE.TUBE_ECHANGE ech ON ech.ID_ECHANGE = msg.ID_ECHANGE
JOIN TUBE.TUBE_MESSAGE msg_parent ON msg_parent.ID_MESSAGE = msg.ID_MESSAGE_PARENT
LEFT JOIN TUBE.TUBE_ECHANGE_OBJET obj ON obj.ID_ECHANGE = ech.ID_ECHANGE
WHERE 1=1
AND msg.DT_ECHANGE >= TO_DATE('01/05/2017 14:43:30', 'DD/MM/YYYY HH24:Mi:SS')
AND msg_parent.ID_OPERATION_SERVICE IN
(
SELECT op.ID_OPERATION_SERVICE
FROM TUBE.TUBE_OPERATION_SERVICE op
JOIN TUBE.TUBE_SERVICE srv ON srv.ID_SERVICE = op.ID_SERVICE
WHERE 1=1
AND srv.C_SERVICE LIKE '%SCI-GINKO-GestionMesures-WS-v1%'
AND op.C_OPERATION LIKE '%demanderPublicationRecurrenteMesures%'
)
AND msg.ID_OPERATION_SERVICE IN
(
SELECT op.ID_OPERATION_SERVICE
FROM TUBE.TUBE_OPERATION_SERVICE op
JOIN TUBE.TUBE_SERVICE srv ON srv.ID_SERVICE = op.ID_SERVICE
WHERE 1=1
AND srv.C_SERVICE LIKE '%BA-STM-DemandePublication%'
AND op.C_OPERATION LIKE '%modifierDemandePublication%'
)
GROUP BY msg.ID_ECHANGE, msg.DT_ECHANGE
)
GROUP BY PDL
ORDER BY 1 DESC
)
GROUP BY DELAIS
ORDER BY 1
;

--ACM
SELECT * FROM CONTRAT.CONTRAT ctr
JOIN CONTRAT.ASS_CTR_TAM_ACM ass ON ass.CTR_ID = ctr.CTR_ID
JOIN CONTRAT.ACTEUR_MARCHE acm ON acm.ACM_ID = ass.ACM_ID
WHERE CTR_T_NUM IN ('1059653', '1201652', '1060654')
;

--F120 et F140 le même jour
SELECT TO_CHAR(DATE_EFFET, 'YYYY/MM/DD') as DATE_VOL, COUNT(1) as VOLUMETRIE FROM(
SELECT DISTINCT dem.DEM_ID_PRM as POINT, TRUNC(dem.DEM_D_EFFET) as DATE_EFFET
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
WHERE 1=1
AND dem.DEM_D_DEMANDE >= TO_DATE('01/07/2017', 'DD/MM/YYYY')
AND nat.NAT_C_PRESTATION = 'F140'
AND ee.EST_T_ETAT = 'Close, prestation réalisée'
AND (
SELECT MAX(dem2.AFF_T_DISCO)
FROM SUIVI.DEMANDE dem2
JOIN SUIVI.NATURE nat2 ON dem2.DEM_K_NAT = nat2.NAT_ID
JOIN SUIVI.ETAT_STATUT ee2 ON dem2.DEM_K_EST_EXT = ee2.EST_ID
WHERE nat2.NAT_C_PRESTATION = 'F120B'
AND dem2.DEM_ID_PRM = dem.DEM_ID_PRM
AND TRUNC(dem2.DEM_D_EFFET) = TRUNC(dem.DEM_D_EFFET)
AND ee.EST_T_ETAT = 'Close, prestation réalisée'
) IS NOT NULL
)
GROUP BY TO_CHAR(DATE_EFFET, 'YYYY/MM/DD')
ORDER BY 1
;

--Résil et souscription le même jour
SELECT TO_CHAR(DATE_EFFET, 'YYYY/MM/DD') as DATE_VOL, COUNT(1) as VOLUMETRIE FROM(
SELECT situ1.SCN_APP_REF_POINT, situ1.SCN_SIT_DATE_DEBUT as DATE_EFFET
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ1
WHERE 1=1
AND TRUNC(situ1.SCN_SIT_DATE_DEBUT) > '01/08/17'
AND (
SELECT MAX(SCN_ID)
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ2
WHERE 1=1
AND situ2.SCN_APP_REF_POINT = situ1.SCN_APP_REF_POINT
AND TRUNC(situ2.SCN_SIT_DATE_FIN) >= TRUNC(situ1.SCN_SIT_DATE_DEBUT)
AND TRUNC(situ2.SCN_SIT_DATE_FIN) - TRUNC(situ1.SCN_SIT_DATE_DEBUT) <= 1
) IS NOT NULL
)
GROUP BY TO_CHAR(DATE_EFFET, 'YYYY/MM/DD')
ORDER BY 1
;

--Délais avancement souscription abonnements récurrents
SELECT DELAIS_S, COUNT(1) as VOLUMETRIE
FROM
(
	SELECT AFFAIRE,
	CASE
	WHEN DELAIS_S <= 10 THEN '1 - Moins de 10 secondes'
	WHEN DELAIS_S > 10 AND DELAIS_S <= 60 THEN '2 - Moins d''une minute'
	WHEN DELAIS_S > 60 AND DELAIS_S <= 600 THEN '3 - Moins de 10 minutes'
	WHEN DELAIS_S > 600 AND DELAIS_S <= 3600 THEN '4 - Moins d''une heure'
	WHEN DELAIS_S > 3600 AND DELAIS_S <= 6*3600 THEN '5 - Moins de 6 heures'
	WHEN DELAIS_S > 6*3600 AND DELAIS_S <= 24*3600 THEN '6 - Moins d''un jour'
	WHEN DELAIS_S > 24*3600 AND DELAIS_S <= 2*24*3600 THEN '7 - Moins de deux jours'
	WHEN DELAIS_S > 2*24*3600 AND DELAIS_S <= 7*24*3600 THEN '8 - Moins d''une semaine'
	WHEN DELAIS_S > 7*24*3600 THEN '9 - Plus d''une semaine'
	END as DELAIS_S
	FROM
	(
		SELECT AFFAIRE, TRUNC((MAX(D_JALON) - MIN(D_JALON))*24*60*60) as DELAIS_S
		FROM
		(
			SELECT DISTINCT dem.AFF_T_DISCO as AFFAIRE, dem.DEM_ID_PRM as POINT, nat.NAT_C_PRESTATION as PRESTATION, nat.NAT_C_SOUS_TYPE as PRS_OPTION, jal.JAL_ETAT_EXTERNE, jal.JAL_DATE_JALON as D_JALON
			FROM SUIVI.DEMANDE dem
			JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
			JOIN SGEL_IAP_SCH.T_AFFAIRE aff ON aff.AFF_ID = dem.AFF_T_DISCO
			JOIN SGEL_IAP_SCH.T_JALON jal ON jal.AFF_ID_SEQUENCE =  aff.AFF_ID_SEQUENCE
			WHERE 1=1
			AND dem.DEM_B_IS_SGEL IN ('O')
			AND dem.DEM_B_IS_GINKO IN ('O')
			AND nat.NAT_C_PRESTATION IN ('F305', 'F300C')
			AND dem.DEM_D_DEMANDE >= TO_DATE('01/10/2017', 'DD/MM/YYYY')
			ORDER BY AFFAIRE, JAL_DATE_JALON
		)
		GROUP BY AFFAIRE
	)
	ORDER BY 1
)
GROUP BY DELAIS_S
ORDER BY 1
;

--F180 GINKO cible + source
SELECT AFFAIRE, POINT, PRESTATION, OPT, FOURNISSEUR, STATUT, ETAT_EXTERNE, ETAT_INTERNE, DATE_DEMANDE, DATE_EFFET, MEDIA, REGION, TERRITOIRE, FTA_SOURCE, FTA_CIBLE, CAL_SOURCE, CAL_CIBLE
FROM
(
SELECT DISTINCT dem.AFF_T_DISCO as AFFAIRE,
dem.DEM_ID_PRM as POINT,
nat.NAT_C_PRESTATION as PRESTATION,
frn.FRN_T_ACTEUR as FOURNISSEUR,
dem.DEM_R_STATUT as STATUT,
ee.EST_T_ETAT as ETAT_EXTERNE,
ei.EST_T_ETAT as ETAT_INTERNE,
dem.DEM_D_DEMANDE as DATE_DEMANDE,
dem.DEM_D_EFFET as DATE_EFFET,
dem.DEM_R_MEDIA_RECEPTION as MEDIA,
mai.MAI_T_REGION as REGION,
mai.MAI_T_TERRITOIRE as TERRITOIRE,
dem.DEM_B_IS_SGEL as SGEL,
dem.DEM_B_IS_GINKO as GINKO,
t_dema.INT_DEM_MODEREA_CODE as MODE_REAL,
t_pres.PRE_FICHECAS_CODE as OPT,
situ.SCN_ST_FORM_TARIF_ACHEMIN as FTA_SOURCE,
t_stru.STR_TAR_ST_FORTARACH as FTA_CIBLE,
situ.SCN_GF_CALENDRIER_FOURN_CODE as CAL_SOURCE,
t_stru.STR_TAR_ST_GFRN_CAL_CODE as CAL_CIBLE, 
situ.SCN_TECH_DATE_MAJ,
ROW_NUMBER() OVER (ORDER BY dem.AFF_T_DISCO,
situ.SCN_TECH_DATE_MAJ DESC) AS ROWNUMBER
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN SGEL_IAP_SCH.T_AFFAIRE aff ON aff.AFF_ID = dem.AFF_T_DISCO
JOIN SGEL_IAP_SCH.T_PRESTATION t_pres ON t_pres.AFF_ID_SEQUENCE = aff.AFF_ID_SEQUENCE
LEFT JOIN SGEL_IAP_SCH.T_INTERVENTION_AFFAIRE ia ON ia.AFF_ID = dem.AFF_T_DISCO
LEFT JOIN SGEL_IAP_SCH.T_INTERVENTION t_inte ON ia.INT_ID = t_inte.INT_ID
LEFT JOIN SGEL_IAP_SCH.T_DEMANDE t_dema ON t_inte.INT_DEM_ID = t_dema.INT_DEM_ID
LEFT JOIN SGEL_IAP_SCH.T_PLANIFICATION t_plan ON t_inte.PLA_ID =  t_plan.PLA_ID
LEFT JOIN SGEL_IAP_SCH.T_STRUCTURE_TARIFAIRE t_stru ON t_stru.STR_TAR_ID = t_pres.PRE_DEM_STR_TAR_ID
JOIN SGEL_IAP_SCH.T_RECEVABILITE t_rece ON t_rece.PRE_REC_ID = t_pres.PRE_REC_ID
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON situ.SCN_APP_REF_POINT = dem.DEM_ID_PRM
WHERE 1=1
AND dem.DEM_B_IS_SGEL IN ('O')
AND nat.NAT_C_PRESTATION IN ('F180')
AND dem.DEM_D_DEMANDE >= TO_DATE('01/08/2017', 'DD/MM/YYYY')
AND situ.SCN_SITU_TYPE = 'H'
AND TRUNC(situ.SCN_TECH_DATE_MAJ) < TRUNC(dem.DEM_D_EFFET)
ORDER BY dem.AFF_T_DISCO, situ.SCN_TECH_DATE_MAJ DESC
) tbl1
JOIN
(
SELECT MIN(ROWNUMBER) as ROWNUMBER, AFF_T_DISCO
FROM(
SELECT ROW_NUMBER() OVER (ORDER BY dem.AFF_T_DISCO, situ.SCN_TECH_DATE_MAJ DESC) AS ROWNUMBER, dem.AFF_T_DISCO, situ.SCN_TECH_DATE_MAJ
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON situ.SCN_APP_REF_POINT = dem.DEM_ID_PRM
WHERE 1=1
AND dem.DEM_B_IS_SGEL IN ('O')
AND nat.NAT_C_PRESTATION IN ('F180')
AND dem.DEM_D_DEMANDE >= TO_DATE('01/08/2017', 'DD/MM/YYYY')
AND situ.SCN_SITU_TYPE = 'H'
AND TRUNC(situ.SCN_TECH_DATE_MAJ) < TRUNC(dem.DEM_D_EFFET)
ORDER BY dem.AFF_T_DISCO, situ.SCN_TECH_DATE_MAJ DESC
)
GROUP BY AFF_T_DISCO
ORDER BY 1
) tbl2
ON tbl1.ROWNUMBER = tbl2.ROWNUMBER
;

--F180B2 DISCO cible + source
SELECT AFFAIRE, POINT, FOURNISSEUR, STATUT, ETAT_EXTERNE, ETAT_INTERNE, DATE_DEMANDE, DATE_EFFET, MEDIA, REGION, TERRITOIRE, CTA_FTA_CODE as FTA_SOURCE,
DECODE(R_FORMULE_TARIFAIRE,
'MU-DT', 'BTINFMUDT',
'CU-ST', 'BTINFCUST',
'LU', 'BTINFLU'
) as FTA_CIBLE
 FROM
(
SELECT DISTINCT
dem.AFF_T_DISCO as AFFAIRE,
dem.DEM_ID_PRM as POINT,
frn.FRN_T_ACTEUR as FOURNISSEUR,
dem.DEM_R_STATUT as STATUT,
ee.EST_T_ETAT as ETAT_EXTERNE,
ei.EST_T_ETAT as ETAT_INTERNE,
dem.DEM_D_DEMANDE as DATE_DEMANDE,
dem.DEM_D_EFFET as DATE_EFFET,
dem.DEM_R_MEDIA_RECEPTION as MEDIA,
mai.MAI_T_REGION as REGION,
mai.MAI_T_TERRITOIRE as TERRITOIRE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'R_FORMULE_TARIFAIRE'
) THEN info.VAR_T_DATA END) as R_FORMULE_TARIFAIRE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'N_CODE_TARIF_ANC'
) THEN info.VAR_T_DATA END) as N_CODE_TARIF_ANC
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID
WHERE 1=1
AND dem.DEM_B_IS_SGEL IN ('N')
AND nat.NAT_C_PRESTATION IN ('F180')
AND nat.NAT_C_SOUS_TYPE IN ('F180B2')
AND dem.DEM_D_DEMANDE >= TO_DATE('01/08/2017', 'DD/MM/YYYY')
AND info.VAR_ID IN (SELECT VAR_ID FROM AFFAIRE.VARIABLE WHERE VAR_C_CODE IN ('R_FORMULE_TARIFAIRE', 'N_CODE_TARIF_ANC'))
GROUP BY dem.AFF_T_DISCO, dem.DEM_ID_PRM, frn.FRN_T_ACTEUR, dem.DEM_R_STATUT, ee.EST_T_ETAT, ei.EST_T_ETAT, dem.DEM_D_DEMANDE, dem.DEM_D_EFFET, dem.DEM_R_MEDIA_RECEPTION, mai.MAI_T_REGION, mai.MAI_T_TERRITOIRE
)
JOIN SGEL_TRV_SCH.T_CODE_TARIF tar ON N_CODE_TARIF_ANC = tar.CTA_CODE
;

--Volumétrie des situations contractuelles actives par calendrier (avec info profilage)
SELECT COUNT(1), CALENDRIER, PROFILABLE
FROM
(
SELECT DISTINCT situ.SCN_ID, situ.SCN_GF_CALENDRIER_FOURN_CODE as CALENDRIER, sTemp.STT_PROFILAGE_AUTORISE as PROFILABLE
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ
JOIN SGEL_SCH.T_CALENDRIER cal ON cal.CAL_CODE = situ.SCN_GF_CALENDRIER_FOURN_CODE
JOIN SGEL_SCH.T_STRUCTURE_TEMPORELLE sTemp ON sTemp.STT_Id = cal.STT_ID
WHERE situ.SCN_SITU_TYPE = 'C'
AND situ.SCN_SIT_ETAT_CODE = 'actif'
AND situ.SCN_APP_APPLICATION_CODE = 'GINKO'
)
GROUP BY CALENDRIER, PROFILABLE
ORDER BY 1 DESC
;

--Volumétrie des situations contractuelles actives par fournisseur et SI
SELECT *
FROM (
SELECT COUNT(1) as VOLUMETRIE, situ.SCN_CF_NUMERO_CONTRAT as CONTRAT, situ.SCN_APP_APPLICATION_CODE as SI 
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ
WHERE 1=1
AND situ.SCN_APP_APPLICATION_CODE IN ('GINKO', 'QETGC')
AND situ.SCN_SITU_TYPE = 'C'
AND situ.SCN_SIT_ETAT_CODE = 'actif'
GROUP BY situ.SCN_CF_NUMERO_CONTRAT, situ.SCN_APP_APPLICATION_CODE
ORDER BY 1 DESC
) vol
JOIN (
SELECT DISTINCT acm.ACM_T_LIB as FOURNISSEUR, ctr.CTR_T_NUM as GRD_ID, acm.ACM_C_CODE as ACM_ID, acta.ACT_C_EIC as EIC_ID
FROM CONTRAT.ASS_CTR_TAM_ACM acta
JOIN CONTRAT.ACTEUR_MARCHE acm ON acm.ACM_ID = acta.ACM_ID
JOIN CONTRAT.TYPE_ACTEUR tam ON tam.TAM_ID = acta.TAM_ID
JOIN CONTRAT.CONTRAT ctr ON ctr.CTR_ID = acta.CTR_ID
WHERE 1=1
AND tam.TAM_C_CODE LIKE 'F%'
) acm
ON acm.GRD_ID = vol.CONTRAT
;

--Situations contractuelles actives
SELECT COUNT(1), situ.SCN_APP_APPLICATION_CODE
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ
WHERE 1=1
AND situ.SCN_APP_APPLICATION_CODE IN ('GINKO', 'QETGC')
AND situ.SCN_SITU_TYPE = 'C'
--AND situ.SCN_SIT_ETAT_CODE = 'actif' !champ de mauvaise qualité!
AND situ.SCN_SIT_DATE_FIN IS NULL
AND situ.SCN_CF_CATEGORIE_CODE = 'PRO'
AND situ.SCN_CF_NUMERO_CONTRAT = 'GRD-F006'
GROUP BY situ.SCN_APP_APPLICATION_CODE
ORDER BY 1 DESC
;

355271	QETGC
98752	GINKO

--SUPER HC et Dolce WE
SELECT COUNT(1), situ.SCN_APP_APPLICATION_CODE, situ.SCN_GF_CALENDRIER_FOURN_CODE
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ
WHERE 1=1
AND situ.SCN_APP_APPLICATION_CODE IN ('GINKO', 'QETGC')
AND situ.SCN_SITU_TYPE = 'C'
--AND situ.SCN_SIT_ETAT_CODE = 'actif' !champ de mauvaise qualité!
AND situ.SCN_SIT_DATE_FIN IS NULL
AND situ.SCN_GF_CALENDRIER_FOURN_CODE IN ('FP000001', 'FP007644')
GROUP BY situ.SCN_GF_CALENDRIER_FOURN_CODE, situ.SCN_APP_APPLICATION_CODE
;

493	GINKO	FP000001
302	GINKO	FP007644

--EDF OH PRO
SELECT COUNT(1)
FROM SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ
WHERE 1=1
AND situ.SCN_APP_APPLICATION_CODE IN ('GINKO', 'QETGC')
AND situ.SCN_SITU_TYPE = 'C'
--AND situ.SCN_SIT_ETAT_CODE = 'actif' !champ de mauvaise qualité!
AND situ.SCN_SIT_DATE_FIN IS NULL
AND situ.SCN_CF_NUMERO_CONTRAT = 'PROTOC-501'
AND situ.SCN_CF_CATEGORIE_CODE = 'PRO'
;

741314

--Version appli
SELECT VER_T_VERSION_SGE as RES FROM TECHNIQUE.VERSION
WHERE REGEXP_LIKE (VER_T_VERSION_SGE, '^[78][\._]')
ORDER BY VER_D_EXECUTION DESC

--RIF sèches
WITH a AS (
    SELECT dem.AFF_T_DISCO as AFFAIRE, dem.DEM_ID_PRM as POINT, nat.NAT_C_PRESTATION as PRESTATION, t_pres.PRE_FICHEOPTION_CODE as OPT, dem.DEM_D_DEMANDE as DATE_DEMANDE, dem.DEM_R_STATUT
    , DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANK
    FROM SUIVI.DEMANDE dem
    JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
    JOIN SGEL_IAP_SCH.T_AFFAIRE aff ON aff.AFF_ID = dem.AFF_T_DISCO
    LEFT JOIN SGEL_IAP_SCH.T_PRESTATION t_pres ON t_pres.AFF_ID_SEQUENCE = aff.AFF_ID_SEQUENCE
    WHERE 1=1
    AND dem.DEM_B_IS_SGEL IN ('O')
    AND dem.DEM_B_IS_GINKO IN ('O')
    AND dem.DEM_R_STATUT <> 'AFF-ANNULEE'
    AND nat.NAT_C_PRESTATION NOT IN ('F300C', 'F305')
    AND dem.DEM_D_DEMANDE >= TO_DATE('01/05/2019', 'DD/MM/YYYY')
)

SELECT * FROM a
JOIN a b ON (a.POINT = b.POINT and b.RANK = a.RANK + 1)
WHERE 1=1
AND a.PRESTATION = ('F140')
AND a.OPT = ('F140BO2')
;

--Analyse codes 471
WITH a AS
(
    SELECT DISTINCT
    dem.AFF_T_DISCO as AFFAIRE,
    dem.DEM_ID_PRM as POINT,
    dem.DEM_D_DEMANDE as DATE_DEMANDE,
    MAX(CASE WHEN info.VAR_ID = (
    SELECT VAR_ID FROM AFFAIRE.VARIABLE
    WHERE VAR_C_CODE = 'K_RETOUR_DISWS'
    ) THEN info.VAR_T_DATA END) as K_RETOUR_DISWS,
    MAX(CASE WHEN info.VAR_ID = (
    SELECT VAR_ID FROM AFFAIRE.VARIABLE
    WHERE VAR_C_CODE = 'T_RETOUR_DISWS'
    ) THEN info.VAR_T_DATA END) as T_RETOUR_DISWS,
    MAX(CASE WHEN info.VAR_ID = (
    SELECT VAR_ID FROM AFFAIRE.VARIABLE
    WHERE VAR_C_CODE = 'R_FAISABILITE_PRESTATION'
    ) THEN info.VAR_T_DATA END) as R_FAISABILITE_PRESTATION
    FROM SUIVI.DEMANDE dem
    JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
    LEFT JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
    JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
    JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
    LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
    JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID
    WHERE 1=1
    AND dem.DEM_B_IS_SGEL IN ('N')
    AND dem.DEM_B_IS_GINKO IN ('N')
    AND nat.NAT_C_PRESTATION IN ('F120B')
    AND nat.NAT_C_SOUS_TYPE IN ('F120B2')
    AND dem.DEM_D_DEMANDE >= TO_DATE('10/05/2019', 'DD/MM/YYYY')
    AND dem.DEM_D_DEMANDE <= TO_DATE('20/05/2019', 'DD/MM/YYYY')
    AND info.VAR_ID IN (SELECT VAR_ID FROM AFFAIRE.VARIABLE WHERE VAR_C_CODE IN ('K_RETOUR_DISWS', 'T_RETOUR_DISWS', 'R_FAISABILITE_PRESTATION'))
    GROUP BY dem.AFF_T_DISCO, dem.DEM_ID_PRM, dem.DEM_D_DEMANDE
)

SELECT COUNT(1) as VOLUMETRIE, FAISABILITE, ECART_SF, RETOUR_DISCO, ROUTAGE
FROM
(
    SELECT AFFAIRE, POINT, DATE_DEMANDE,R_FAISABILITE_PRESTATION as FAISABILITE, 
    CASE
        WHEN T_RETOUR_DISWS LIKE '%INDEX DE REOUVERTURE%' THEN 'INDEX DE REOUVERTURE'
        WHEN T_RETOUR_DISWS LIKE '%ECART NON SATISFAIT, CONSOMMATION : -%' THEN 'ECART NON SATISFAIT -'
        WHEN T_RETOUR_DISWS LIKE '%ECART NON SATISFAIT, CONSOMMATION : +%' THEN 'ECART NON SATISFAIT +'
        WHEN T_RETOUR_DISWS LIKE '%INDEX SAISI DOIT ETRE%' THEN 'INDEX SAISI DOIT ETRE'
        WHEN T_RETOUR_DISWS LIKE '%LA CONSOMMATION%' THEN 'LA CONSOMMATION'
        WHEN T_RETOUR_DISWS LIKE '%DATE%' THEN 'DATE'
        WHEN T_RETOUR_DISWS = 'ERREUR VALIDATION MF' THEN 'ERREUR VALIDATION MF'
        ELSE T_RETOUR_DISWS
    END RETOUR_DISCO,
    CASE
        WHEN T_RETOUR_DISWS LIKE '%INDEX DE REOUVERTURE%' THEN 'NON'
        WHEN T_RETOUR_DISWS LIKE '%ECART NON SATISFAIT, CONSOMMATION : -%' THEN 'NON'
        WHEN T_RETOUR_DISWS = 'ERREUR VALIDATION MF' THEN 'NON'
        WHEN T_RETOUR_DISWS LIKE '%ECART NON SATISFAIT, CONSOMMATION : +%' THEN 'OUI'
        WHEN T_RETOUR_DISWS LIKE '%INDEX SAISI DOIT ETRE%' THEN 'OUI'
        WHEN T_RETOUR_DISWS LIKE '%LA CONSOMMATION%' THEN 'OUI'
        WHEN T_RETOUR_DISWS LIKE '%DATE%' THEN 'OUI'
        ELSE '?'
    END ECART_SF,
    CASE
        WHEN T_RETOUR_DISWS LIKE '%INDEX DE REOUVERTURE%' THEN ''
        WHEN T_RETOUR_DISWS LIKE '%ECART NON SATISFAIT, CONSOMMATION : -%' THEN ''
        WHEN T_RETOUR_DISWS = 'ERREUR VALIDATION MF' THEN ''
        WHEN T_RETOUR_DISWS LIKE '%ECART NON SATISFAIT, CONSOMMATION : +%' THEN 'SGE44C'
        WHEN T_RETOUR_DISWS LIKE '%INDEX SAISI DOIT ETRE%' THEN 'SGE43B'
        WHEN T_RETOUR_DISWS LIKE '%LA CONSOMMATION%' THEN 'SGE44B'
        WHEN T_RETOUR_DISWS LIKE '%DATE%' THEN 'SGE41C'
        ELSE '?'
    END ROUTAGE
    FROM a
    WHERE K_RETOUR_DISWS = '471'
)
GROUP BY RETOUR_DISCO, ECART_SF, ROUTAGE, FAISABILITE
ORDER BY 1 DESC
;

--Analyse codes retour DISCO
WITH a AS
(
    SELECT DISTINCT
    dem.AFF_T_DISCO as AFFAIRE,
    MAX(CASE WHEN info.VAR_ID = (
    SELECT VAR_ID FROM AFFAIRE.VARIABLE
    WHERE VAR_C_CODE = 'K_RETOUR_DISWS'
    ) THEN info.VAR_T_DATA END) as CODE_RETOUR,
    MAX(CASE WHEN info.VAR_ID = (
    SELECT VAR_ID FROM AFFAIRE.VARIABLE
    WHERE VAR_C_CODE = 'T_RETOUR_DISWS'
    ) THEN info.VAR_T_DATA END) as MESSAGE_RETOUR,
    MAX(CASE WHEN info.VAR_ID = (
    SELECT VAR_ID FROM AFFAIRE.VARIABLE
    WHERE VAR_C_CODE = 'R_FAISABILITE_PRESTATION'
    ) THEN info.VAR_T_DATA END) as FAISABILITE
    FROM SUIVI.DEMANDE dem
    JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
    LEFT JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
    JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
    JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
    LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
    JOIN AFFAIRE.INFO_VARIABLE info ON info.AFF_ID = dem.DEM_ID
    WHERE 1=1
    AND dem.DEM_B_IS_SGEL IN ('N')
    AND dem.DEM_B_IS_GINKO IN ('N')
    AND nat.NAT_C_PRESTATION IN ('F120B')
    AND nat.NAT_C_SOUS_TYPE IN ('F120B2')
    AND dem.DEM_D_DEMANDE >= TO_DATE('20/04/2019', 'DD/MM/YYYY')
    AND dem.DEM_D_DEMANDE <= TO_DATE('20/05/2019', 'DD/MM/YYYY')
    AND info.VAR_ID IN (SELECT VAR_ID FROM AFFAIRE.VARIABLE WHERE VAR_C_CODE IN ('K_RETOUR_DISWS', 'T_RETOUR_DISWS', 'R_FAISABILITE_PRESTATION'))
    GROUP BY dem.AFF_T_DISCO
)

SELECT COUNT(1) as VOLUMETRIE, FAISABILITE, CODE_RETOUR, MESSAGE_RETOUR
FROM
(
    SELECT * FROM a
    WHERE CODE_RETOUR = '490'
)
GROUP BY FAISABILITE, CODE_RETOUR, MESSAGE_RETOUR
ORDER BY 1 DESC
;

--F300C + F305
WITH a AS 
(
    SELECT DISTINCT dem.AFF_T_DISCO as AFFAIRE, dem.DEM_ID_PRM as POINT, nat.NAT_C_PRESTATION as PRESTATION, nat.NAT_C_SOUS_TYPE as PRS_OPTION, frn.FRN_T_ACTEUR as FOURNISSEUR, dem.DEM_R_STATUT as STATUT, ee.EST_T_ETAT as ETAT_EXTERNE, ei.EST_T_ETAT as ETAT_INTERNE, dem.DEM_D_DEMANDE as DATE_DEMANDE, dem.DEM_D_EFFET as DATE_EFFET, DECODE(dem.DEM_K_MODALITE_RDV, '1', 'DIS', '2', 'FRN') as MOD_RDV, dem.DEM_R_MEDIA_RECEPTION as MEDIA, mai.MAI_T_REGION as REGION, mai.MAI_T_TERRITOIRE as TERRITOIRE, dem.DEM_B_IS_SGEL as SGEL, dem.DEM_B_IS_GINKO as GINKO
    FROM SUIVI.DEMANDE dem
    JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
    LEFT JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
    JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
    JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
    LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
    WHERE 1=1
    AND nat.NAT_C_PRESTATION IN ('F300C', 'F305')
    AND dem.DEM_R_STATUT IN ('AFF-TERMINEE')
    AND ee.EST_T_ETAT LIKE '%Close, prestation réalisée%'
    AND dem.DEM_D_DEMANDE >= TO_DATE('29/07/2019', 'DD/MM/YYYY')
    AND mai.MAI_T_REGION IN ('M8 - Méditerranée')
)

SELECT DISTINCT a.POINT--, a.PRESTATION as PRS1, a.AFFAIRE as AFF1, b.PRESTATION as PRS2, b.AFFAIRE as AFF2
FROM a
JOIN a b ON a.POINT = b.POINT
WHERE 1=1
AND a.PRESTATION = 'F300C'
AND b.PRESTATION = 'F305'
;

--10 plus vieux srv ADAM par type
SELECT RANK, srv.SERVICE_ID, seg.PRM_ID, srv.SERVICE_TYPE as TYPE_SERVICE
, srv.ETAT_CODE, srv.DATE_DEBUT, srv.DATE_FIN, srv.MOTIF_FIN_LIBELLE, srv.DATE_CREATION, srv.ABONNEMENT_ID
, srv.PERIODICITE_TRANSMISSION, mes.TYPE_CODE as TYPE_MESURE, mes.PAS as PAS_MESURE
, CASE  WHEN ben.TYPE = 'PERSONNE' THEN 'Client'
        WHEN ben.TYPE = 'FINALITE' THEN 'Interne'
        WHEN ben.TYPE = 'CONTRAT' AND (ben.code LIKE 'GRD-F%' or ben.code = 'PROTOC-501') THEN 'Fournisseur'
        WHEN ben.TYPE = 'CONTRAT' AND NOT (ben.code LIKE 'GRD-F%' or ben.code = 'PROTOC-501') THEN 'Tiers'
        ELSE 'Indéterminé'
        END "TYPE_DEMANDEUR"
, CASE  WHEN ben.TYPE = 'FINALITE' THEN ben.CODE
        WHEN ben.TYPE = 'CONTRAT' THEN ben.LIBELLE
        END "DEMANDEUR"
FROM
(
    SELECT DENSE_RANK() OVER (PARTITION BY srv.SERVICE_TYPE ORDER BY srv.DATE_DEBUT, srv.SERVICE_ID) as RANK, srv.*
    FROM ADA_SCH.SERVICE_SOUSCRIT srv
) srv
LEFT JOIN ADA_SCH.BENEFICIAIRE ben ON srv.BENEFICIAIRE_ID = ben.ID
LEFT JOIN ADA_SCH.PRM_SEGMENT seg ON srv.PRM_SEGMENT_ID = seg.ID
LEFT JOIN ADA_SCH.MESURE mes ON srv.MESURE_ID = mes.ID
WHERE RANK < 11
ORDER BY TYPE_SERVICE, RANK
;