
# coding: utf-8

# In[ ]:

#1
import math
t1= input("Ingrese Latitud")
g1= input("Ingrese longitud")
t2= input("Ingrese segunda latitud")
g2= input("Ingrese segunda longitud")

def gra(a):
    return (a*3.1416)/180

dis=6371.01*math.acos(math.sin(gra(t1))*math.sin(gra(t2))+math.cos(gra(t1))*math.cos(gra(t2))*math.cos(gra(g1)-gra(g2)))
print dis, "Kilometros"
#Luis Manuel Garcia Valdivia

