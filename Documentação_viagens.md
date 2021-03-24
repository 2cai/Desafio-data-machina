# Documentação da Api viagem explicando as funções usadas

## Toda construção da API foi utilizada com o método post, com as funções a seguir usadas para retornar o desejado, de tal maneira que essas funções foram construídas com a biblioteca lib_viagens que possui sua documentação também nesse repositório.

## async def list_normalization(list:list):
- Função usada para a chamada da API "/get_normalization/" e retorna a lista passada normalizada

## async def time_travel(atual:str,destino:str,p:int):
- Função usada para a chamada da API "/viagem/" e retorna dados_viagem(atual,destino,p)

## async def travel(lista_t:list):
 - Função usada para a chamada da API "/otimizar_simples/" e retorna otimizar(lista_t)

 ## async def travel_otimizada (lista_t:list):
 - Função usada para a chamada da API "/otimizar_completo/" , e retorna uma lista com uma rota de viagens otimizada pelo "simulated annealing".
