# -*- coding: utf-8 -*-
import numpy
def Knapsack(volumn_of_pack,weight_of_things,value_of_things):
    n=len(weight_of_things)+1
    c=volumn_of_pack+1
    knapsack=numpy.zeros((n,c))
     
    for i in range(1,n):
        for w in range(1,c):
             
            if weight_of_things[i-1]>w:
                knapsack[i][w]=knapsack[i-1][w]
            else:
                knapsack[i][w]=max([knapsack[i-1][w],knapsack[i-1][w-weight_of_things[i-1]]+value_of_things[i-1]])
    return knapsack[n-1][c-1]

volumn_of_pack=10
weight_of_things=[5,4,6,3]
value_of_things=[10,40,30,50]

print Knapsack(volumn_of_pack,weight_of_things,value_of_things)
                 
