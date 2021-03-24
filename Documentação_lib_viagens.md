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

exemplo de entrada: 




