
# coding: utf-8

# In[ ]:

#6
anospersona=int(raw_input("Ingrese la cantidad de anos persona: "))
if anospersona<0:
	anospersona=int(raw_input("Ingrese un numero positivo: "))
else:
	pass

def conversion(a):
	ap=0 #anos perro
	for i in range(1,a+1):
		if i<=2:
			ap=ap+10.5
		else:
			ap=ap+4
	return ap

print conversion(anospersona)
#Luis Manuel Garcia Valdivia

