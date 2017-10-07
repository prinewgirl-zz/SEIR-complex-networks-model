#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import networkx as nx
import numpy as np

def grafoscale_free(n, m, seed=None):
	"""Retorna uma matriz de adjacencia de do tipo scale-free
	 de acordo com o modelo de Barabasi e Albert G{n,m}.

	Parametros
	----------
	n : int
	O numero de nos.
	m : numero de arestas
	seed : int, opcional
	Semente para a criacao de numeros aleatorios (default = None).

	Caso a semente seja nula,ie, None:
	random.seed(seed) 
	"""
	if seed is None:
		random.seed(seed)
	
	G = nx.to_numpy_matrix(nx.barabasi_albert_graph(n,m,seed))

	
	return G


