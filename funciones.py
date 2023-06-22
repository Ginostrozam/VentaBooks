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
#Guardar
#Buscar
#CertificadoCriticas
#CertificadoDetalle