#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()


def Paga(HorasSemanal, SalarioHora):
        Cadena = u'Joaquin'
        print (type(Cadena))
        Encontrado = Cadena.find('l')
        Horas = HorasSemanal > 40
        if Horas:
                HorasExtras = HorasSemanal - 40
        else:
                HorasExtras = 0
        TotalSalario = (HorasSemanal - HorasExtras) * SalarioHora + HorasExtras * SalarioHora * 1.5
        return (TotalSalario)
amigos= ['Juan', 'Alberto', 'Luis']

for amigo in amigos:
        print (amigo)

try:
        HorasSemanales = int(input ('Cuantas horas a trabajado esta semana :'))
except:
        HorasSemanales = 40
try:
        SalarioHora = int(input('Salario hora normal :'))
except:
        SalarioHora = 10

print ("Esta semana usted a ganado", Paga(HorasSemanales, SalarioHora))
