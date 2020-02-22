def fcounter(C, *args, **kwargs):
	newc = C(*args, **kwargs)

	cm =  [f for f in dir(C) if callable(getattr(C,f)) and not f.startswith('_')]
	cf =  [f for f in dir(C) if not callable(getattr(C,f))  and not f.startswith('_')]
	om =  [f for f in vars(newc) if callable(getattr(newc,f)) and f not in set(cm) and not f.startswith('_')]
	of =  [f for f in vars(newc) if not callable(getattr(newc,f)) and f not in set(cf) and not f.startswith('_')]  
	
	cm.sort(), cf.sort(), om.sort(), of.sort()

	return cm, cf, om, of


