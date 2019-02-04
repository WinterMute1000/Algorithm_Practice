# -*- coding: utf-8 -*-
import numpy

def EditDistance(string1,string2):
    m=len(string1)
    n=len(string2)
    edit_arr=numpy.zeros((m,n))
    for i in range(0,m):
        edit_arr[i][0]=i
    for j in range(0,n):
        edit_arr[0][j]=j
        
    for i in range(0,m):
         for j in range(0,n):
             alpha= 0 if string1[i]==string2[j] else 1
             edit_arr[i][j]=min([edit_arr[i][j-1]+1,edit_arr[i-1][j]+1,edit_arr[i-1][j-1]+alpha])
             
    return edit_arr[m-1][n-1]

string1="stone"
string2="strong"

print EditDistance(string1,string2)

