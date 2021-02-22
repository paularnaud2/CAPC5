--SELECT app.site, pds.REFERENCE as POINT, 'COLLECTIF' as T...
SELECT app.site, pds.REFERENCE as POINT, 'COLLECTIF' as TYPE_POINT
FROM gahfld.TPOINTDESERVICE pds
cross join gahfld.tapplicationinfo app 
INNER JOIN gahfld.TESPACEDELIVRAISON edl ON (edl.ID = pds.EspaceDeLivraison_ID)
INNER JOIN gahfld.EQUIPEMENT_INSTALLATIONS coll_eqi ON (coll_eqi.Dest = pds.ID)
INNER JOIN gahfld.TEQUIPEMENT coll_eq ON(coll_eqi.Source = coll_eq.ID AND MOD(coll_eq.EtatObjet, 2 ) = 0)
INNER JOIN gahfld.TBRANCHEMENT coll_bcht ON (coll_bcht.ID= coll_eq.Branchement_ID AND coll_bcht.Role = coll_eq.Branchement_Role AND MOD(coll_bcht.EtatObjet, 2)=0)
INNER JOIN gahfld.TBRANCHEMENTELEC coll_bcei ON (coll_bcei.ID = coll_bcht.ID)
where pds.REFERENCE LIKE '500%'
--and PDS.nature = 1 --point consommation

union all

-- points individuels
select app.site,pds.REFERENCE as POINT, 'INDIVIDUEL' as TYPE_POINT
FROM gahfld.TPOINTDESERVICE pds
cross join gahfld.tapplicationinfo app
INNER JOIN gahfld.TESPACEDELIVRAISON edl ON (edl.ID = pds.EspaceDeLivraison_ID)
INNER JOIN gahfld.TBRANCHEMENT ind_bcht ON (ind_bcht.EspaceDeLivraison_ID = edl.ID AND MOD(ind_bcht.EtatObjet, 2)=0)
INNER JOIN gahfld.TBRANCHEMENTELEC ind_bcei on (ind_bcei.ID = ind_bcht.ID)
where pds.REFERENCE LIKE '500%'
--and PDS.nature = 1 --point consommation

union all

--points collectifs ne commençant pas par 500 rattachés sur le EDL
SELECT app.site,pds.REFERENCE as POINT, 
CASE WHEN coll_bcei.typebranchement = 'INCONNU' then 'COLLECTIF' else 'INDIVIDUEL' END as TYPE_POINT
FROM gahfld.TPOINTDESERVICE pds 
cross join gahfld.tapplicationinfo app
INNER JOIN gahfld.TESPACEDELIVRAISON edl ON (edl.ID = pds.EspaceDeLivraison_ID)
INNER JOIN gahfld.EQUIPEMENT_INSTALLATIONS coll_eqi ON (coll_eqi.Dest = pds.ID)
INNER JOIN gahfld.TEQUIPEMENT coll_eq ON(coll_eqi.Source = coll_eq.ID AND MOD(coll_eq.EtatObjet, 2 ) = 0)
INNER JOIN gahfld.TBRANCHEMENT coll_bcht ON (coll_bcht.ID= coll_eq.Branchement_ID AND coll_bcht.Role = coll_eq.Branchement_Role AND MOD(coll_bcht.EtatObjet, 2)=0)
INNER JOIN gahfld.TBRANCHEMENTELEC coll_bcei ON (coll_bcei.ID = coll_bcht.ID)
WHERE coll_eq.ROLE = 'com.hermes.ref.edl.businessobject.ColonneCollective'
and pds.reference <> '500%'
--and pds.nature = 1

union all

--points collectifs ne commençant pas par 500 et ne sont pas rattachés sur le EDL
select app.site,pds.REFERENCE as POINT, 
CASE WHEN ind_bcei.typebranchement = 'INCONNU' then 'COLLECTIF' else 'INDIVIDUEL' END as TYPE_POINT
FROM gahfld.TPOINTDESERVICE pds
cross join gahfld.tapplicationinfo app
INNER JOIN gahfld.TESPACEDELIVRAISON edl ON (edl.ID = pds.EspaceDeLivraison_ID)
INNER JOIN gahfld.TBRANCHEMENT ind_bcht ON (ind_bcht.EspaceDeLivraison_ID = edl.ID AND MOD(ind_bcht.EtatObjet, 2)=0)
INNER JOIN gahfld.TBRANCHEMENTELEC ind_bcei on (ind_bcei.ID = ind_bcht.ID)
and pds.reference <> '500%'
--and pds.nature = 1 
;