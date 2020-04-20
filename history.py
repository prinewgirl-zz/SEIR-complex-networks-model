import numpy as np
from copy import deepcopy
import new_states
import sir

def historico(estados_iniciais, grafo, doenca, k):
	"""Retorna uma lista com o historico do numero de nos em cada um dos estados
	de acordo com o modelo sir
	Parametros
	----------
	estados iniciais : matriz 
	Informa o estado inicial de cada um dos nos
	grafo : matriz 
	Matriz de adjacencia da rede complexa
	doenca : vetor 
	Vetor com o os valores dos diferentes estagios da doenca
	k: float
	Coeficiente relativo de infectuosidade 
	"""
	L = []
	i = 0
	estados = deepcopy(estados_iniciais)
	count = sir.sir(estados_iniciais)
	estados = new_states.passo_epidemico(estados_iniciais, grafo, doenca,k)
	while (count.item(1) > 0):
		i = i+1
		L.append(count.transpose().tolist())
		estados = new_states.passo_epidemico(estados, grafo, doenca,k)
		count = sir.sir(estados)
	
	L.append(count.transpose().tolist())
	print("retornou " + str(i))
	return i,L



