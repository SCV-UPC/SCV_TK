from subprocess import check_output

def cerca():
	"""
	Retorna el valor de la IP local de la Raspberry. Es suposa que aquest valor
	no varia mentre la Raspberry esta connectada. En cas que la IP canvies seria
	necessari fer un reset de la Raspberry. Es recomana tenir el modem configurat 
	amb ip's estatiques per eliminar aquest inconvenient. A pesar d'aixo, en 
	condicions normals la IP no canvia quan la Raspberry esta funcionant. 
	"""

	IP=check_output(['hostname', '-I'])
	return IP.strip()

print cerca()


