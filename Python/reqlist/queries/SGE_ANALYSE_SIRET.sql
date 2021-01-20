SELECT DISTINCT dem.DEM_ID_PRM as POINT, dem.AFF_T_DISCO as AFFAIRE, dem.DEM_R_MEDIA_RECEPTION as CANAL
, nat.NAT_C_PRESTATION as PRESTATION
, frn.FRN_T_ACTEUR as FOURNISSEUR
, dem.DEM_R_STATUT as STATUT
, ee.EST_T_ETAT as ETAT_EXTERNE, ei.EST_T_ETAT as ETAT_INTERNE
, dem.DEM_D_DEMANDE as DATE_DEMANDE, dem.DEM_D_EFFET as DATE_EFFET
, dem.DEM_T_SIRET as SIRET
FROM SUIVI.DEMANDE dem
JOIN SUIVI.NATURE nat ON dem.DEM_K_NAT = nat.NAT_ID
LEFT JOIN SUIVI.ETAT_STATUT ee ON dem.DEM_K_EST_EXT = ee.EST_ID
JOIN SUIVI.ETAT_STATUT ei ON dem.DEM_K_EST_INT = ei.EST_ID
JOIN SUIVI.FOURNISSEUR frn ON frn.FRN_ID = dem.DEM_K_FRN
WHERE 1=1
AND dem.DEM_ID_PRM IN @@IN@@
AND dem.DEM_T_SIRET = '00000000000018'
ORDER BY dem.DEM_D_DEMANDE DESC