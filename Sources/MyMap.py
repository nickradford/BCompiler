class MyMap(dict):
	def deleteAll(self):
		self.clear()
	def defined(self, key):
		return key in self