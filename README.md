# Desafio-data-machina
Os problemas em questão foram feitos usando a biblioteca FastApi para a criação de uma API que possivel chamadas para seus respectivos problemas. Para uso da API viagens é necessário baixar os arquivos desse repositório ,colocá-los em uma mesma e rodar no terminal ou em alguma IDE na pasta onde está o codigo "viagem" o seguinte código:

uvicorn viagem:app --reload
 
Em seguida,copie o url de saída e adicione um "/docs" para entrar no ambiente de teste do Fast Api. O endereço ficará da seguinte forma : //127.0.0.1:8000/docs
### Agora, os argumentos serão passados em forma de query paramerts, tendo cada chamada um dos exercícios relacionados da seguinte forma:
#### Problema 2.1:
Solucionado na chamada /get_normalization/, onde a entrada deve ser uma lista de interios ou floats como o seguinte exemplo : [1,2,5,90]. Após isso, o programa retorna a lista da entrada normalizada
### Problema 2.2:
Solucionado na chamada /viagem/, em que teremos de entrada os parâmetros:
atual : recebe uma string com o nome da cidade em que se inicia o trajeto e o nome do seu estado como no seguinte exemplo : rio de janeiro rio de janeiro
destino : recebe uma string com o nome da cidade de destino como no seguinte exemplo : juiz de fora minas gerais
p : recebe um inteiro 

Se p for igual a 2, será retornado um inteiro informado a duração da viagem em minutos, caso contrarário, será retornado um texto informando quantas horas e minutos a viagem durou e a distância percorrida como no seguinte exemplo: "A distancia percorrida séra de 184,0 km  e a duração estimada é de 2 horas e 51 minutos"

### Problema 2.2:
Possui duas soluções, uma na chamada /otimizar_simples/, em que foi usado o algormito do vizinho mais próximo e outra na /otimizar_completo/, em que foi usado meta_heurística "simulated annealing". Em ambos os casos, a entrada deve ser uma lista em que o primeiro elemento deve ser a cidade de origem dos trajeto, que nesse caso é São Paulo. A entrada deve ser passada da seguinte forma:


[{"produto":" ","valor":0,"destino":"sao paulo sp","limite":"2020-05-9"},
    {"produto":"sofá","valor":10.0,"destino":"juiz de fora mg","limite":"2020-05-10"},
        {"produto": "geladeira", "valor": 25.0, "destino": "salvador bahia", "limite": "2020-05-11"},
         {"produto": "computador", "valor": 54.0, "destino": "campo grande mato grosso do sul ", "limite": "2020-05-12"}  ]
         
Sendo:
produto: string com o nome do produto transportado
valor:  float o custo do seu transporte
destino: string com a cidade em que ele deve ser entregue e o seu estado
limite: string com a data limite que o produto deve ser entregue para a empresa obter o maior lucro com o serviço necessariamente no formato:ano-mês-dia

Ao final, teremos a lista das cidades, começando por São Paulo, na ordem em que as entregas deverão ser feitas.

Ps: na chama /otimizar_completo/,os códigos do seguinte link foram usados para a implementação do "simulated annealing": https://github.com/perrygeo/simanneal, que se encontram na pasta "annealing" nesse repositório.

