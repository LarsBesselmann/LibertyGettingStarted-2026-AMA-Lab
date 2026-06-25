# [6/24/26 11:23:43:078 EDT] Enterprise Applications > Enterprise Applications
AdminApp.install('simple-pharmacy.war', '[  -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -appname simple-pharmacy_war -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -contextroot /simplePharmacy  -MapModulesToServers [[ "Simple Pharmacy Dashboard" simple-pharmacy.war,WEB-INF/web.xml WebSphere:cell=Default01Cell,node=AppSrv01Node1,server=server1 ]] -MapWebModToVH [[ "Simple Pharmacy Dashboard" simple-pharmacy.war,WEB-INF/web.xml default_host ]] -CtxRootForWebMod [[ "Simple Pharmacy Dashboard" simple-pharmacy.war,WEB-INF/web.xml /simplePharmacy ]]]' )

# [6/24/26 11:23:56:855 EDT] Enterprise Applications > Enterprise Applications
AdminConfig.save()

# [6/24/26 11:24:17:058 EDT] Nodes
AdminControl.invoke('WebSphere:name=cellSync,process=dmgr,platform=common,node=Dmgr01Node,version=9.0.5.25,type=CellSync,mbeanIdentifier=cellSync,cell=Default01Cell,spec=1.0', 'syncNode', '[AppSrv01Node1]')
