import threading

class sublime_thread(threading.Thread):
	status 		= None
	exception 	= None
	def __init__(self):
		self.exception 	= None
		self.status 	= ""
		threading.Thread.__init__(self)

	def execute(self,command):
		self.status = command
		return shell(command)