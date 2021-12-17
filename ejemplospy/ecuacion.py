import math

ListaNumeros = [1,1,1]
resultados = [0,0]

#Entrada de valores en la lista abc. Si a es cero no es de segundo grado y devuelve false
def entradaValores(abc): 
   print ("Calculo de ecuacion de segundo grado con enteros ")
   abc[0] = int(input ("Introduzca el a (a debe de ser > 0) :"))
   Retorno = abc[0] != 0
   if Retorno :
      abc[1] = int(input ("Introduzca el b :"))
      abc[2] = int(input ("Introduzca el c :"))
   return Retorno
   
#Calcula el resultado de la ecuacion
#abc es una lista con los 3 valores
#solucion es una lista con los 2 resultados
def CalculaEcuacion(abc, solucion):
   CalculoRaiz = abc[1]**2 - (4 * abc[0] * abc[2])
   retorno = (CalculoRaiz >= 0)
   
   if retorno :
      solucion[0] = (-abc[1] + math.sqrt(CalculoRaiz)) / (2 * abc[0])
      solucion[1] = (-abc[1] - math.sqrt(CalculoRaiz)) / (2 * abc[0])
   return retorno 
         
      
if entradaValores(ListaNumeros) :
   if not CalculaEcuacion(ListaNumeros, resultados) :
      print ("No tiene solucion")
   else :
      print (resultados)
else :
   print ("El valor de a no debe de ser cero")
       


