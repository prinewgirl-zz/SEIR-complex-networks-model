#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import networkx as nx
import numpy as np

def grafognM_random(n, p=0.5, seed=None):
	"""Retorna a matriz de adjacencia de rede aleatoria G{n,p}.

	Parametros
	----------
	n : int
	O numero de nos.
	p : float
	Probabilidade para a criacao de uma aresta. (default = 0.5).
	Arestas possiveis: n[n-1]/2
	seed : int, opcional
	Semente para a criacao de numeros aleatorios (default = None).

	Caso a semente seja nula,ie, None:
	random.seed(seed) 
	"""
	if seed is None:
		random.seed(seed)
	
	G = nx.to_numpy_matrix(nx.erdos_renyi_graph(n,p, seed))

	
	return G


