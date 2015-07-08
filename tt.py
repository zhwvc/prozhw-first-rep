import itertools
for key,value in itertools.groupby("AaBB",lambda x: x.upper()):
	print (key,list(value))