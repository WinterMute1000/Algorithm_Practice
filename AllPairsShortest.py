# -*- coding: utf-8 -*-
def AllPairsShortest(distance_arr,num_of_vertex):
    for k in range(0,num_of_vertax):
        for i in range(0,num_of_vertax):
            if i==k:
                continue
            for j in range(0,num_of_vertax):
                if j==k or j==i:
                    continue
                distance_arr[i][j]=min([distance_arr[i][k]+distance_arr[k][j],
                                       distance_arr[i][j]])
    

weight_arr=[[0,4,2,5,99],[99,0,1,99,4],[1,3,0,1,2],[-2,99,99,0,2],[99,-3,3,1,0]]
num_of_vertax=5

AllPairsShortest(weight_arr,num_of_vertax)

print weight_arr

