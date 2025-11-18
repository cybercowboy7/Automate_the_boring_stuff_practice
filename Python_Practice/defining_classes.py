class Router:
	'''Router Class'''  #Doc string to document what the class is for 
	def __init__(self, model, swversion, ip_add):
		'''initialize values'''
		self.model = model
		self.swversion = swversion
		self.ip_add = ip_add
rtr1 = Router("iosV", "15.6.7", "10.1.1.1")
