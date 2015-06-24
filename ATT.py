import json
import requests
import time

path='ATT/'

CLIENT_ID = 'akgpcgksgua9ak6coo2gbsmcipbw4tza'
CLIENT_SECRET = 'q7m0gegmnh6aidcycvkgalczhp1m6d5y'
TOKEN = None


def get_token():

        response = requests.post("https://api.att.com/oauth/token", {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "client_credentials",
            "scope": "SPEECH"
        })
        content = json.loads(response.content)
        TOKEN = content["access_token"]
	return TOKEN

def text_from_file(token, lan,name):

        with open(path+name, 'rb') as f:
	    t1=time.time()
            response = requests.post("https://api.att.com/speech/v3/speechToText",
                headers = {
                    "Authorization": "Bearer %s" %(token),
                    "Accept": "application/json",
                    "Content-Type": "audio/wav",
                    "X-SpeechContext": "Generic",
		    "Content-Language": lan,
            }, data=f)
	    t2=time.time()
	    dif=t2-t1
	    
        content = json.loads(response.content)
        return dif,content

def response_time(lan,name):

	token=get_token()
	dif,content=text_from_file(token,lan,name)	   
	return dif,content




