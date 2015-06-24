import ATT
import witai
import GoogleAPI
import NexiWave



def temps(motor):

	
	audios=["audio1sE.wav","audio1s.wav"]

	if motor=='Google':

		a='Google\n'

		for f in range(2):
			if f==0:
				lan="en-US"
			else:
				lan="es-US"

			resposta=GoogleAPI.response_time(lan,audios[f])
		
			a=a+'\n'+str(resposta)

		return a

	elif motor=='ATT':
		a='\n\nAT&T\n'

		for f in range(2):
			if f==0:
				lan="en-US"
			else:
				lan="es-US"

			resposta=ATT.response_time(lan,audios[f])
		
			a=a+'\n'+str(resposta)

		

		return a

	elif motor=='Witai':

		a='\n\nWit.ai\n'

		for f in range(2):
			if f==0:
				lan="en-US"
			else:
				lan="es-US"

			resposta=witai.response_time(lan,audios[f])
		
			a=a+'\n'+str(resposta)


		return a
