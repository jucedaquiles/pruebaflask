lista = [2]



def ListaPrimos(Lista):
   for x in range(2, Max+1) :
      for i in range(2, x) :
         if x % i == 0 :
            break
         else :
            Lista.append(x)
            break
         
Max = int(input ("Obtine los numeros primos hasta el numero :"))
ListaPrimos(lista)
print (lista)