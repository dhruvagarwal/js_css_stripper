from bs4 import BeautifulSoup as bs
import sys,os
from xml.etree import ElementTree

def stripper(directory,filename):
	html=open(directory+'/'+filename,'r').read()
	soup=bs(html)
	l=os.popen('ls '+directory).read()
	if 'js' not in l.split():
		os.system('mkdir '+directory+'/js')
	if 'css' not in l.split():
		os.system('mkdir '+directory+'/css')
	for js in soup.find_all('script'):
		try:
			link=js["src"]
			if link.startswith('http'):
				os.system('wget '+link + ' -P '+directory+'/js/')
				js["src"]='js/'+js["src"].split('/')[-1].strip()
		except:
			continue

	for css in soup.find_all('link'):
		try:
			link=css['href']
			if link.startswith('http'):
				os.system('wget '+link + ' -P '+directory+'/css/')
				css['href']='css/'+css['href'].split('/')[-1].strip()
		except:
			continue
	
	return soup.prettify()

directory="."
s=raw_input('Enter Complete Path of the directory(leave blank for current directory): ')

if s!="":
	if s.endswith('/'):
		s=s[:-1]
	directory=s
try:
	l=os.popen('ls '+directory).read()
	for x in l.split():
		if x.endswith('.html'):
			newhtml=stripper(directory,x)
			with open(directory+'/'+x,'w') as f:
				f.write(newhtml.encode('utf8'))
except:
	print 'Invalid Path'
	sys.exit()