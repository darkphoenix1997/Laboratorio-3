
# coding: utf-8

# In[ ]:

#3
a= int(input("Ingrese numero entero:"))
b= int(input("Ingrese numero entero:"))
c= int(input("Ingrese numero entero:"))

if a<b and a<c and b<c:
  print a, b, c
if a<c and a<b and c<b:
  print a, c, b
if b<a and b<c and a<c:
  print b, a, c
if b<c and b<a and c<a:
  print b, c, a
if c<a and c<b and a<b:
  print c, a, b
if c<b and c<a and b<a:
  print c, b, a
else:
  "No se aceptan numeros iguales"
#Luis Manuel Garcia Valdivia

