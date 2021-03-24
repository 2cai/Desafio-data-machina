import statistics
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from typing import List
from lib_viagens import entrada_dados_viagem,dados_viagem,otimizar,buscarmenor,dic_datas,i_produtos,peso_tempo,lista_cidades,peso_atraso,TravellingSalesmanProblem
from collections import defaultdict
import unidecode
from simanneal import Annealer
import abc
import copy
import datetime
import math
import pickle
import random
import signal
import sys
import time


app= FastAPI()


@app.post("/get_normalization/")
async def list_normalization(list:list):
   normal = []
   mean = statistics.mean(list)
   std = statistics.stdev(list)
   for x in list:
      element = (x - mean) / std
      normal.append(element)
   return normal


@app.post("/viagem/")
async def time_travel(atual:str,destino:str,p:int):
    return dados_viagem(atual,destino,p)


@app.post("/otimizar_simples/")
async def travel(lista_t:list):
    return otimizar(lista_t)

@app.post("/otimizar_completo/")
async def travel_otimizada (lista_t:list):
    lista = lista_cidades(lista_t)
    init_state = lista
    random.shuffle(init_state)
    distance_matrix = defaultdict(dict)
    importancia_produtos = i_produtos(lista_t)
    for va in init_state:
        for vb in init_state:
            distancia = dados_viagem(va, vb, 2)
            peso_preco = importancia_produtos[vb]
            distance_matrix[va][vb] = distancia *(1- peso_preco) * peso_atraso(va, vb, lista_t)

    tsp = TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.set_schedule(tsp.auto(minutes=0.2))
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()
    while state[0] != 'sao paulo sp':
        state = state[1:] + state[:1]
    return(state)





















