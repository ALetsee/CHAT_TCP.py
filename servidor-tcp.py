import socket
import threading
import time
import os
import platform


clientes = []

alias_clientes = {}

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def manejar_cliente(conexion, direccion):
    print(f"[JOINED] Un nuevo cliente ha entrado desde {direccion}.")
    conectado = True
    alias = None
    
    try:
        mensaje_inicial = conexion.recv(1024).decode('utf-8')

        if mensaje_inicial.startswith("ALIAS:"):
            alias = mensaje_inicial[6:].strip()

            alias_clientes[conexion] = alias
            clientes.append(conexion)
            

     
            print(f"[NEW USERS] {alias} se ha registrado desde {direccion}")
            

            mostrar_usuarios_conectados()
        else:

            conexion.send("ERROR: Incorrecto".encode('utf-8'))
            conexion.close()
            return
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        conexion.close()
        return
    
    while conectado:
        try:
            mensaje = conexion.recv(1024).decode('utf-8')
            if not mensaje:
                break  
            
            if mensaje.lower() == "exit" or mensaje.lower() == "salir":
                conectado = False
                conexion.send("[SYSTEM] Connection Terminated".encode('utf-8'))
            else:

                broadcast(mensaje, conexion)
             
                print(f"[MENSAJE] {mensaje}")
        except Exception as e:
            print(f"[ERROR] Se produjo un error {alias}: {e}")
            break
    if conexion in clientes:

        if alias:
            broadcast(f"[SYSTEM] {alias} Ha salido", conexion, is_system=True)
        
        clientes.remove(conexion)
        if conexion in alias_clientes:
            del alias_clientes[conexion]

        mostrar_usuarios_conectados()
        
    print(f"[DESCONEXIÓN] {alias} Ha cerrado la conexión {direccion}.")
    conexion.close()

def mostrar_usuarios_conectados():

    usuarios = list(alias_clientes.values())
    if usuarios:
        print(f"[USERS] Total: {len(usuarios)} - {', '.join(usuarios)}")
    else:
        print("[USERS] No hay usuarios conectados")

def broadcast(mensaje, remitente, is_system=False):
    
    mensaje_bytes = mensaje.encode('utf-8')
    
    desconectados = []
    for cliente in clientes:
        if cliente != remitente or is_system:  
            try:
                cliente.send(mensaje_bytes)
            except:
            
                desconectados.append(cliente)
    
    for cliente in desconectados:
        if cliente in clientes:
            clientes.remove(cliente)
            if cliente in alias_clientes:
                del alias_clientes[cliente]

def iniciar_servidor():
    limpiar_pantalla()
    direccion_host = ''  
    puerto = 65535
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        servidor.bind((direccion_host, puerto))
        servidor.listen(10) 
        print(f"[SERVER STARTED] Servidor en {direccion_host if direccion_host else '*'}:{puerto}")
        
        while True:
            conexion, direccion = servidor.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
            hilo.daemon = True
            hilo.start()
            print(f"[CONEXIONES] {len(clientes)}")
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Servidor detenido.")
    except Exception as e:
        print(f"[ERROR] Error al iniciar el servidor: {e}")
    finally:

        for cliente in clientes:
            try:
                cliente.send("[SYSTEM] Servidor cerrando.".encode('utf-8'))
                cliente.close()
            except:
                pass
        servidor.close()

if __name__ == "__main__":
    print("[STARTING] Server starting...")
    iniciar_servidor()