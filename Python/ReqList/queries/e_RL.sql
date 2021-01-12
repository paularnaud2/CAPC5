SELECT * FROM
(
SELECT DISTINCT
dem.AFF_T_DISCO as AFFAIRE,
dem.DEM_ID_PRM as POINT,
nat.NAT_C_PRESTATION as PRESTATION,
dem.DEM_R_STATUT as STATUT,
ee.EST_T_ETAT as ETAT_EXTERNE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'R_SOUS_TYPE_DEMANDE'
) THEN info.VAR_T_DATA END) as R_SOUS_TYPE_DEMANDE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_COMMENTAIRE_DEMANDE'
) THEN info.VAR_T_DATA END) as T_COMMENTAIRE_DEMANDE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_DETAIL_DEMANDE'
) THEN info.VAR_T_DATA END) as T_DETAIL_DEMANDE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_PDM_ADR_NUM'
) THEN info.VAR_T_DATA END) as T_PDM_ADR_NUM,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_PDM_ADR_VOIE'
) THEN info.VAR_T_DATA END) as T_PDM_ADR_VOIE,
MAX(CASE WHEN info.VAR_ID = (
SELECT VAR_ID FROM AFFAIRE.VARIABLE
WHERE VAR_C_CODE = 'T_REPONSE_DEFINITIVE'
) THEN info.VAR_T_DATA END) as T_REPONSE_DEFINITIVE
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
AND nat.NAT_C_PRESTATION IN ('M002')
AND info.VAR_ID IN (SELECT VAR_ID FROM AFFAIRE.VARIABLE WHERE VAR_C_CODE IN ('R_SOUS_TYPE_DEMANDE', 'T_COMMENTAIRE_DEMANDE', 'T_DETAIL_DEMANDE', 'T_PDM_ADR_NUM', 'T_PDM_ADR_VOIE', 'T_REPONSE_DEFINITIVE'))
GROUP BY dem.AFF_T_DISCO, dem.DEM_ID_PRM, nat.NAT_C_PRESTATION, dem.DEM_R_STATUT, ee.EST_T_ETAT
)
WHERE 1=1
AND AFFAIRE IN @@IN1@@
;