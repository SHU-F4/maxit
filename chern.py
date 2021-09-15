# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
s1=0
s2=0
print("Введите количество строк")
n=int(input())
print("Введите количество столбцов")
m=int(input())

a=np.zeros((n,m))  
for i in range(0,n):
    for j in range(0,m):
        a[i,j]=np.around(np.random.random(1)*9)
print(a)
summa=0
for i in range(0,n):
    for j in range(0,m):
        summa+=a[i,j]
        while summa!=-9:
            q=int(input())
            w=int(input())
            b=False
            k=0

            for i in range(0,n):
                for j in range(0,m):
                    if q==i and w==j:
                        b=True
            
            if b==True: 
                s1+=a[q,w]
                a[q,w]=-1
                k=j
            else:
                print("Введите снова")
            print(s1)
            print(a)

            q2=int(input())
            w2=int(input())
            b=False
            for i in range(0,n):
                if q2==i and w2==k:
                    b=True
            if b==True:
    
                s2+=a[q2,w2]
                a[q2,w2]=-1
                i=k
            else:
                print("Введите снова")
            print(s2)
            print(a)
      