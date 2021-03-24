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
exemplo de entrada: [{"produto":" ","valor":0,"destino":"sao paulo sp","limite":"2020-05-9"}, {"produto":"sofá","valor":10.0,"destino":"juiz de fora mg","limite":"2020-05-10"}, {"produto": "geladeira", "valor": 25.0, "destino": "salvador bahia", "limite": "2020-05-11"}, {"produto": "computador", "valor": 54.0, "destino": "campo grande mato grosso do sul ", "limite": "2020-05-12"} ]

### Retorno
retorna uma lista com as cidades na ordem em que devem ser feitas as entregas, em que essa ordem foi gerada por um algormito de escolha do vizinho mais próximo.

## A partir daqui, os parâmetros lista sempre terão esse formato como na função otimizar

## i_produtos(lista):







