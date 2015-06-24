import pygame
import time
import sys
import Pyro4

#IP_MASTER=sys.argv[1]
IP_MASTER='192.168.1.40'
simulador=Pyro4.Proxy("PYRO:jasper.Simulador@%s:5123"%(IP_MASTER))

fons=pygame.image.load('simulador/simulador.png')
persiana1=pygame.image.load('simulador/persiana1.png')
persiana2=pygame.image.load('simulador/persiana2.png')
persiana3=pygame.image.load('simulador/persiana3.png')
persiana4=pygame.image.load('simulador/persiana4.png')
persiana5=pygame.image.load('simulador/persiana5.png')
persiana6=pygame.image.load('simulador/persiana6.png')
persiana7=pygame.image.load('simulador/persiana7.png')
porta1=pygame.image.load('simulador/porta1.png')
porta2=pygame.image.load('simulador/porta2.png')
porta3=pygame.image.load('simulador/porta3.png')
porta4=pygame.image.load('simulador/porta4.png')
porta5=pygame.image.load('simulador/porta5.png')
porta6=pygame.image.load('simulador/porta6.png')
porta7=pygame.image.load('simulador/porta7.png')
porta8=pygame.image.load('simulador/porta8.png')
porta9=pygame.image.load('simulador/porta9.png')
porta10=pygame.image.load('simulador/porta10.png')
llum=pygame.image.load('simulador/bombeta.png')
llum2=pygame.image.load('simulador/bombeta2.png')
musica=pygame.image.load('simulador/nota.png')
gota=pygame.image.load('simulador/gota.png')
ventilador=pygame.image.load('simulador/ventilador.png')
televisor=pygame.image.load('simulador/televisor.png')

fotos=[fons,persiana1,persiana2,persiana3,persiana4,persiana5,persiana6,persiana7,porta1,porta2,porta3,porta4,porta5,porta6,porta7,porta8,porta9,porta10,llum,llum,llum,llum,llum,llum,llum2,llum2,
llum2,llum2, gota,televisor,ventilador,musica,musica,musica,musica]

index=[(0,0),(116,878),(400,878),(735,878),(992,878),(1250,878),(1479,374),(522,231),(258,231),(392,457),(537,544),(792,392),(803,541),(983,540),(888,230),(1212,231),(929,2),(1110,428),(200,350),
(320,700), (770,720),(990,720),(1280,400),(700,450),(100,150),(430,150),(730,150),(1100,150),(650,30),(23,700),(450,700),(100,600),(200,600),(900,300),(1000,350)]

def display_box(screen, message , posicio,tamany):

	fontobject=pygame.font.SysFont('Arial',tamany)
	if len(message)!=0:
		screen.blit(fontobject.render(message,1,(0,0,0)),posicio)

	pygame.display.flip()

def function():

	pygame.init()
	pygame.mouse.set_visible(False)
	surf=pygame.display.set_mode((1500,900))
	final=False
	
	while not final:

		try:


			estats=simulador.valor_actual()
			alarma=simulador.alarma()
			temperatura=simulador.temperatura()
			canal=simulador.canal()

			for idx,el in enumerate(estats):
				if el==1:
					foto=fotos[idx]
					surf.blit(foto,index[idx])
	
					
			display_box(surf,alarma, (1220,780),50)
			display_box(surf,temperatura, (1220,600),50)

			if estats[29]:
				display_box(surf,canal, (140,750),50)
			time.sleep(0.5)

			pygame.display.flip()

			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
				final = True

		except SystemExit:

    			pygame.quit()

		except:
			pass

	pygame.quit()

function()

	
	

	
