BEGIN
	BEGIN
		EXECUTE IMMEDIATE 'DROP TABLE @@TABLE_NAME@@';
		EXCEPTION
			WHEN OTHERS THEN
				IF sqlcode != -0942 THEN RAISE; END IF;
	END;
	EXECUTE IMMEDIATE 'CREATE TABLE @@TABLE_NAME@@ (
		"PRM" VARCHAR2(14 BYTE), 
		"AFFAIRE" VARCHAR2(8 BYTE), 
		"SI" VARCHAR2(5 BYTE), 
		"PRESTATION" VARCHAR2(5 BYTE), 
		"STATUT" VARCHAR2(12 BYTE), 
		"ETAT_EXTERNE" VARCHAR2(64 CHAR), 
		"FOURNISSEUR" VARCHAR2(50 BYTE), 
		"TYPE_OFFRE" VARCHAR2(2 BYTE), 
		"DATE_DEMANDE" VARCHAR2(20 BYTE),
		"MODEREA" VARCHAR2(4 CHAR)
	) SEGMENT CREATION IMMEDIATE 
	PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
	NOCOMPRESS LOGGING
	STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
	PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
	BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)';
	COMMIT;
END;