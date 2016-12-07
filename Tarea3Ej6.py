
# coding: utf-8

# In[ ]:

#6
x= int(input("Introduzca años:"))

def funcion(x):
  if (x<0):
    print "Error"
  if (x==1):
    x=1
    print x, "año humano"
  elif (x==2):
    x=10.5
    print x, "años humanos"
  else:
    x=x*4
    print x, "años humanos"
funcion(x)

