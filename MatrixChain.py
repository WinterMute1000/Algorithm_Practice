# -*- coding: utf-8 -*-
import numpy
def MatrixChain(value_of_chain,num_of_matrix):
    infinite=100000000
    chain=numpy.full((num_of_matrix,num_of_matrix),infinite)
    
    for i in range(0,num_of_matrix):
        chain[i][i]=0
        
    for l in range(0,num_of_matrix-1):
        for i in range(0,num_of_matrix-l):
            j=i+l
            chain[i][j]=infinite
            for k in range(i,j):
                temp=chain[i][k]+chain[k+1][j]+value_of_chain[i-1]*value_of_chain[j]*value_of_chain[k]
                if temp < chain[i][j]:
                    chain[i][j]=temp
    
    return chain[0][num_of_matrix-1]


multiple_chain=[10,20,5,15,30]
num_of_matrix=4
print MatrixChain(multiple_chain,num_of_matrix)
                

