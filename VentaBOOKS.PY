import funciones as fu
while True:
    fu.lp()
    fu.verd("SISTEMA VENTABOOKS")
    fu.az("***********************")
    print("""
    1) Guardar
    2) Buscar
    3) Certificados
    0) Salir""")
    opcion=int(input("Seleccione : "))

    #Validamos la opcion
    if opcion==0:
        fu.amar("Adios!")
        break
    elif opcion==1:
        fu.verd("///GUARDAR///")
    elif opcion==2:
        fu.verd("///BUSCAR///")
    elif opcion==3:
        fu.verd("///CERTIFICADOS///")
        fu.az("1) Criticas")
        fu.az("2) Detalles")
        cert=int(input("Seleccione : "))
        if cert==1:
            fu.verd("Certificado de Criticas")
        elif cert==2:
            fu.verd("Certificado detalle Ventas")
        else:
            fu.roj("Opción no valida")
    else:
        fu.roj("Opción no valida.")
