import json
import sys

class printJson():
	def __init__(self):
		with open('students.json','r') as self.file:
			self.data = json.load(self.file)

		print "Type: ",
		print type(self.data)

		print "Length: ",
		print len(self.data['students'])

		for key in self.data['students']:
			print "Name: " + str(self.data['students'][key]['Name']),
			print "Age: " + str(self.data['students'][key]['Age']),
			print "Class: " + str(self.data['students'][key]['Class'])


logic = printJson()
		