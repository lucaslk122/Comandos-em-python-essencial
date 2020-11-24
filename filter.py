# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:11:07 2020

@author: ldiniz
"""
"""
filters serve para filtrar dados numa determinada coleção.
filter recebe dois parametros, sendo uma função e um iteravel

#exemplo

mport statistics # biblioteca para trabalhar com dados estatisticos

sensor = [1.3, 4.5, 7.8, 9.5, 10, 1, 2, 3] #pode ser dados coletados de algum lugar
media = statistics.mean(sensor) #mean significa que ele vai pegar a media dos numeros passados na lista "sensor"
print(round(media,2))
res = filter(lambda x: x > media, sensor) #ira filtrar um dado conjunto de dados, baseado na expresão lambada
print(list(res))

#exemplo 2

paises = ['', "Brasil", "Paraguai", '', "Noroega", '', "Uruguai"]
#res = filter(lambda pais: len(pais) > 0, paises) Outra forma de fazer
res = filter(None, paises) # Nnone é um tipo de variavel None, isso significa que ele vai filtrar por um vazio
print(list(res))

#exemplo 3

usuarios = [
            {"Username":"Lucas", "Tweets":["Eu sou muito azarado","Queria morrer","Evangelion é o menor anime de todos"]},
           { "Username":"Sara", "Tweets":[]},
           { "Username":"Pedro", "Tweets":["Gosto de comer banana","Pizza é a melhor comida"]},
            {"Username":"Sarah", "Tweets":["Gosto de alimentos saudaveis","Gosto do playstation 5"]},
           { "Username":"Lucas", "Tweets":[]},
           { "Username":"Andreia", "Tweets":["Gosto do lucas, acho ele bem inteligente"]},
           { "Username":"Lucas", "Tweets":[]},
           { "Username":"Rosangela", "Tweets":["Prefiro nem comentar"]}
    ]

inativos = filter(lambda usuario: len(usuario["Tweets"]) == 0, usuarios)
print(list(inativos))

#Outra forma exercicio 3.5
usuarios = [
            {"Username":"Lucas", "Tweets":["Eu sou muito azarado","Queria morrer","Evangelion é o menor anime de todos"]},
           { "Username":"Sara", "Tweets":[]},
           { "Username":"Pedro", "Tweets":["Gosto de comer banana","Pizza é a melhor comida"]},
            {"Username":"Sarah", "Tweets":["Gosto de alimentos saudaveis","Gosto do playstation 5"]},
           { "Username":"Lucas", "Tweets":[]},
           { "Username":"Andreia", "Tweets":["Gosto do lucas, acho ele bem inteligente"]},
           { "Username":"Lucas", "Tweets":[]},
           { "Username":"Rosangela", "Tweets":["Prefiro nem comentar"]}
    ]

for inativos in range(usuarios):
    if len(usuarios["Tweets"]) == 0 :
        print("Usuarios inativos: ", inativos)
    else:
        pass
""" 



