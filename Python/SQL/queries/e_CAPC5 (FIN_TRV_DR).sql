SELECT sge.PRM, sge.CODE_INSEE, sge.CODE_DEPARTEMENT, sge.CCD, sge.COMMUNE, sge.DR, sge.REG
, sge.SI, sge.EN_SERVICE, sge.TYPE_OFFRE, sge.CALENDRIER, sge.CAL_LIBELLE CAL_LIBELLE_COMPTEUR
, sge.PS PS_MAX_KW, sge.P_RAC P_RAC_KW, sge.COMPTEUR, sge.CPT_COMMUNICANT, sge.CPT_ACCESSIBLE
, sge.MODE_RLV, sge.MEDIA, sge.F130_EC, sge.DATE_EFFET, sge.BP, sge.COLOC
, rlv_g.DATE_DER_RLV DATE_DER_RLV_GINKO, rlv_g.STATU_DER_RLV STATU_DER_RLV_GINKO, rlv_g.FACT_DER_RLV FACT_DER_RLV_GINKO
, rlv_d.DIDACR001 DATE_DER_RLV_DISCO
, CASE WHEN rlv_g.DATE_DER_RLV <= TO_DATE('01/10/2019', 'DD/MM/YYYY') OR rlv_d.DIDACR001 <= '2019270' THEN 'KO' ELSE 'OK' END RLV_REELLE
FROM SGE sge
LEFT JOIN RLV_GINKO rlv_g ON sge.PRM = rlv_g.PRM
LEFT JOIN RLV_DISCO rlv_d ON sge.PRM = rlv_d.IDPDLL
WHERE 1=1
AND SI IN ('DISCO', 'GINKO')
AND EN_SERVICE ='O'
AND TYPE_OFFRE ='OH'
AND DR = '@@DR@@'