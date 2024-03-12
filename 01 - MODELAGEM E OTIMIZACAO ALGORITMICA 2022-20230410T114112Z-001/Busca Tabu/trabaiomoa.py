# -*- coding: utf-8 -*-
"""
# **Trabalho de MOA**

### Implementação do algoritmo tabu e resolução do problema do caixeiro viajante


*   Ra: 116086 - Nathalia Mesquita Carnevalli
*   Ra: 112680 - Rodrigo Vieira de Vasconcelos
*   Ra: 108176 - Arthur Gustavo Toyotani Campanha
"""

#Importando as bibliotecas necessárias 
import math as m
import random as r

#Inicialização do problema do caixeiro viajante
#as cidades e as coordenadas (x, y) delas
cities = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (2, 3),
    'D': (5, 1),
    'E': (6, 5),
    'F': (7, 3)
}

cities

#pegando o objeto anterior e transformando em uma lista
cities_list = list(cities.keys())

#embaralhando a lista de cidades fazendo com que a solução inicial seja aleatória
r.shuffle(cities_list) 

cities_list

#função que calcula a distância entre duas cidades
def calculate_distance(city1, city2):
   x1, y1 = cities[city1]
   x2, y2 = cities[city2]
   return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#função que calcula o custo do problema (soma as distâncias entre todas as cidades) 
def calculate_total_distance(cities_list):
   cost = 0 
   for i in range(len(cities_list) - 1):
     cost += calculate_distance(cities_list[i], cities_list[i+1])
   return cost + calculate_distance(cities_list[-1], cities_list[0])

#função que gera novas soluções para a solução atual (current_solution)
def getNeighbors(current_solution, tabu_list):
  neighborhood_solutions = []
  for j in range(len(current_solution)):
        for k in range(j+1, len(current_solution)):
            new_solution = current_solution.copy()
            new_solution[j], new_solution[k] = new_solution[k], new_solution[j]

            if(new_solution not in tabu_list):
              neighborhood_solutions.append(new_solution)
  return neighborhood_solutions, j, k

#retorna uma resposta a ação executada na função
def response(res):
    return res

#algoritmo tabu 
def tabu_search(initial_solution, tabu_size, max_iterations):
  best_solution = initial_solution
  current_solution = initial_solution
  tabu_list = []

  #Verificação das entradas da função
  if((tabu_size < 0) or (max_iterations < 0) or (type(initial_solution) != list)):
    return response('É necessário passar valores válidos para executar o algoritmo tabu')

  #inicio da busca tabu de acordo com um número máximo de iterações 
  for i in range(max_iterations):
    neighborhood, j, k = getNeighbors(current_solution, tabu_list)

    #se não achar soluções naquela vizinhança adiciona uma aleatória
    if not neighborhood:
        neighborhood = [current_solution]
        
    #acha a solução que tem o menor caminho dentre as soluções atuais (current_solution)
    current_solution = min(neighborhood, key=calculate_total_distance)
    
    #atualiza a  melhor solução (best_solution) 
    if calculate_total_distance(current_solution) < calculate_total_distance(best_solution):
        best_solution = current_solution
    
    #atualiza a lista tabu para sempre gerar o máximo de soluções possíveis
    if len(tabu_list) >= tabu_size:
        tabu_list.pop(0)

    #insere na lista tabu
    tabu_list.append((current_solution[j], current_solution[k]))

  return response('A melhor solução é ' + str(best_solution) + ' com custo de ' + str(round(calculate_total_distance(best_solution), 2)))

#chamando a função tabu
tabu_search(cities_list.copy(), 4, 10)