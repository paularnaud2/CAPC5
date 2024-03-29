SELECT POINT, ETAT_ADAM, DEBUT_ADAM, FIN_ADAM, MODIFICATION_ADAM, PAS_ADAM FROM
(
	SELECT PRM_ID as POINT, srv.ETAT_CODE ETAT_ADAM, srv.DATE_DEBUT DEBUT_ADAM
	, srv.DATE_FIN FIN_ADAM, srv.DATE_MODIFICATION MODIFICATION_ADAM, mes.PAS PAS_ADAM
	, DENSE_RANK() OVER (PARTITION BY seg.PRM_ID ORDER BY srv.DATE_DEBUT DESC, srv.DATE_MODIFICATION DESC, srv.ETAT_CODE, mes.PAS) as RANG
	FROM ADA_SCH.SERVICE_SOUSCRIT srv
	LEFT JOIN ADA_SCH.PRM_SEGMENT seg ON srv.PRM_SEGMENT_ID = seg.ID
	LEFT JOIN ADA_SCH.MESURE mes ON srv.MESURE_ID = mes.ID
	WHERE 1=1
	AND mes.TYPE_CODE = 'CDC'
	AND seg.PRM_ID IN @@IN@@
)
WHERE RANG  = 1