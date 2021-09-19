import numpy as np
s1 = 0
s2 =0
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
msum = 1
nsum = 1
b1=False
while b1==False :    #1 игрок
    print("Игрок 1, введите координаты числа")
    q=int(input())
    w=int(input()) 
    for i in range (0,n):
        for j in range(0,m):
            if q==i and w==j:
                b1=True
                k=j
    if b1==True: 
        s1+=a[q,w]
        a[q,w]=0
    else:
        print("Введите координаты снова")
    print("Сумма игрока 1=",s1)
print(a)

hod = 0
while (msum!=0 or nsum!=0) and hod<2:   
    b2=False
    b1=False
    nsum=0
    while b2==False :   #Игрок 2
        for i in range (0,n):
            nsum+=a[i,k]
        if nsum!=0:
            print("Игрок 2,введите координаты числа")
            q2=int(input())
            w2=int(input())
            for i in range(0,n):  
                if q2==i and w2==k:
                    b2=True
                    k=i
            if b2==True:
                s2+=a[q2,w2]
                a[q2,w2]=0 
            else:
                print("Введите координаты снова")                     
            print("Сумма игрока 2=",s2)
        else:
            print("Игрок 2 пропускает ход")
            hod += 1
            break
        print(a)
    if hod==2:
        break
   
    msum=0
    while b1== False: #игрк 1
        for j in range (0,m):
            msum+=a[k,j]
        if msum!=0:
            print("Игрок 1,введите координаты числа")
            q=int(input())
            w=int(input())
            for j in range(0,n):   
                if q==k and w==j:
                    b1=True
                    k=j
            if b1==True:
                s1+=a[q,w]
                a[q,w]=0
            else:
                print("Введите координаты снова")                     
            print("Сумма игрока 1=",s1)
        else:
            print("Игрок 1 пропускает ход")
            hod += 1
            break
        print(a)
    
if s1==s2:
    print("Ничья!Сумма очков игрока 1-",s1,"Сумма очков игрока 2-",s2)
else:
    if s2<s1:
        print("Победил игрок 1,сумма его очков состваляет",s1)
    else:
        print("Победил игрок 2,сумма его очков состваляет",s2)