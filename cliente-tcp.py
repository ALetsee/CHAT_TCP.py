import socket
import threading
from colorama import Fore, Style, init
import time
import sys
import os
import platform

init(autoreset=True)

cliente = None
alias = None
conectado = False
color_usuario = Fore.WHITE  
host = None
port = None

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

limpiar_pantalla()

def mostrar_menu_configuracion():
    global host, port
    limpiar_pantalla()
    print(f"{Fore.BLUE}{Style.BRIGHT}" + 
      "_________   ___ ___    ________________\n" + 
      "\\_   ___ \\ /   |   \\  /  _  \\\__    ___/\n" + 
      "/    \\  \\/    ~    \\/  /_\\  \\|    |   \n" + 
      "\\     \\___\\    Y    /    |    \\    |   \n" + 
      " \\______  /\\___|_  /\\____|__  /____|   \n" + 
      "        \/       \/         \/          ")

    host = input(f"{Fore.BLUE}{Style.BRIGHT}► Ingresa la IP: {Fore.WHITE}").strip()
    while not host:
        print(f"{Fore.RED}[ERROR] IP inválida.{Style.RESET_ALL}")
        host = input(f"{Fore.BLUE}{Style.BRIGHT}► Ingresa la IP: {Fore.WHITE}").strip()
    limpiar_pantalla()

    while not port:
        try:
            port = int(input(f"{Fore.BLUE}{Style.BRIGHT}► Ingresa el puerto: {Fore.WHITE}"))
            if port <= 0 or port > 65535:
                print(f"{Fore.RED}[ERROR] Puerto inválido.{Style.RESET_ALL}")
                port = None
        except ValueError:
            print(f"{Fore.RED}[ERROR] Debe ser un número.{Style.RESET_ALL}")
    limpiar_pantalla()

def _menu_colores():
    print(f"{Fore.BLUE}╔════════════════════╗")
    print(f"{Fore.BLUE}║         COLORES    ║")
    print(f"{Fore.BLUE}╚════════════════════╝")
    colores = [Fore.RED,Fore.GREEN, Fore.MAGENTA, Fore.BLUE]
    nombres = ["Rojo", "Verde", "Magenta", "Azul"]
    for i, nombre in enumerate(nombres, start=1):
        print(f"{colores[i-1]}{i}. {nombre}{Style.RESET_ALL}")

    while True:
        try:
            opcion = int(input(f"{Fore.WHITE}> Elige un color (1-6): {Style.RESET_ALL}"))
            if 1 <= opcion <= 6:
                limpiar_pantalla()
                return colores[opcion-1]
            else:
                print(f"{Fore.RED}[ERROR]{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}[ERROR]  Introduce un número.{Style.RESET_ALL}")

def recibir_mensajes():
    global conectado
    while conectado:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if not mensaje:
                break

            sys.stdout.write(f"\r{mensaje}\n")
            sys.stdout.flush()
            sys.stdout.write(f"{color_usuario}{alias} > {Style.RESET_ALL}")
            sys.stdout.flush()
        except Exception as e:
            if conectado:
                print(f"\r{Fore.RED}[ERROR] Conexión perdida: {e}{Style.RESET_ALL}")
            break
    limpiar_pantalla()
    conectado = False

def start_client():
    global cliente, alias, conectado, color_usuario, host, port
    mostrar_menu_configuracion()
    alias = input(f"{Fore.BLUE}Usuario > {Style.RESET_ALL}").strip()
    while not alias:
        print(f"{Fore.RED}[ERROR] El nombre de usuario no puede estar vacío.{Style.RESET_ALL}")
        alias = input(f"{Fore.BLUE}Usuario >{Style.RESET_ALL}").strip()
    limpiar_pantalla()

    color_usuario = _menu_colores()
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((host, port))
        cliente.send(f"ALIAS: {alias}".encode('utf-8'))
        conectado = True
        hilo_recepcion = threading.Thread(target=recibir_mensajes)
        hilo_recepcion.daemon = True
        hilo_recepcion.start()

        print(f"{Fore.BLUE}╔══════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.BLUE}║                  CHAT                ║{Style.RESET_ALL}")
        print(f"{Fore.BLUE}╚══════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[CONECTADO] Server: {Fore.WHITE}{host}:{port}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[CONECTADO] Welcome, {color_usuario}{alias}{Style.RESET_ALL}!")
        print(f"{Fore.BLUE}[INFO] Escribe 'exit' o 'salir' para salir.{Style.RESET_ALL}")
        
        while conectado:
            mensaje = input(f"{color_usuario}{alias} > {Style.RESET_ALL}")
            if mensaje.lower() in ["exit", "salir"]:
                cliente.send("exit".encode('utf-8'))
                conectado = False
                break
            cliente.send(f"{alias}: {mensaje}".encode('utf-8'))
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {e}{Style.RESET_ALL}")
    finally:
        cliente.close()
        print(f"{Fore.RED}[OFFLINE]{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.BLUE}[INICIANDO] Cliente{Style.RESET_ALL}")
    try:
        start_client()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[CANCELED] Programa terminado.{Style.RESET_ALL}")
        sys.exit(0)
