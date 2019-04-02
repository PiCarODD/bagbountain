import urllib2
import requests
import os
import sys
import time
print """


__________            __________                     __          
\______   \__ __  ____\______   \ ____  __ __  _____/  |_ ___.__.
 |    |  _/  |  \/ ___\|    |  _//  _ \|  |  \/    \   __<   |  |
 |    |   \  |  / /_/  >    |   (  <_> )  |  /   |  \  |  \___  |
 |______  /____/\___  /|______  /\____/|____/|___|  /__|  / ____|
        \/     /_____/        \/                  \/      \/     


"""
def slowprint(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)	
inp1=raw_input("Enter Target URL for sublist:")
url1="python ./Sublist3r/sublist3r.py -d "+inp1+" -o ./url/"+inp1.split('.')[0]+".txt"
os.system(url1)
slowprint("[!]Subdomains ready! Checking valid url of not........")
domain=""
urls=""
with open("./url/"+inp1.split('.')[0]+".txt",'r') as f:
    f=f.readlines()
    for i in range(len(f)):
      	url=f[i].strip('\n')
      	url="https://"+url
      	try:
      		r=requests.get(url,timeout=0.4)
      	except requests.exceptions.ConnectionError:
      		url="http://"+url
      	except requests.exceptions.Timeout:
      		slowprint("URL take too long to response skipped!")
 	slowprint("[!]Fuzzing url..."+url)
 	fuzz="python ./Photon/photon.py -u "+url+" -o ./url"
 	os.system(fuzz)
slowprint("Done! Thanks for using my script")

			
