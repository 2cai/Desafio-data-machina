import statistics
from fastapi import FastAPI
from datetime import date, timedelta
import abc
import copy
import datetime
from datetime import date, timedelta
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import math
import random
from collections import defaultdict
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
import unidecode

def entrada_dados_viagem(nome):
    sem_acentos = unidecode.unidecode(nome)
    return sem_acentos.lower()

def dados_viagem(atual,destino,p):
    atual_l = entrada_dados_viagem(atual)
    destino_l = entrada_dados_viagem(destino)
    if p==2 and atual_l==destino_l:
        return 0
#passando as cidades
#ajustando as entradas para a url
    atual_ok = atual_l.replace(' ','+')
    destino_ok = destino_l.replace(' ','+')
# pegando o url de busca das distancias
    req = requests.get("https://www.google.com/search?q=distancia+entre+{}+e+{}".format(atual_ok,destino_ok))
# buscando as classes span em que há o elemento em que está o tempo de viagem e o tamanho do trajeto
    soup1 = BeautifulSoup(req.text, 'html.parser')
    soup_news = soup1.find_all("span")
# buscando o elemento em que está as horas
    texto = str(soup_news[17])
    splitado = texto.split()
    # caso a viagem dure menos de uma hora
    horas = '0'
    minutos = '0'
    n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',']
    texto_tempo = ''
    if splitado[len(splitado)-3]!= 'h':
       for x in splitado[len(splitado)-2]:
            if x in n:
                minutos = minutos + x
    else:
       for x in splitado:
            if x.startswith("AWuZUe"):
                texto_tempo =x
# obtendo a hora exata
       for x in texto_tempo:
            if x in n:
               horas = horas+x
# obtendo os minutos
       if splitado[len(splitado)-1] =='min</span>':
                minutos = splitado[len(splitado)-2]
    if p == 2:
        h = int(horas)
        m = int(minutos)
        tempos = 60*h + m
        return tempos
    else:
# obtendo a distancia em quilometros a ser percorrida
        texto_dis = str(soup_news[16])
        splitado_dis = texto_dis.split()
        distancia =''
        index_texto_dis = splitado_dis.index('via')
        for x in splitado_dis[index_texto_dis-2]:
           if x in n:
             distancia=distancia + x
    resultado = "A distancia percorrida no trajeto entre {} e {} de {} km  e a duração estimada é de {} horas e {} minutos".format(atual,destino,distancia,int(horas),int(minutos))
    return resultado


def buscarmenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return i


# função que otmiza a rota pelo algoritmo do vizinho mais proximo
def otimizar(lista):
    cidadesp = []
    for x in range (0,len(lista)):
       cidadesp.append(lista[x]["destino"])
    result = []
    atual = 'sao paulo sp'
    while (len(cidadesp) > 0):
        distancias = []
        for y in cidadesp:
            if cidadesp =='sao paulo sao paulo':
                result.append('sao paulo sao paulo')
            else:
                distancias.append(dados_viagem(atual, y, 2))
                destino = cidadesp[distancias.index(buscarmenor(distancias))]
                result.append(destino)
                cidadesp.remove(destino)
                atual = destino
    return result


def i_produtos(lista):
    # ganho total com o investimento
    ganho = 0
    for x in range(0,len(lista)):
        ganho = ganho + lista[x]['valor']

    # importancia no valor
    importancia = defaultdict(dict)
    for x in range(0,len(lista)):
        valor = lista[x]['valor']
        produto = lista[x]['destino']
        importancia[produto]= valor/ganho
    return importancia
#print(i_produtos(lista)["cu de cachorro"])


def dic_datas(lista):
    datas = defaultdict(dict)
    for x in range(0, len(lista)):
        limite = lista[x]['limite']
        produto = lista[x]['destino']
        datas[produto] = limite
    return datas


# calculando a diferença de tempo entre as datas
def peso_tempo(atual,destino,lista):
    inicial = dic_datas(lista)[atual]
    limite = dic_datas(lista)[destino]
    mdate1 = datetime.datetime.strptime(inicial, "%Y-%m-%d").date()
    rdate1 = datetime.datetime.strptime(limite, "%Y-%m-%d").date()
    delta = (rdate1 - mdate1).days
    return delta*24




def peso_atraso(atual,destino,lista):
    tempo_viajem = dados_viagem(atual, destino, 2)
    tempo_limite = peso_tempo(atual, destino, lista)
    if tempo_viajem > tempo_limite:
        return 2
    else:
        return 1



def dis_preco(atual,destino,lista,preco_c):
    if atual == destino:
        return 0
    else:
        return dados_viagem(atual,destino,2)*(1-preco_c)

def lista_cidades(lista):
    cidades = []
    for x in range(0,len(lista)):
        cidades.append(lista[x]['destino'])
    return cidades



class TravellingSalesmanProblem(Annealer):

    """Test annealer with a travelling salesman problem.
    """

    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two cities in the route."""
        # no efficiency gain, just proof of concept
        # demonstrates returning the delta energy (optional)
        initial_energy = self.energy()

        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

        return self.energy() - initial_energy

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e = e + self.distance_matrix[self.state[i-1]][self.state[i]]
        return e
