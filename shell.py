import subprocess

def shell(command):
	process = subprocess.Popen(command,\
	stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.STDOUT,\
	shell=True)
	r = process.communicate()
	if process.returncode!=0:
		raise SystemError(r[0])
	else:
		return r[0][0:-1]