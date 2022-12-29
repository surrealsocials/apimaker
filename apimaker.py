#apimaker.py
import os

print('methods: \napimaker.make(name,__file__)\napimaker.addhere(__file__)\n')

class Builder:
	def __init__(self,name,file):
		self.name=name
		self.file=file

	def setup(self):
		open(self.name,'w').close()
		if isinstance(self.file,list)is True:
			for f in self.file:
				template=(f'import {f[:-3]}')
				with open(self.name,'a') as f: f.write(template+'\n')
		else:
			self.file=self.file.split('\\')[len(self.file.split('\\'))-1]
			template=(f'import {self.file[:-3]}')
			with open(self.name,'a') as f: f.write(template+'\n')

		template=(f'from flask import Flask\n\napp = Flask(__name__)')
		with open(self.name,'a') as f: f.write(template+'\n\n')
		template=('@app.route("/")\ndef index():\n	return "welcome to your API"')
		with open(self.name,'a') as f: f.write(template+'\n\n')

	def GET(self,fn,data=None):
		if data==None:
			data='return'
		template=f'@app.route("/{fn}",methods=["GET"])\ndef {fn}():\n	'
		with open(self.name,'a') as f: f.write(template+data+'\n\n')

	def POST(self,fn,data=None):
		if data==None:
			data='return'
		template=f'@app.route("/{fn}",methods=["POST"])\ndef {fn}():\n	'
		with open(self.name,'a') as f: f.write(template+data+'\n\n')

	def run(self):
		template="if __name__ == '__main__':\n	app.run()"
		with open(self.name,'a') as f: f.write(template+'\n\n') 

	def start(self):
		os.system(f'python {self.name}')

def make(name,file,cwd=None):
	if cwd != None:
		os.chdir(cwd)
	API=Builder(name,file)
	API.setup()
	API.GET('getfun')
	API.POST('postfun')
	API.run()
	#API.start()


def addhere(file):
	make('temp.txt',file)

	with open('temp.txt','r') as f :
		with open(file,'a') as f2: f2.write(f.read())
	
	os.remove('temp.txt')
