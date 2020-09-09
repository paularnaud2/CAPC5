SELECT 
prm.PRM_ID as PDL
, prm.PRM_SC_SEGMENT as SEGMENT
, situ.SCN_CF_CATEGORIE_CODE as CAT
, prm.PRM_AIN_LIGNE2 PRM_LIGNE2, prm.PRM_AIN_LIGNE3 PRM_LIGNE3, prm.PRM_AIN_LIGNE4 PRM_LIGNE4, prm.PRM_AIN_LIGNE5 PRM_LIGNE5, prm.PRM_AIN_LIGNE6 PRM_LIGNE6

, ic.PRS_PHY_CIVILITE IC_CIVILITE
, ic.PRS_PHY_NOM IC_NOM
, ic.PRS_PHY_PRENOM IC_PRENOM
, ic.PRS_COORD_EMAIL IC_EMAIL
, ic.PRS_COORD_TELEPHONE_FIXE IC_TELEPHONE_FIXE
, ic.PRS_COORD_TELEPHONE_PORT IC_TELEPHONE_PORT
, ic.PRS_ADRESSE_LIGNE_DEUX IC_LIGNE2, ic.PRS_ADRESSE_LIGNE_TROIS IC_LIGNE3, ic.PRS_ADRESSE_LIGNE_QUATRE IC_LIGNE4, ic.PRS_ADRESSE_LIGNE_CINQ IC_LIGNE5, ic.PRS_ADRESSE_LIGNE_SIX IC_LIGNE6

, cf.PRS_PHY_CIVILITE CF_CIVILITE
, cf.PRS_PHY_NOM CF_NOM
, cf.PRS_PHY_PRENOM CF_PRENOM
, cf.PRS_COORD_TELEPHONE_FIXE CF_TELEPHONE_FIXE
, cf.PRS_COORD_TELEPHONE_PORT CF_TELEPHONE_PORT
, cf.PRS_MOR_ACTIVITE CF_ACTIVITE
, cf.PRS_MOR_DENOMINATION_SOCIALE CF_RAISON_SOCIALE
, cf.PRS_MOR_NOM_COMMERCIAL CF_NOM_COMMERCIAL
, cf.PRS_MOR_NUMERO_SIRET CF_SIRET
, cf.PRS_ADRESSE_LIGNE_DEUX CF_LIGNE2, cf.PRS_ADRESSE_LIGNE_TROIS CF_LIGNE3, cf.PRS_ADRESSE_LIGNE_QUATRE CF_LIGNE4, cf.PRS_ADRESSE_LIGNE_CINQ CF_LIGNE5, cf.PRS_ADRESSE_LIGNE_SIX CF_LIGNE6

FROM SGEL_PRM_SCH.T_PRM prm
JOIN SGEL_PRM_SCH.T_SITUATION_CONTRACTUELLE situ ON prm.SCN_ID = situ.SCN_ID
LEFT JOIN SGEL_PRM_SCH.T_PERSONNE cf ON situ.SCN_CLIENT_FINAL_ID = cf.PRS_ID
LEFT JOIN SGEL_PRM_SCH.T_PERSONNE ic ON situ.SCN_INTERLOCUTEUR_CLIENT_ID = ic.PRS_ID
WHERE 1=1
AND prm.PRM_SC_ETAT_CONTRACTUEL_CODE = 'SERVC'
AND prm.PRM_SC_SEGMENT IN ('C5', 'P4')
AND situ.SCN_CF_CATEGORIE_CODE = 'PRO'
AND prm.PRM_ID LIKE '@@PRM_RANGE_2@@%'
AND ROWNUM <= 1000