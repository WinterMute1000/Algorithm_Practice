# -*- coding: utf-8 -*-
def SetCover(u,f):
    while len(u)!=0:
        best_include=0
        for i in range(len(f)):
            if len(u&f[i])>len(u&f[best_include]):
                best_include=i
                
        u=u-f[best_include]
        print f[best_include]
        del f[best_include]
        
u=set([1,2,3,4,5,6,7,8,9,10])
f=[set([1,2,3,8]),set([1,2,3,4,8]),set([1,2,3,4]),set([2,3,4,5,7,8]),set([4,5,6,7])
  ,set([5,6,7,9,10]),set([4,5,6,7]),set([1,2,4,8]),set([6,9]),set([6,10])]

SetCover(u,f)
        
            
            

