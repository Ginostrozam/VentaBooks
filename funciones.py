import numpy
from colorama import Style,Back,Fore
import os
import msvcrt
import random

###############################################
#CREAR ARREGLO
libros=numpy.empty([10,4],object)

################################################
#Funciones de diseño
def verd(texto:str): #El :str es para obligar a la funcion que sea texto(opcional)
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")
def amar(texto):
    print(f"{Fore.LIGHTBLUE_EX}{Back.LIGHTYELLOW_EX}{texto}{Fore.RESET}{Back.RESET}")
def roj(texto):
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")
def az(texto):
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")
def lp():
    amar("<<<PRESIONE UNA TECLA PARA CONTINUAR>>>")
    msvcrt.getch()
    os.system('cls')
################################################
#Funciones Arreglo
#Validar Codigo
def validarcod(cod):
    for i in range(10):
        if libros[i,0]==cod:
            return i
    return -1
#Guardar
def agregar(cod,tit,autor,precio):
    if None in libros:
        if validarcod(cod)<0:
            if len(tit)>=4:
                if precio>=0:
                    for i in range(10):
                        if libros[i,0]==None:
                            libros[i,0]=cod
                            libros[i,1]=tit
                            libros[i,2]=autor
                            libros[i,3]=precio
                            verd(f"El Libro titulado como {tit} Ha sido registrado con exito.")
                            break
                else:
                    roj("El Precio no debe ser menor a 0")
            else:
                roj("El titulo debe tener al menos 4 caracteres")
        else:
            roj("El codigo se encuentra repetido")
    else:
        roj("No hay Espacio Disponible")
#Buscar
def listar(cod):
    busq=validarcod(cod)
    if busq>=0:
        verd(f"Libro encontrado    CODIGO: {libros[busq,0]}        TITULO: {libros[busq,1]}      AUTOR: {libros[busq,2]}       PRECIO: ${libros[busq,3]}")
    else:
        roj("Codigo no registrado")
#CertificadoCriticas
criticas=[]
criticas.append("Libro muy Bueno")
criticas.append("Lo volveria a leer!")
criticas.append("Estoy muy contento/a con esta compra")
criticas.append("Ni bueno Ni malo")
criticas.append("Libro regular")
criticas.append("No es de mi gusto")
criticas.append("No me gusto para nada")
criticas.append("No lo volveria a comprar")
criticas.append("Lo recomendaria en lo absoluto")
criticas.append("No lo Recomiendo para nada")
criticas.append("Horrible!")

def certificadoop(cod):
    busq=validarcod(cod)
    if busq>=0:
        verd(f"""
             ---------------------------------------
             CERTIFICADO:
             ---------------------------------------
             CODIGO: {libros[busq,0]}       TITULO: {libros[busq,1]}  
             ----------------------------------------
             Criticas 1:{criticas[random.randint(0,11)]}
             Criticas 2:{criticas[random.randint(0,11)]}
             Criticas 3:{criticas[random.randint(0,11)]}""")
    else:
        roj("Codigo no encontrado")
#CertificadoDetalle
def detalle(cod):
    cantlibros=random.randint(0,70)
    busq=validarcod(cod)
    if busq>=0:
        verd(f"""
             -----------------------------------------
                           DETALLE
             -----------------------------------------
             CODIGO: {libros[busq,0]}      TITULO: {libros[busq,1]}  
             ----------------------------------------
             Precio:      {libros[busq,3]} 
             Ventas:      {cantlibros} 
             ----------------------------------------
             Total:       {cantlibros*libros[busq,3]}
             ----------------------------------------""")
    else:
        roj("Codigo no encontrado")