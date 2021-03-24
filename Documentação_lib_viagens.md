# Documentação Lib viagens
A biblioteca lib_viagens possui as funções utilizar na execução do programa Api e possui as seguintes funções:

## dados_viagem(atual,destino,p)
### Parâmetros de entrada
- atual: recebe uma string que deve possuir o nome da cidade de inicio como no seguinte exemplo: "juiz de fora minas gerais","Jaboatão dos Guararapes Recife".
- destino: recebe uma string que deve possuir o nome da cidade de destino s como no seguinte exemplo:"rio de janeiro rj" , "Belo Horizonte Minas Gerais
- p: inteiro
### Retorno
Se p=2 , retorna o tempo da viagem em minutos, caso contrário, retorna um texto do tipo string informando a duração da viagem e a distância percorrida como no seguinte exemplo:
"A distancia percorrida no trajeto entre rio de janeiro rio de janeiro e juiz de fora minas gerais é de 184,0 km e a duração estimada é de 2 horas e 51 minutos"

## (A partir daqui, todos os parâmetros de entrada atual e destino serão do mesmo formato como citado acima)

## entrada_dados_viagem(nome)
### Parâmetros de entrada
- nome : recebe uma string
### Retorno
Retorna essa string sem acentos e com notas as letras em minúsculo, por exemplo: nome = entrada_dados_viagem("São Paulo") , então nome = "sao paulo"
## buscarmenor(lst):
### Parâmetros de entrada
- lst: recebe uma lista de inteiros ou floats
### Retorno
retorna o menor elemento de lst

## otimizar(lista):
### Parâmetros de entrada
- lista: recebe uma lista que os elementos são da seguinte forma : {"produto": string com o nome do produto a ser transportado,"valor":float com o valor da entrega,"destino":string com a cidade de destino do produto,"limite":string com a data de entrega limite para o lucro máximo na entrega necessáriamente no formato "ano-mes-dia"}
- OBS : o primeiro elemento da lista precisa deve possuir como destino a cidade de onde o transporte começará a fazer as entradas e o limite deve ser a data em que esse transporte se inicia. Nesse primeiro elemento, o atributo produto pode ser preenchido com qualquer string e o valor com qualquer float 
exemplo de entrada: [{"produto":" ","valor":0,"destino":"sao paulo sp","limite":"2020-05-09"}, {"produto":"sofá","valor":10.0,"destino":"juiz de fora mg","limite":"2020-05-10"}, {"produto": "geladeira", "valor": 25.0, "destino": "salvador bahia", "limite": "2020-05-11"}, {"produto": "computador", "valor": 54.0, "destino": "campo grande mato grosso do sul ", "limite": "2020-05-12"} ]

### Retorno
retorna uma lista com as cidades na ordem em que devem ser feitas as entregas, em que essa ordem foi gerada por um algormito de escolha do vizinho mais próximo.

## (A partir daqui, os parâmetros lista sempre terão esse formato como na função otimizar e o exemplo de entrada usado será o mesmo)

## lista_cidades(lista):
### Parâmetros de entrada
- lista : (já mencionado)
### Retorno
Retorna uma lista com as cidades que estão nos atributos "destino" no parâmetro de entrada lista passada. 


## i_produtos(lista):
### Parâmetros de entrada:
- lista : (como mencionado)
### Retorno
retorna um dicionário com cada destino tendo a porcentagem de valor no total que pode ser obtido na viagem calculador por: porcetagem = valor/soma dos valores de toda a lista

-exemplo: {'sao paulo sp': 0.0, 'juiz de fora mg': 0.11235955056179775, 'salvador bahia': 0.2808988764044944, 'campo grande mato grosso do sul ': 0.6067415730337079}

## dic_datas(lista):
### Parâmetros de entrada:
-lista: (como mencionado)
### Retorno:
 retorna uma um dicionário em que cada destino possui como elemento a data limite de entrega 
 
 - exemplo:{'sao paulo sp': '2020-05-09', 'juiz de fora mg': '2020-05-10', 'salvador bahia': '2020-05-11', 'campo grande mato grosso do sul ': '2020-05-12'}

## peso_tempo(atual,destino,lista):
### Parâmetros de entrada:
-atual: (já mencionado)
- destino: (já mencionado)
- lista: (já mencionada)

### Retorno:
-Retona um inteiro que é a diferença de tempo em dias entre as datas limites dos parâmetros atual e destino, em que esses dois são atributos "destino" da lista e a data, atributos "limite".

## peso_atraso(atual,destino,lista):
-atual : (já mencionado)
- destino : (já mencionado)
- lista : (já mencionada)
### Parâmetros de entrada:
-atual : (já mencionado)
- destino : (já mencionado)
- lista : (já mencionada)
### Retorno:
- Retorna o inteiro 2 se dados_viagem(atual, destino, 2)  > peso_tempo(atual, destino, lista) e o inteiro 1 se dados_viagem(atual, destino, 2)<=peso_tempo(atual, destino, lista).

## TravellingSalesmanProblem(Annealer):
Importada dos códigos indicados no README para o uso do algoritmo "simulated annealing" , em que temos a função __int__ para a criação de uma matriz que relaciona todas as cidades, duas a duas, pela métrica de avalição da otimização, sendo essa métrica calculada por:

- sendo A = cidade atual e B = cidade destino:
 ### métrica = dados_viagem(A, B, 2)* i_produtos(lista_cidades(lista_t))[B] * peso_atraso(atual,destino,lista_cidades(lista_t))
 
 Além disso, teremos 





 









