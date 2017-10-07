import numpy as np
import random

def passo_epidemico(estado_anterior, grafo, doenca, k):
	"""Retorna um vetor com o novo estado dos nos apos uma iteracao do
	passo de evolucao da epidemia.	

	Parametros
	----------
	estado_anterior : vetor com o estado anterior dos nos
	grafo: matrix n x n de adjacencia de uma rede complexa
	doenca:
	k: 
	"""
	novo_estado = np.matrix([[0 for i in xrange(1)] for r in xrange(0,estado_anterior.size)])
	
	infectuosidade = np.matrix([[0.0 for i in xrange(1)] for r in xrange(0, estado_anterior.size)])

	for individuo in xrange(0, estado_anterior.size):
		
		if estado_anterior.item(individuo) > 0:
			infectuosidade.itemset(individuo,doenca.item(estado_anterior.item(individuo) -1) )
			

	prob = (grafo*infectuosidade)*k
	
	for individuo in range(0, estado_anterior.size):
		
				
		if(estado_anterior.item(individuo) > 0):
			if (estado_anterior.item(individuo) == doenca.size):
				novo_estado.itemset(individuo,-1)
			else:
				novo_estado.itemset((individuo), estado_anterior.item(individuo) + 1)
							

		elif (estado_anterior.item(individuo) == 0):
			if ( random.random() < prob.item(individuo)):
				
				novo_estado.itemset(individuo,1)
				
		elif (estado_anterior.item(individuo) == -1):
			novo_estado.itemset(individuo, -1)	
		
	return novo_estado

