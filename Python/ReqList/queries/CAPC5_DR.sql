SELECT prm.PRM, geo.DR
FROM PRM_LITE_20201202 prm
JOIN TGEO geo ON prm.CODE_INSEE = geo.CODE_INSEE
WHERE 1=1
-- AND PRM = '00000000000000'
AND PRM IN @@IN1@@