import pygame
import time
import sys
import Pyro4

IP_MASTER=sys.argv[1]


def display_box(screen, message , posicio,tamany):

	fontobject=pygame.font.SysFont('Arial',tamany)
	if len(message)!=0:
		screen.blit(fontobject.render(message,1,(0,0,0)),posicio)

	pygame.display.flip()

def function():

	pygame.init()
	pygame.mouse.set_visible(False)
	surf=pygame.display.set_mode((1000,500))
	foto=pygame.image.load('simulador.jpg')
	final=False

	try:

		while not final:

			s=Pyro4.Proxy("PYRO:jasper.Simulador@%s:5123"%(IP_MASTER))

			t=s.temperatura()
			print t
			a=s.alarma()
			print a

			surf.blit(foto,(0,0))
			display_box(surf,t, (200,350),50)
			display_box(surf,a, (650,350),50)
			time.sleep(0.5)

			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
				final = True

		pygame.quit()

	except SystemExit:
    		pygame.quit()
function()

	
	

	
