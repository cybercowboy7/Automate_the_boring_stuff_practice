class Router:
	'''Router Class'''
	def __init__(self, model, swversion, ip_add):
		'''initialize values'''
		self.model = model
		self.swversion = swversion
		self.ip_add = ip_add
	
	def getDescription(self):
		'''Return a formatted description of the router'''
		Description = f'Router Model:			{self.model}\n'\
		      	      f'Software Version:		{self.swversion}\n'\
		              f'Management Address:		{self.ip_add}'
		return Description

rtr1 = Router("iosV", "15.6.7", "10.1.1,1")
rtr2 = Router("IOSXE", "17.12.5", "192.168.1.1")


# sep is a argument for the print function that controls how the output is displayed
print("Rtr1:\n", rtr1.getDescription(), "\n", sep="")
print("Rtr2:\n", rtr2.getDescription(), "\n", sep="")



 
