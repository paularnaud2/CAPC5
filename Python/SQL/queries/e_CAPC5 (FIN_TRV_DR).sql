SELECT sge.*
, rlv_g.DATE_DER_RLV DATE_DER_RLV_GINKO, rlv_g.STATU_DER_RLV STATU_DER_RLV_GINKO, rlv_g.FACT_DER_RLV FACT_DER_RLV_GINKO
, rlv_d.DIDACR001 DATE_DER_RLV_DISCO
, CASE WHEN rlv_g.DATE_DER_RLV <= TO_DATE('01/10/2019', 'DD/MM/YYYY') OR rlv_d.DIDACR001 <= '2019270' THEN 'KO' ELSE 'OK' END RLV_REELLE
FROM TGINKOSGE_DR_SI_7 sge
LEFT JOIN T_RLV_GINKO_20200911 rlv_g ON sge.PRM = rlv_g.PRM
LEFT JOIN T_RLV_DISCO_20200911 rlv_d ON sge.PRM = rlv_d.IDPDLL
WHERE 1=1
AND SI IN ('DISCO', 'GINKO')
AND EN_SERVICE ='O'
AND TYPE_OFFRE ='OH'
AND DR = '@@DR@@'