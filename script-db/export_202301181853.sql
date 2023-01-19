INSERT INTO public.auth_group (name) VALUES
	 ('Administradores'),
	 ('Operadores');
INSERT INTO public.security_module (created_at,created_by,updated_at,update_by,deleted,deleted_at,deleted_by,code,url,name,category_module,type_module,icon,image,description,"order",visible) VALUES
	 ('2023-01-09 19:07:06.041423-05','admin','2023-01-09 23:23:06.268986-05','admin',false,NULL,NULL,'001','/','Rec. de objetos (IA)','Maintenance','Menu','mdi mdi-face-recognition','',NULL,1,true),
	 ('2023-01-09 19:08:55.910381-05','admin','2023-01-09 23:25:28.871108-05','admin',false,NULL,NULL,'003','/','Gestionar API','Maintenance','Menu','mdi mdi-api','',NULL,3,true),
	 ('2023-01-09 19:09:47.796673-05','admin','2023-01-15 23:13:59.347686-05','admin',false,NULL,NULL,'004','/dashboard','Panel Dashboard','Resports','Menu','dripicons-graph-pie','',NULL,4,true),
	 ('2023-01-09 19:08:07.139532-05','admin','2023-01-15 23:33:41.350617-05','admin',false,NULL,NULL,'002','/security/auth-qr','Autentificación  QR','Maintenance','Menu','mdi mdi-qrcode-scan','',NULL,2,true),
	 ('2023-01-15 23:08:40.866385-05','admin','2023-01-15 23:37:40.0367-05','admin',false,NULL,NULL,'005','/customers','Crud web','Maintenance','Menu','dripicons-checklist','',NULL,8,true);
INSERT INTO public.security_modulegrupcategory (created_at,created_by,updated_at,update_by,deleted,deleted_at,deleted_by,code,name,"order") VALUES
	 ('2023-01-09 19:14:26.035635-05','admin','2023-01-09 19:14:33.50361-05','admin',false,NULL,NULL,NULL,'DESARROLLO WEB',3),
	 ('2023-01-09 19:13:40.792662-05','admin','2023-01-09 19:13:40.792678-05',NULL,false,NULL,NULL,NULL,'INTELIGENCIA ARTIFICIAL',1),
	 ('2023-01-09 19:13:06.130281-05','admin','2023-01-09 19:13:46.353446-05','admin',false,NULL,NULL,NULL,'DASHBOARD',2);
INSERT INTO public.security_modulegruppermissions (created_at,created_by,updated_at,update_by,deleted,deleted_at,deleted_by,description,priority,group_id,main_category_id,module_id) VALUES
	 ('2023-01-09 19:20:34.922728-05','admin','2023-01-09 19:20:34.922783-05',NULL,false,NULL,NULL,'Gestión API',4,1,3,3),
	 ('2023-01-09 19:19:59.213452-05','admin','2023-01-10 00:23:07.069832-05','admin',false,NULL,NULL,'Panel Dashboard',1,1,1,4),
	 ('2023-01-09 19:18:38.562434-05','admin','2023-01-10 00:23:12.99633-05','admin',false,NULL,NULL,'Code QR',2,1,2,2),
	 ('2023-01-09 19:17:09.180732-05','admin','2023-01-10 00:23:19.833406-05','admin',false,NULL,NULL,'Modulo Objetos IA',3,1,2,1),
	 ('2023-01-15 23:09:11.645151-05','admin','2023-01-15 23:09:11.645168-05',NULL,false,NULL,NULL,NULL,2,1,3,5);
