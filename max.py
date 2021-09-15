#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 20:15:38 2021

@author: anastasiya
"""

import numpy as np
s1=0
s2=0
print("Введите количество строк")
n=int(input())
print("Введите количество столбцов")
m=int(input())

a=np.zeros((n,m),'int')  
for i in range(0,n):
    for j in range(0,m):
        a[i,j]=np.around(np.random.random(1)*8+1) 
        
        '''
        заполняем матрицу(np.random.random выдает диапазон от 0 до 1,
        он не подходит, тк попадает 0 и он не 9,поэтому умножаю на 8 
        и прибаляю 1)
        
        '''
print(a)

q=int(input())
w=int(input()) 
b=False
k=0

for i in range(0,n):  #1 игрок
    for j in range(0,m):
        if q==i and w==j:
            b=True
            
if b==True: 
    s1+=a[q,w]
    a[i,j]=0
    k=j
else:
    print("Введите снова")
print(s1)
print(a)

q2=int(input())
w2=int(input())
b=False
for i in range(0,n):     #2 игрок
    if q2==i and w==k:
        b=True
if b==True:
    
    s2+=a[q2,w2]
    a[q2,w2]=0
    i=k
else:
    print("Введите снова")
print(s2)
print(a)