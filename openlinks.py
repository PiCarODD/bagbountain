import urllib2
import requests
import os
print """


__________            __________                     __          
\______   \__ __  ____\______   \ ____  __ __  _____/  |_ ___.__.
 |    |  _/  |  \/ ___\|    |  _//  _ \|  |  \/    \   __<   |  |
 |    |   \  |  / /_/  >    |   (  <_> )  |  /   |  \  |  \___  |
 |______  /____/\___  /|______  /\____/|____/|___|  /__|  / ____|
        \/     /_____/        \/                  \/      \/     


"""
inp1=raw_input("Enter Target URL for sublist:")
url1="python ./Sublist3r/sublist3r.py -d "+inp1+" -o "+inp1.split('.')[0]+".txt"
os.system(url1)
print "[!]Subdomains ready! Checking valid url of not........"
domain=""
urls=""
with open(inp1.split('.')[0]+".txt",'r') as f:
    for url in f.readlines():
      key=url.split('\n')
      for i in key:
      	if i!="":
      		domain='https://'+i
		try:
			r=requests.get(domain)
			print "[+]Valid url:"+domain
			print "[!]Fuzzing url..."
			fuzz="python ./Photon/photon.py -u "+domain
			os.system(fuzz)
		except requests.exceptions.ConnectionError:
			print "[-]Failed:"+domain

			
