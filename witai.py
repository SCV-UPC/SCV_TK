import json
import requests
import time

path='Wit.ai/'

token='AHWDLGI7GWULZLVKKTTX5FOADV74THYV'
token2='BWI3BDNQ4DUGJPD6CAM75T7FVS2YXN4P'



def text_from_file(lan,name):


        with open(path+name, 'rb') as f:
	    t1=time.time()
            response = requests.post('https://api.wit.ai/speech?v=20150508',
                headers = {
                    "Authorization": "Bearer %s" %(token),
                    "Accept": "application/json",
                    "Content-Type": "audio/wav",
                    "X-SpeechContext": "Generic",
            }, data=f)
	    t2=time.time()
	    dif=t2-t1
	
        content = json.loads(response.content)
        return dif,content

def response_time(lan,name):
	
	dif,content=text_from_file(lan,name)	    
	return dif,content

