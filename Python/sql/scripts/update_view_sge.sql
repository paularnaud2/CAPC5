  CREATE OR REPLACE FORCE VIEW "CAPC5"."@@VIEW_NAME@@" ("PRM", "DR", "REG", "SEG"
  , "CODE_INSEE", "CODE_POSTAL", "CODE_DEPARTEMENT", "CCD", "COMMUNE", "SI", "ETAT_CONTRACTUEL", "EN_SERVICE"
  , "CONTRAT", "TYPE_OFFRE", "CAT_CIENT"
  , "CF_CIV", "CF_NOM", "CF_PRENOM", "CF_RSOCIALE"
  , "CF_AD_1", "CF_AD_2", "CF_AD_3", "CF_AD_4", "CF_AD_5", "CF_AD_6", "IC_NOM"
  , "DATE_DER_MES", "DATE_DER_CHGT_FRN", "DATE_DER_MODIF_FTA", "DATE_PREM_POS_LINKY"
  , "CALENDRIER", "CAL_LIBELLE", "FTA", "NB_CADRANS", "CAL_CODE_COPIE"
  , "PS", "P_RAC", "COMPTEUR", "NB_FILS", "NIV_OUV_SERV", "CPT_COMMUNICANT", "CPT_TELEOPERABLE", "CPT_ACCESSIBLE"
  , "MODE_RLV", "MEDIA", "INT_REGLAGE_DJ", "CALIBRE_DJ", "PARTICULARITE", "COLOC", "BP"
  , "F130_EC", "DATE_EFFET") AS 
  SELECT sge.PRM
, geo.DR, geo.REG
, "SEG"
, sge.CODE_INSEE, sge.CODE_POSTAL, sge.CODE_DEPARTEMENT
,"CCD","COMMUNE","SI","ETAT_CONTRACTUEL","EN_SERVICE","CONTRAT","TYPE_OFFRE"
,"CAT_CIENT","CF_CIV","CF_NOM","CF_PRENOM","CF_RSOCIALE"
, "CF_AD_1", "CF_AD_2", "CF_AD_3", "CF_AD_4", "CF_AD_5", "CF_AD_6"
, "IC_NOM"
,"DATE_DER_MES","DATE_DER_CHGT_FRN","DATE_DER_MODIF_FTA"
,"DATE_PREM_POS_LINKY","CALENDRIER","CAL_LIBELLE","FTA","NB_CADRANS","CAL_CODE_COPIE"
, "PS", "P_RAC"
,"COMPTEUR", "NB_FILS"
,"NIV_OUV_SERV","CPT_COMMUNICANT","CPT_TELEOPERABLE","CPT_ACCESSIBLE"
,"MODE_RLV","MEDIA"
,"INT_REGLAGE_DJ","CALIBRE_DJ"
,"PARTICULARITE","COLOC","BP","F130_EC","DATE_EFFET"
FROM @@TABLE_NAME@@ sge
LEFT JOIN TGEO geo ON sge.CODE_INSEE = geo.CODE_INSEE