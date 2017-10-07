import numpy as np

def sir(estados):
	"""Retorna um vetor com o numero de individuos 
	nos estado S, I ou R.

	Parametros
	----------
	estados : vetor com o estado  dos nos
	da rede
	"""
	vetor = np.array([0 for i in xrange(3)] )
	for individuo in range(0, estados.size):
		if (estados.item(individuo) == 0):
			vetor.itemset(0, vetor.item(0) + 1)
		elif (estados.item(individuo) == -1):
			vetor.itemset(2, vetor.item(2) + 1)
		else:
			vetor.itemset(1, vetor.item(1) + 1)
			
	return vetor
