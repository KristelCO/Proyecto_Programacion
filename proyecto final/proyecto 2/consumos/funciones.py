import data.energia as eg

def obtenerdatos():
  return eg.consumo_energia
def obtenerinfo():
  return eg.informacion

###pregunta 1###
def obtenerconsumo(consumo_energia,informacion):
  planta=input("Ingrese el nombre de una planta: ").title()
  lista_plantas=list(consumo_energia.keys())
  while planta not in lista_plantas:
    print("Por favor ingrese una planta válida")
    planta=input("Ingrese el nombre de una planta: ")
  ciudad=input("Ingrese el nombre de una ciudad:").lower().capitalize()
  lista_ciudades=list(consumo_energia[planta].keys())
  while ciudad not in lista_ciudades:
    print("Por favor ingrese una ciudad válida")
    ciudad=input("Ingrese el nombre de una ciudad:").lower().capitalize()

  consumo=consumo_energia[planta][ciudad]["consumos"]
  consumo=sum(consumo)
  linea="Los megavatios totales consumidos por la ciudad {} en la planta {} es de {} megavatios".format(ciudad,planta,consumo)
  return linea


### pregunta 2###
def obtenerdic(consumo_energia,informacion):
  ciudad=input("Ingrese el nombre de una ciudad:").lower().capitalize() 
  d={}
  lista_plantas=list(consumo_energia.keys())
  for planta in lista_plantas:
    if ciudad in consumo_energia[planta].keys():
      d[planta]=0
      tupla_consumo=consumo_energia[planta][ciudad]["consumos"]
      d[planta]=sum(tupla_consumo)
    else:
      d[planta]=0
  return d

### pregunta 3 ###
def obtenertTarifa(consumo_energia,informacion):
  region=input("Ingrese una region: ").lower()
  lista_r=list(informacion.keys())
  while region not in lista_r:
   region=input("Ingrese una region: ").lower()
  lista_plantas=list(consumo_energia.keys())
  ciudades=informacion[region]
  lista_totales=[]
  for planta,ciudad in zip(lista_plantas,ciudades):
    if ciudad in consumo_energia[planta]:
      consumo=consumo_energia[planta][ciudad]["consumos"]
      consumo=sum(consumo)
      tarifa=consumo_energia[planta][ciudad]["tarifa"]
      total=consumo*tarifa
      lista_totales.append(total)
      total=sum(lista_totales)
  linea='La region',region,'ha recaudado ${}'.format(total)
  return linea
  
###pregunta 4 ####
def solicitud_mes(n1,n2,n3,n4):
    tarifa=(eg.consumo_energia[n3][n2]["tarifa"])
    op=-1
    while op!=0:
        if n4 == 1 or "Enero":
            print('El mes de Enero')
            n4=(1-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 2 or "Febrero":
            print('El mes de Febrero')
            n4=(2-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 3 or "Marzo":
            print('El mes de Marzo')
            n4=(3-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 4 or "Abril":
            print('El mes de  Abril')
            n4=(4-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 5 or "Abril":
            print('El mes de  Mayo')
            n4=(5-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 6 or "Junio":
            print('El mes de Junio')
            n4=(6-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 7 or "Julio":
            print('El mes de Julio')
            n4=(7-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 8 or "Agosto":
            print('El mes de Agosto')
            n4=(8-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 9 or "Septiembre":
            print('El mes de Septiembre')
            n4=(9-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 10 or "Octubre":
            print('El mes de Octubre')
            n4=(10-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 11 or "Noviembre":
            print('El mes de Noviembre')
            n4=(11-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        elif n4 == 12 or "Diciembre":
            print('El mes de Diciembre')
            n4=(12-1)
            consumo=(eg.consumo_energia[n3][n2]["consumos"][n4])
            resultado=consumo*tarifa
            print("El valor gano este mes es de:",resultado)
            break
        else:
            print('ERROR')
            break
