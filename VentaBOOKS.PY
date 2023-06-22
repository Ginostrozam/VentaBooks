import funciones as fu
while True:
    try:
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
            cod=int(input("Ingrese codigo: "))
            tit=input("Ingrese Titulo del Libro: ").capitalize()
            autor=input("Ingrese Autor del Libro: ").capitalize()
            precio=int(input("Ingrese Precio del Libro:"))
            fu.agregar(cod,tit,autor,precio)
        elif opcion==2:
            fu.verd("///BUSCAR///")
            cod=int(input("Ingrese codigo: "))
            fu.listar(cod)
        elif opcion==3:
            fu.verd("///CERTIFICADOS///")
            fu.az("1) Criticas")
            fu.az("2) Detalles")
            cert=int(input("Seleccione : "))
            if cert==1:
                fu.verd("Certificado de Criticas")
                cod=int(input("Ingrese codigo: "))
                fu.certificadoop(cod)
            elif cert==2:
                fu.verd("Certificado detalle Ventas")
                cod=int(input("Ingrese codigo: "))
                fu.detalle(cod)
            else:
                fu.roj("Opción no valida")
        else:
            fu.roj("Opción no valida.")
    except:
        fu.roj("Falla en el sistema,intente nuevamente.")
