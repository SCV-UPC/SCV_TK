#coding=utf-8

import time
import sys, os, json, urllib2, urllib, time
import requests

USERNAME = "edugodori@gmail.com"
PASSWORD = "38W5K89EVPW5YA6"

path= "Google/audio3sE.wav"

   
url = 'https://api.nexiwave.com/SpeechIndexing/file/storage/' + USERNAME +'/recording/?authData.passwd=' + PASSWORD + '&auto-redirect=true&response=application/json'

def response_time():

	t1=time.time()
	r = requests.post(url, files={'mediaFileData': open(path,'rb')})
	t2=time.time()
	dif=t2-t1
	return dif,'caca'
		
	    
	    

  
    
   
