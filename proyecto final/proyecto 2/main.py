import consumos.funciones as fn

consumo_energia=fn.obtenerdatos()
informacion=fn.obtenerinfo()

op = -1
while op !=0:
    print('1. Mostrar consumo total por Planta')
    print('2 Mostrar Total de megavatios')
    print('3 Mostrar total por Region')
    print()
   
    op = int(input('Ingrese opcion: '))

    if op == 1:
        p1=fn.obtenerconsumo(consumo_energia,informacion)
        print(p1)
        print()
                       
    if op == 2:
        p2=fn.obtenerdic(consumo_energia,informacion)
        print(p2)
        print()
        
    if op == 3:
        p3=fn.obtenertTarifa(consumo_energia,informacion)
        print(p3)
        print()
    
    if op == 4:
        p4=fn.solicitud_mes(n1,n2,n3,n4)
        print(p4)
        print()