# -*- coding: utf-8 -*-
import numpy

def DPCoinChange(change,coins):
    infinite=1000000000
    coin_arr=[infinite for i in range(change+1)]
    coin_arr[0]=0
    
    for j in range(1,change+1):
        for i in range(len(coins)):
            if coins[i]<=j and coin_arr[j-coins[i]]+1<coin_arr[j]:
                coin_arr[j]=coin_arr[j-coins[i]]+1
    
    return coin_arr[change]

change=20
coins=[1,5,10,16]
print DPCoinChange(change,coins)

