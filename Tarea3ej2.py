
# coding: utf-8

# In[ ]:

#2
n=int(input("Ingrese su entero"))
def suma(n):
    x=0
    while n>0:
        x=x+n%10
        n =n/10
    print x + n
suma(n)
#Luis Manuel Garcia Valdivia

