import sublime,sublime_plugin
from sublime_thread import sublime_thread
from shell import shell

import os, re

def is_python_file(view):
    return bool(re.search('Python', view.settings().get('syntax'), re.I))

def unlink_pyc():
	for root, dirs, files in os.walk('.'):
		for f in files:
			fileName, fileExtension = os.path.splitext(f)
			if fileExtension == ".pyc":
				if f[0:-1] not in files:
					os.unlink(os.path.join(root, f))

class unlink_thread(sublime_thread):
	def run(self):
		try:
			self.status = "delete .pyc files"
			unlink_pyc()
		except Exception, e:
			self.exception=str(e)

class DeletePycListener(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if is_python_file(view):
			unlink_pyc()
			if view.file_name() is not None:
				ThreadProgress(unlink_thread(),callback=None)
