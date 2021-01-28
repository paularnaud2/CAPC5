--Supervision Ginko
with my_transfert as 
   (select ech.ID_ECHANGE, ech.XDT_ECHANGE, ech.XCODE_FLUX, 
		ech.XSTATUT, ID_TRANSFERT, SENS, INSTANCE, ID_PRM, 
		CODE_APPEL, tra.STATUT, tra.UNIQUE_ID_TRANSFERT, tra.DT_TRANSFERT,
			1 as "value_numeric", con.CONTENU
	from ginko_supervision.T_TRANSFERT tra, 
		ginko_supervision.T_ECHANGE ech, 
		ginko_supervision.T_CONTENU con
	where ech.ID_ECHANGE = tra.ID_ECHANGE
	and tra.UNIQUE_ID_TRANSFERT = con.UNIQUE_ID_TRANSFERT (+)
	and tra.xdt_echange >= '10/09/18'
	and tra.xdt_echange < '11/09/18')
select nvl(e.ID_ECHANGE, s.ID_ECHANGE) ID_ECHANGE,
	   nvl(e.XDT_ECHANGE, s.XDT_ECHANGE) XDT_ECHANGE, 
	   nvl(e.XCODE_FLUX, s.XCODE_FLUX) XCODE_FLUX,
	   nvl(e.XSTATUT, s.XSTATUT) XSTATUT,
	   nvl(e.INSTANCE, s.INSTANCE) INSTANCE,
	   nvl(e.ID_PRM, s.ID_PRM) ID_PRM,
	   e.CODE_APPEL CODE_APPEL_E, 
	   s.CODE_APPEL CODE_APPEL_S,
	   e.STATUT STATUT_E,
	   e.STATUT STATUT_s,
	   e.CONTENU CONTENU_E,
	   s.CONTENU CONTENU_S
	from (select * from my_transfert where sens = 'E') e
	full outer join
		(select * from my_transfert where sens = 'S') s
	ON (e.id_echange = s.id_echange)
  ;

--Supervision ILE
SELECT *
FROM ILE_SUPERVISION.T_TRANSFERT tr
JOIN ILE_SUPERVISION.T_OBJET_METIER ob ON tr.ID_ECHANGE = ob.ID_ECHANGE
--JOIN ILE_SUPERVISION.T_CONTENU ct ON tr.UNIQUE_ID_TRANSFERT = ct.UNIQUE_ID_TRANSFERT
--JOIN ILE_SUPERVISION.T_CONTENU_META_DONNEE ctm ON ct.ID_CONTENU = ctm.ID_CONTENU
WHERE 1=1
AND tra.xdt_echange >= '10/09/18'
AND tra.xdt_echange < '11/09/18')
--AND tr.DT_DERN_MODIF_UTC < '27/02/2019'
AND tr.CODE_MOUVEMENT = 'C15-FOURN-S'
AND tr.SENS = 'E'
AND ob.ID_OBJET = 'nomFichier'
--AND ob.VALEUR_OBJET = 'Enedis_C15_FR_17X100A100F0019Z_GRD-C501_0324_01417_20190224055614.zip'
ORDER BY tr.XDT_ECHANGE
;

--Partitions
SELECT * FROM DBA_PART_KEY_COLUMNS; --pas les droits, résultat :

ILE_SUPERVISION T_CONTENU       TABLE   UNIQUE_ID_TRANSFERT     1 
ILE_SUPERVISION T_CONTENU_META_DONNEE   TABLE   ID_CONTENU      1 
ILE_SUPERVISION T_OBJET_ERREUR  TABLE   XDT_ECHANGE     1 
ILE_SUPERVISION T_OBJET_METIER  TABLE   XDT_ECHANGE     1 
ILE_SUPERVISION T_TRANSFERT     TABLE   XDT_ECHANGE     1 
