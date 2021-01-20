SELECT pds.REFERENCE POINT
FROM GAHFLD.TPOINTDESERVICE pds
JOIN gahfld.TPOINTACCESSERVICESCLIENT pasc ON pasc.POINTDESERVICE_ID = pds.ID
WHERE 1=1
AND pasc.STATUT = 0
AND pasc.REFUSENREGISTREMENTCDC = '1'