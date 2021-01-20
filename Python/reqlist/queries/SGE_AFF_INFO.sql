SELECT DISTINCT dem.DEM_ID_PRM as POINT
--, dem.AFF_T_DISCO as AFFAIRE
--, nat.NAT_C_PRESTATION as PRESTATION, nat.NAT_C_SOUS_TYPE as PRS_OPTION
--, DECODE(dem.DEM_K_CATEGORIE, '1', 'PRO', '2', 'PART') as CAT_CLIENT, frn.FRN_T_ACTEUR as FOURNISSEUR
--, dem.DEM_R_STATUT as STATUT
, ee.EST_T_ETAT as ETAT_AFF_SGE
--, ei.EST_T_ETAT as ETAT_INTERNE
, dem.DEM_D_DEMANDE as DATE_DEMANDE, dem.DEM_D_EFFET as DATE_EFFET
--, DECODE(dem.DEM_K_MODALITE_RDV, '1', 'DIS', '2', 'FRN') as MOD_RDV
--, dem.DEM_R_MEDIA_RECEPTION as MEDIA, mai.MAI_T_REGION as REGION, mai.MAI_T_TERRITOIRE as TERRITOIRE
--, dem.DEM_B_IS_SGEL as SGEL, dem.DEM_B_IS_GINKO as GINKO
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
LEFT JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
LEFT JOIN SUIVI.MAILLE mai ON mai.MAI_ID = dem.DEM_K_MAI
WHERE 1=1
AND dem.AFF_T_DISCO IN @@IN@@