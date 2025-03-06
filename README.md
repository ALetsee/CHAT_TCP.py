# Configuración y Ejecución del Servidor en Python

## Introducción

Este documento explica cómo configurar y ejecutar un servidor en Python utilizando el código proporcionado. El servidor se configurará utilizando la dirección IP obtenida a través del comando `ipconfig` y se ejecutará en el puerto 65535.

## Paso 1: Obtener la Dirección IP

1. Abre una terminal o símbolo del sistema.
2. Ejecuta el comando `ipconfig` para obtener la dirección IP de tu máquina.
3. Busca la `Dirección IPv4`, que es la dirección IP que necesitas.

## Paso 2: Configurar la Dirección IP en el Código de Python

1. Abre el archivo de código de Python en tu editor de texto favorito.
2. Localiza la sección del código donde se define `direccion_host`.
3. Sustituye el valor vacío `''` de `direccion_host` por la Dirección IPv4 obtenida en el paso anterior. Por ejemplo:
    ```python
    direccion_host = '192.168.1.100'  # Sustituye con tu Dirección IPv4
    ```

## Paso 3: Configurar el Puerto

1. En el mismo archivo de código, localiza la línea donde se define `puerto`.
2. Asegúrate de que el valor del puerto sea `65535`. Por ejemplo:
    ```python
    puerto = 65535
    ```

## Paso 4: Ejecutar el Servidor

1. Guarda los cambios en el archivo de código.
2. Abre una terminal o símbolo del sistema en el directorio donde se encuentra el archivo de código.
3. Ejecuta el siguiente comando para iniciar el servidor:
    ```sh
    python Servidor.py
    ```
4. El servidor debería comenzar a ejecutarse y deberías ver un mensaje indicando que el servidor ha iniciado en la dirección y puerto especificados.

## Descripción del Código

### Importación de Módulos

- `socket`: Permite crear y manejar conexiones de red.
- `threading`: Permite manejar múltiples conexiones simultáneamente.
- `time`, `os`, `platform`: Utilizados para funciones auxiliares como limpiar la pantalla y manejar el sistema operativo.

### Variables Globales

- `clientes`: Lista que almacena las conexiones de los clientes.
- `alias_clientes`: Diccionario que asocia las conexiones de los clientes con sus alias.

### Funciones

- `limpiar_pantalla()`: Limpia la pantalla dependiendo del sistema operativo.
- `manejar_cliente(conexion, direccion)`: Maneja la comunicación con un cliente específico, incluyendo la recepción de mensajes y la desconexión.
- `mostrar_usuarios_conectados()`: Muestra la lista de usuarios actualmente conectados.
- `broadcast(mensaje, remitente, is_system=False)`: Envía un mensaje a todos los clientes conectados, excepto al remitente.
- `iniciar_servidor()`: Inicia el servidor, acepta nuevas conexiones y lanza hilos para manejar cada cliente.

# Configuración y Ejecución del Cliente en Python

## Paso 1: Configurar la Dirección IP y el Puerto

1. Al ejecutar el script, se te pedirá que ingreses la dirección IP y el puerto del servidor al que deseas conectarte.
2. Abre una terminal o símbolo del sistema.
3. Ejecuta el comando `python Cliente.py` para iniciar el script.
4. Ingresa la Dirección IP y el puerto del servidor cuando se te solicite.

## Paso 2: Elegir un Alias y un Color

1. Ingresa un alias (nombre de usuario) que se utilizará para identificarte en el chat.
2. Elige un color para tu nombre de usuario en el chat. Los colores disponibles son:
    - Rojo
    - Verde
    - Magenta
    - Azul

## Paso 3: Ejecutar el Cliente

1. Guarda los cambios en el archivo de código.
2. Abre una terminal o símbolo del sistema en el directorio donde se encuentra el archivo de código.
3. Ejecuta el siguiente comando para iniciar el cliente:
    ```sh
    python Cliente.py
    ```

## Descripción del Código

### Importación de Módulos

- `socket`: Permite crear y manejar conexiones de red.
- `threading`: Permite manejar múltiples hilos simultáneamente.
- `colorama`: Utilizado para añadir colores a la salida en la terminal.
- `time`, `sys`, `os`, `platform`: Utilizados para funciones auxiliares como limpiar la pantalla y manejar el sistema operativo.

### Variables Globales

- `cliente`: Objeto socket que representa la conexión del cliente.
- `alias`: Alias (nombre de usuario) del cliente.
- `conectado`: Variable booleana que indica si el cliente está conectado.
- `color_usuario`: Color del nombre de usuario en el chat.
- `host`: Dirección IP del servidor.
- `port`: Puerto del servidor.

### Funciones

- `limpiar_pantalla()`: Limpia la pantalla dependiendo del sistema operativo.
- `mostrar_menu_configuracion()`: Muestra el menú de configuración para ingresar la dirección IP y el puerto del servidor.
- `_menu_colores()`: Muestra el menú de selección de colores para elegir el color del nombre de usuario.
- `recibir_mensajes()`: Hilo que se encarga de recibir y mostrar mensajes del servidor.
- `start_client()`: Función principal que inicia el cliente, se conecta al servidor y lanza el hilo de recepción de mensajes.


