import numpy as np
from random import random, randint, choice, uniform
import copy
import sys
from math import cos, exp, sqrt
import math
import benchmarks

def jaya(f):
    print("************************JAYA ALGORITHM*************************************")
    gens = 100
    pop_size = 40
    if f == 1:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 2:
        dimensions = 30
        min_value = -10
        max_value = 10
    if f == 3:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 4:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 5:
        dimensions = 30
        min_value = -30
        max_value = 30
    if f == 6:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 7:
        dimensions = 30
        min_value = -1.28
        max_value = 1.28
    if f == 8:
        dimensions = 30
        min_value = -500
        max_value = 500
    if f == 9:
        dimensions= 30
        min_value = -5.12
        max_value = 5.12
    if f == 10:
        dimensions= 30
        min_value = -32
        max_value = 32
    if f == 11:
        dimensions= 30
        min_value = -600
        max_value = 600
    if f == 12:
        dimensions= 30
        min_value = -50
        max_value = 50
    if f == 13:
        dimensions= 30
        min_value = -50
        max_value = 50
    if f == 14:
        dimensions= 2
        min_value = -65.536
        max_value = 65.536
    if f == 15:
        dimensions= 4
        min_value = -5
        max_value = 5
    if f == 16:
        dimensions= 2
        min_value = -5
        max_value = 5
    if f == 17:
        dimensions= 2
        min_value = -5
        max_value = 15
    if f == 18:
        dimensions= 2
        min_value = -2
        max_value = 2
    if f == 19:
        dimensions= 3
        min_value = 0
        max_value = 1
    if f == 20:
        dimensions= 6
        min_value = 0
        max_value = 1
    if f == 21:
        dimensions= 4
        min_value = 0
        max_value = 10
    if f == 22:
        dimensions= 4
        min_value = 0
        max_value = 10
    if f == 23:
        dimensions= 4
        min_value = 0
        max_value = 10
    population = np.zeros(( pop_size, dimensions ))
    for i in range(pop_size):
        for j in range(dimensions):
            population[i][j] = uniform( min_value, max_value )   #initializing the population

    best_fitness = sys.maxsize
    best_index = -1
    best_ind = np.zeros(( dimensions ))
    worst_fitness = 0
    worst_index = -1
    worst_ind = np.zeros(( dimensions ))
    fit_matrix = np.zeros(( pop_size ))
    
    
    for i in range( pop_size ):
        fitness_value = benchmarks.fitness( population[i], dimensions,f)  #calculating fitness of every individual
        fit_matrix[i] = fitness_value
        if fitness_value < best_fitness:   #finding best fit element
            best_fitness = fitness_value
            best_index = i
            best_ind = population[i]
        if fitness_value > worst_fitness:   #finding worst fit element
            worst_fitness = fitness_value
            worst_index = i
            worst_ind = population[i]

    for g in range( gens):       # iterating over generations
        #if g == 0 or g==gens-1:

        #print( best_fitness)
        #print(population)
        #print()
        for i in range(pop_size):
            new_value = np.zeros(( dimensions ))
            for j in range(dimensions):
                new_value[j] = population[i][j] + random()*( best_ind[j] - abs(population[i][j]) ) - random()*( worst_ind[j] - abs(population[i][j]))  # jaya equaion

            new_value_fit = benchmarks.fitness( new_value, dimensions, f )
            current_fit = fit_matrix[i]
            if new_value_fit < current_fit:   #replacing current element with new element if it has better fitness
                population[i] = new_value
                fit_matrix[i] = new_value_fit

  
        for i in range( pop_size ):              # finding the best and worst element


            if fit_matrix[i] < best_fitness :
                best_fitness = fit_matrix[i]
                best_fitness_index = i
                best_ind = population[i]

            if fit_matrix[i] > worst_fitness :
                worst_fitness = fit_matrix[i]
                worst_fitness_index = i
                best_ind = population[i]



    print('Best Fitness: '+str(best_fitness)+' Worst Fitness '+ str(worst_fitness)+' Average '+str(np.mean(fit_matrix))
          +' Standard Deviation '+str(np.std(fit_matrix)))
    return [best_fitness,worst_fitness,np.mean(fit_matrix),np.std(fit_matrix)]

def jaya_modified(f):
    print("*********************MODIFIED JAYA ALGORITHM*****************************")
    gens = 100
    pop_size = 40
    if f == 1:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 2:
        dimensions = 30
        min_value = -10
        max_value = 10
    if f == 3:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 4:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 5:
        dimensions = 30
        min_value = -30
        max_value = 30
    if f == 6:
        dimensions = 30
        min_value = -100
        max_value = 100
    if f == 7:
        dimensions = 30
        min_value = -1.28
        max_value = 1.28
    if f == 8:
        dimensions = 30
        min_value = -500
        max_value = 500
    if f == 9:
        dimensions= 30
        min_value = -5.12
        max_value = 5.12
    if f == 10:
        dimensions= 30
        min_value = -32
        max_value = 32
    if f == 11:
        dimensions= 30
        min_value = -600
        max_value = 600
    if f == 12:
        dimensions= 30
        min_value = -50
        max_value = 50
    if f == 13:
        dimensions= 30
        min_value = -50
        max_value = 50
    if f == 14:
        dimensions= 2
        min_value = -65.536
        max_value = 65.536
    if f == 15:
        dimensions= 4
        min_value = -5
        max_value = 5
    if f == 16:
        dimensions= 2
        min_value = -5
        max_value = 5
    if f == 17:
        dimensions= 2
        min_value = -5
        max_value = 15
    if f == 18:
        dimensions= 2
        min_value = -2
        max_value = 2
    if f == 19:
        dimensions= 3
        min_value = 0
        max_value = 1
    if f == 20:
        dimensions= 6
        min_value = 0
        max_value = 1
    if f == 21:
        dimensions= 4
        min_value = 0
        max_value = 10
    if f == 22:
        dimensions= 4
        min_value = 0
        max_value = 10
    if f == 23:
        dimensions= 4
        min_value = 0
        max_value = 10

    #generating first population
    population = np.zeros(( pop_size, dimensions ))
    for i in range(pop_size):
        for j in range(dimensions):
            population[i][j] = uniform( min_value, max_value )   #initializing the population

    best_fitness = sys.maxsize
    best_index = -1
    best_ind = np.zeros(( dimensions ))
    worst_fitness = 0
    worst_index = -1
    worst_ind = np.zeros(( dimensions ))
    fit_matrix = np.zeros(( pop_size ))
    
    
    for i in range( pop_size ):
        fitness_value = benchmarks.fitness( population[i], dimensions, f )   #calculating fitness of every individual
        fit_matrix[i] = fitness_value
        if fitness_value < best_fitness:                          #finding best fit element
            best_fitness = fitness_value
            best_index = i
            best_ind = population[i]
        if fitness_value > worst_fitness:                         #finding worst fit element
            worst_fitness = fitness_value
            worst_index = i
            worst_ind = population[i]

    for g in range( gens):                                       # iterating over generations
        '''if g%50 == 0 :
            print('*******          ', g, '        *******')
        print( best_fitness)'''
        #print(population)
        #print()
        for i in range(pop_size):
            new_value = np.zeros(( dimensions ))
            for j in range(dimensions):
                new_value[j] = population[i][j] + random()*( (best_ind[j]) - abs(population[i][j]) ) - random()*( (worst_ind[j]) - abs(population[i][j]))  # jaya equaion
                if new_value[j] > max_value :    # if the element is going out of bounds, this step makes its values equal to the extremes of search region
                    new_value[j] = max_value
                if new_value[j] < min_value :
                    new_value[j] = min_value
            new_value_fit = benchmarks.fitness( new_value, dimensions, f )
            current_fit = fit_matrix[i]
            if new_value_fit < current_fit:   #replacing current element with new element if it has better fitness
                population[i] = new_value
                fit_matrix[i] = new_value_fit

        
        index = np.argmin( fit_matrix )
        if fit_matrix[ index ] < best_fitness :    # finding the best and worst element
            best_fitness = fit_matrix[ index ]
            best_index = index
            best_ind = population[ index ]

        index = np.argmax( fit_matrix )
        if fit_matrix[ index ] > worst_fitness :
            worst_fitness = fit_matrix[index]
            worst_index = index
            best_ind = population[index]
        
        '''for i in range( pop_size ):
            if fit_matrix[i] < best_fitness :
                best_fitness = fit_matrix[i]
                best_fitness_index = i
                best_ind = population[i]

            if fit_matrix[i] > worst_fitness :
                worst_fitness = fit_matrix[i]
                worst_fitness_index = i
                best_ind = population[i]'''

        #modification proposed in Jaya

        sign = [ -1, 1 ]
        temp = np.argsort( fit_matrix ) #the most fit are in the starting
        #print(temp)
        new_inds = (int)(pop_size/2)  # later half of the population( less fit population) is replaced by the following lines
        for i in range(new_inds):
            for j in range(dimensions):
                if g > gens/2:        # for first 50% of generations
                    if randint(1,100) <= 75:  # 75% chance
                        population[ temp[pop_size-1 -i] ][j] = best_ind[j] + uniform(min_value/3, max_value/3)*abs( best_ind[j] )*choice( sign ) #new value should be far away from best individual 
                    else:
                        population[ temp[pop_size-1 -i] ][j] = best_ind[j] + random()*abs( best_ind[j] )*choice( sign )  # new value should be closer to best individual, randint() produces number between 0 & 1
                else:                # for later 50% of generationgs the ratio is reversed
                    if randint(1,100) > 75:
                        population[ temp[pop_size-1 -i] ][j] = best_ind[j] + uniform(min_value/3, max_value/3)*abs( best_ind[j] )*choice( sign )
                    else:
                        population[ temp[pop_size-1 -i] ][j] = best_ind[j] + random()*abs( best_ind[j] )*choice( sign )
                if population[ temp[pop_size-1 -i] ][j] > max_value :  #replacing current element with new element if it has better fitness
                    population[ temp[pop_size-1 -i] ][j] = max_value
                if population[ temp[pop_size-1 -i] ][j] < min_value :
                    population[ temp[pop_size-1 -i] ][j] = min_value

    print('Best Fitness: '+str(best_fitness)+' Worst Fitness '+ str(worst_fitness)+' Average '+str(np.mean(fit_matrix))
          +' Standard Deviation '+str(np.std(fit_matrix)))
    return best_fitness