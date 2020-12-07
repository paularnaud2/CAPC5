select max(length(GRP)), max(length(CIV)), max(length(NOM)), max(length(PRENOM)), max(length(LOGIN))
FROM
(
	select dem.DEM_T_INITIATEUR LOGIN, dem.DEM_T_REGROUPEMENT GRP, uti.UTI_R_CIVILITE CIV, uti.UTI_T_NOM NOM, uti.UTI_T_PRENOM PRENOM
	from suivi.demande dem
	LEFT JOIN UTILISATEUR.UTILISATEUR uti ON dem.DEM_K_UTI_INITIATEUR = uti.UTI_ID
	WHERE rownum < 1000000
)