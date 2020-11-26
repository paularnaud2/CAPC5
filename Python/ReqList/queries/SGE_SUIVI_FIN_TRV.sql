WITH aff_130 as (
	SELECT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE, dem.DEM_D_EFFET as DATE_EFFET
	, DENSE_RANK() OVER (PARTITION BY dem.DEM_ID_PRM ORDER BY dem.DEM_D_DEMANDE DESC) as RANG
	FROM SUIVI.DEMANDE dem
	JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
	WHERE 1=1
	AND nat.NAT_C_PRESTATION IN ('F130B')
	AND dem.DEM_R_STATUT IN ('AFF-ENCOURS')
)

SELECT PRM, SEG, CODE_INSEE, CODE_POSTAL, CODE_DEPARTEMENT, CCD, COMMUNE
, SI, ETAT_CONTRACTUEL, EN_SERVICE, CONTRAT
, CASE WHEN TYPE_OFFRE_SCN IS NULL THEN TYPE_OFFRE_CTR ELSE TYPE_OFFRE_SCN END TYPE_OFFRE
, CAT_CIENT
, CF_CIV, CF_NOM, CF_PRENOM, CF_RSOCIALE, CF_AD_1, CF_AD_2, CF_AD_3, CF_AD_4, CF_AD_5, CF_AD_6
, IC_NOM
, DATE_DER_MES, DATE_DER_CHGT_FRN, DATE_DER_MODIF_FTA, DATE_PREM_POS_LINKY
, CALENDRIER, CAL_LIBELLE, FTA
, NB_CADRANS, CAL_CODE_COPIE
, PS, P_RAC
, COMPTEUR, NB_FILS, NIV_OUV_SERV, CPT_COMMUNICANT, CPT_TELEOPERABLE, CPT_ACCESSIBLE, MODE_RLV, MEDIA
, INT_REGLAGE_DJ, CALIBRE_DJ, PARTICULARITE
, COLOC, BP
, F130_EC, DATE_EFFET
FROM
(
	SELECT DISTINCT prm.PRM_ID as PRM
	, prm.PRM_SC_SEGMENT SEG
	, DECODE(situ.SCN_APP_APPLICATION_CODE, 'QETGC', 'DISCO', situ.SCN_APP_APPLICATION_CODE) as SI
	, prm.PRM_SC_ETAT_CONTRACTUEL_CODE ETAT_CONTRACTUEL
	, CASE WHEN prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC' THEN 'O' ELSE 'N' END EN_SERVICE
	, CASE WHEN situ.SCN_ST_TYPE_OFFRE_CODE = 'OH' AND situ.SCN_APP_APPLICATION_CODE = 'QETGC' THEN 'PROTOC-501' ELSE prm.PRM_DG_NUMERO_CONTRAT END CONTRAT
	, PRM_SC_DATE_DER_MES DATE_DER_MES
	, PRM_SC_DATE_DER_CHGT_FOURN DATE_DER_CHGT_FRN
	, PRM_SC_DATE_DER_MODIF_STR_TAR DATE_DER_MODIF_FTA
	, prm.PRM_DG_DATE_PREM_POS_COMP_LINK DATE_PREM_POS_LINKY
	, situ.SCN_ST_TYPE_OFFRE_CODE TYPE_OFFRE_SCN
	, CASE WHEN prm.PRM_DG_NUMERO_CONTRAT = 'PROTOC-501' THEN 'OH' ELSE 'NO' END as TYPE_OFFRE_CTR
	, situ.SCN_CF_CATEGORIE_CODE as CAT_CIENT
	, situ.SCN_GF_CALENDRIER_FOURN_CODE as CALENDRIER
	, situ.SCN_ST_FORM_TARIF_ACHEMIN as FTA
	, REPLACE(situ.SCN_ST_P_SOUSCRITE_MAX_V,'.',',') PS
	, REPLACE(talim.ALI_PUISS_RACCO_SOUTI_V,'.',',') P_RAC
	, cal.CAL_LIBELLE_COMPTEUR CAL_LIBELLE
	, DECODE(scm.SCM_DC_STRUCTURE_COMPTAGE_CODE,'AMM', 'LINKY','', 'SSCPT',scm.SCM_DC_STRUCTURE_COMPTAGE_CODE) as COMPTEUR
	, scm.SCM_MODE_RELEVE_CODE MODE_RLV
	, scm.SCM_MEDIA_CODE MEDIA
	, prm.PRM_DG_NIV_OUV_SERV NIV_OUV_SERV
	, CASE WHEN prm.PRM_DG_NIV_OUV_SERV > 0 THEN 'O'
			WHEN scm.SCM_MODE_RELEVE_CODE = 'TRLV' THEN 'O'
			ELSE 'N' END CPT_COMMUNICANT
	, CASE WHEN situ.SCN_APP_APPLICATION_CODE IN ('QETGC', 'GINKO') THEN CASE WHEN scm.SCM_TELEOPERABLE = '1' THEN 'O' ELSE 'N' END
			ELSE NULL END CPT_TELEOPERABLE
	, REPLACE(eqeDJ.EQE_DJ_INT_REGLAGE_V,'.',',') INT_REGLAGE_DJ, eqeDJ.EQE_DJ_CALIBRE_CODE CALIBRE_DJ
	, DECODE(eqeCPT.EQE_ACCESSIBILITE, '0', 'N', '1', 'O', 'N') CPT_ACCESSIBLE
	, eqeCPT.EQE_MC_NB_CADRANS as NB_CADRANS
	, eqeCPT.EQE_CP_NB_FILS as NB_FILS
	, cal.CAL_CODE_COPIE CAL_CODE_COPIE
	, scm.SCM_DC_PARTICULARITE_CODE PARTICULARITE
	, prm.PRM_AI_CODE_INSEE CODE_INSEE
	, prm.PRM_AI_CODE_POSTAL CODE_POSTAL
	, CASE WHEN SUBSTR(prm.PRM_ID, 1, 3) LIKE '500%' OR SUBSTR(prm.PRM_ID, 1, 3) LIKE '300%'
		THEN prm.PRM_DG_CENTRE_CODE ELSE SUBSTR(prm.PRM_ID, 1, 3)
		END CCD
	, SUBSTR(prm.PRM_AI_CODE_INSEE, 1, 2) CODE_DEPARTEMENT
	, SUBSTR(prm.PRM_AIN_LIGNE6, 7) COMMUNE
	, CASE WHEN cf.PRS_MOR_ACTIVITE = 'COLOC' THEN 'O' ELSE 'N' END COLOC
	, CASE WHEN alim.SAL_RACCO_PROVISOIRE = '1' THEN 'O' ELSE 'N' END BP
	, aff_130.AFFAIRE F130_EC, aff_130.DATE_EFFET
	, cf.PRS_PHY_CIVILITE CF_CIV, cf.PRS_PHY_NOM CF_NOM, cf.PRS_PHY_PRENOM CF_PRENOM, cf.PRS_MOR_DENOMINATION_SOCIALE CF_RSOCIALE
	, cf.PRS_ADRESSE_LIGNE_UN CF_AD_1, cf.PRS_ADRESSE_LIGNE_DEUX CF_AD_2, cf.PRS_ADRESSE_LIGNE_TROIS CF_AD_3
	, cf.PRS_ADRESSE_LIGNE_QUATRE CF_AD_4, cf.PRS_ADRESSE_LIGNE_CINQ CF_AD_5, cf.PRS_ADRESSE_LIGNE_SIX CF_AD_6
	, ic.PRS_PHY_NOM IC_NOM
	FROM SGEL_PRM_SCH.T_PRM prm
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
	LEFT JOIN SGEL_PRM_SCH.T_PERSONNE cf ON situ.SCN_CLIENT_FINAL_ID = cf.PRS_ID
	LEFT JOIN SGEL_PRM_SCH.T_PERSONNE ic ON situ.SCN_INTERLOCUTEUR_CLIENT_ID = ic.PRS_ID
	LEFT JOIN SGEL_SCH.T_CALENDRIER cal ON situ.SCN_GF_CALENDRIER_FOURN_CODE = cal.CAL_CODE
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_COMPTAGE scm ON scm.SCM_ID = prm.SCM_ID
	LEFT JOIN SGEL_PRM_SCH.T_EQUIPEMENT eqeCPT ON eqeCPT.SCM_C_ID = prm.SCM_ID
	LEFT JOIN SGEL_PRM_SCH.T_EQUIPEMENT eqeDJ ON eqeDJ.EQE_ID = scm.EQE_DISJONCTEUR_ID
	LEFT JOIN SGEL_PRM_SCH.T_SITUATION_ALIMENTATION alim ON prm.SAL_ID = alim.SAL_ID
	LEFT JOIN SGEL_PRM_SCH.T_ALIMENTATION talim ON talim.ALI_ID = alim.ALI_PRINCIPALE_ID
	LEFT JOIN SGEL_PRM_SCH.T_PERSONNE cf ON situ.SCN_CLIENT_FINAL_ID = cf.PRS_ID
	LEFT JOIN SGEL_SCH.T_CALENDRIER cal ON situ.SCN_GF_CALENDRIER_FOURN_CODE = cal.CAL_CODE
	LEFT JOIN aff_130 ON (prm.PRM_ID = aff_130.POINT AND aff_130.RANG = 1)
	WHERE 1=1
	AND prm.PRM_ID IN @@IN1@@
	-- AND prm.PRM_ID IN ('01102170668103', '24262662797365', '09620984080770', '22177279218565', '25675976808201', '02444862487788', '30000731502759', '19524167854286', '01100144557179', '01100289273089', '30000110326267', '30000751220199', '30002130773580', '01181186604919')
	-- ORDER BY prm.PRM_ID
	-- AND prm.PRM_ID = '24262662797365'
	-- AND prm.PRM_TECH_DATE_MAJ >= TO_DATE('02/10/2020', 'DD/MM/YYYY')
)