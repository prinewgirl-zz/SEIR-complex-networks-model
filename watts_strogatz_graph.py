#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import networkx as nx
import numpy as np

def grafowatts_strogatz(n, k, p = 0.5, seed=None):
	"""Retorna uma matriz de adjacencia de do tipo small-world 
	de acordo com o modelo de Watts e Strogatz G{n,m}.

	Parametros
	----------
	n : int
	O numero de nos.
	k : int 
	Cada no e conectado aos k vizinhos proximos em topologia de anel
	seed : int, opcional
	Semente para a criacao de numeros aleatorios (default = None).
	p: probabilidade de 
	Caso a semente seja nula,ie, None:
	random.seed(seed) 
	"""
	G = nx.to_numpy_matrix(nx.watts_strogatz_graph(n,k,p))	
	
	
	return G

