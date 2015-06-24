#coding=utf-8

import urllib2
import os
import sys
import time

def response_time(lan,name):

	path="Google/"+name

	audio = open(path,'rb')
	audio_data=audio.read()
	filesize = os.path.getsize(path)

	url="http://www.google.com/speech-api/v2/recognize?client=chromium&lang=%s&key=%s" %       (lan,"AIzaSyDgU56QeumsMHrJ6kP7xXOMCM8hFOKZp6U")

	req = urllib2.Request(url)
	req.add_header('Content-type','audio/l16; rate=16000')
	req.add_header('Content-length', str(filesize)) 
	req.add_data(audio_data)

	t1=time.time()
	response = urllib2.urlopen(req)
	t2=time.time()

	repo=response.read()
	dif=t2-t1

	return dif,repo

