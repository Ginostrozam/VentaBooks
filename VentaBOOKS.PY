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
        break
    elif opcion==1:
        fu.verd("///GUARDAR///")
    elif opcion==2:
        fu.verd("///BUSCAR///")
    elif opcion==3:
        fu.verd("///CERTIFICADOS///")
    else:
        fu.roj("Opción no valida.")
