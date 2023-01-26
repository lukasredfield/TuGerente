# Pasos para realizar una reserva de un cuarto del hotel

1. Primeramente para cubrir el flujo normal de operación de reserva se debe registrar/crear un nuevo cliente del hotel. (ES NECESARIO que se anote el "id" del cliente para luego poder utilizarlo al momento de registrar la reserva)
2. Luego ya con el cliente creado se debe elegir el cuarto que se desea reservar. Para ello se debe acceder a la lista de cuartos disponibles en el hotel. (ANOTAR el número de cuarto que se desea elegir para realizar la reserva en el siguiente paso)
3. Y para finalizar, ya con el "id" de mi cliente registrado y el "numero" de cuarto elegido se debe hacer la reserva. Son 6 los campos que debemos rellenar para hacer la reserva. Primero el "cuarto" y allí debemos poner el número de cuarto escogido, en el siguiente campo "cliente" se debe ingresar el "id" de nuestro cliente registrado, luego "fecha de entrada" indicamos desde que fecha reservamos el cuarto y en "fecha salida" en que día termina la reserva. En el campo "metodo de pago" podemos indicar que método de pago que querramos y en ultimo campo "estado" indicamos el estado del pago, en este ultimo campo solo nos va a aceptar entre 3 opciones (Pendiente, Pagado y Eliminado) son los valores que acepta este campo. Luego de rellenar todos los campos de debe envíar la petición y la reserva se abra realizado.

# USO DE POSTMAN 

A continuación se mostrará el camino de los 3 pasos descritos anteriormente con sus respectivos endpoints y ejemplos de su uso:
## Endpoints:

Utilizando Postman se debe ingresar los siguientes endpoints con sus métodos correspondientes (GET,POST):

1. 

- Crear o Registrar "Cliente"  : http://localhost:8000/clientes/  
 - Método: POST
 - En Body / Raw / ejemplo de JSON:
    
    {
    "Nombre": "Axel",
    "Apellido": "Rose",
    "Dni": 4354353455455
    }

- Devolverá el siguiente JSON con el Cliente creado:

    {
    "id": 5,
    "Nombre": "Axel",
    "Apellido": "Rose",
    "Dni": 4354353455455
    }

* (El campo "id" debe ser utilizado al momento de hacer la reservación)


2. 

- Ver Lista de "Cuartos"  : http://localhost:8000/api/Cuartos/    
 - Método: GET
 - Suministrará una lista con todos los cuartos del hotel disponibles y sus características.
 - Ejemplo de un cuarto:
    
    {
        "numero": 3,
        "capacidad_de_personas": 5,
        "cantidad_de_camas": 5,
        "jacuzzi": "No",
        "precio_x_dia": 200,
        "ocupado": "No"
    },

* (El campo "numero" debe ser utilizado al momento de hacer la reservación)



3. 

- Crear "Reservación"  : http://localhost:8000/reservaciones/  
 - Método: POST
 - En Body / Raw / ejemplo de JSON:
    
    {
    "cuarto": 5,
    "cliente": 7,
    "fecha_entrada": "2024-02-02",
    "fecha_salida": "2024-02-10",
    "metodo_de_pago": "Tarjeta",
    "estado": "Pagado"
    }

- Devolverá el siguiente JSON con la Reserva creada:

    {
        "cuarto": 5,
        "cliente": 7,
        "fecha_entrada": "2024-02-02",
        "fecha_salida": "2024-02-10",
        "días_de_estadia": 8,
        "metodo_de_pago": "Tarjeta",
        "monto_pagado": 3200,
        "estado": "Pagado"
    }


4. 

- Ver Lista de "Reservas"  : http://localhost:8000/api/ReservasHotel/    
 - Método: GET
 - Suministrará una lista con todas las reservas del hotel.


5. 

- Ver Lista de "Clientes"  : http://localhost:8000/api/Clientes/   
 - Método: GET
 - Suministrará una lista con todos los clientes del hotel registrados.

# Lista completa de endpoints:

1. Crear Cliente:                                              http://localhost:8000/clientes/
2. Actualizar Cliente (Indicar numero de "id" al final):       http://localhost:8000/clientes/update/1
3. Borrar Cliente (Indicar numero de "id" al final) :          http://localhost:8000/clientes/delete/12 
4. Ver lista de Clientes:                                      http://localhost:8000/api/Clientes/
5. Crear Cuarto:                                               http://localhost:8000/cuartos/
6. Actualizar Cuarto (Indicar "numero" del cuarto al final) :  http://localhost:8000/cuartos/update/1 
7. Borrar Cuarto (Indicar "numero" del cuarto al final) :      http://localhost:8000/cuartos/delete/8 
8. Ver lista de Cuartos:                                       http://localhost:8000/api/Cuartos/8
9. Crear Reserva:                                              http://localhost:8000/api/ReservasHotel/
10. Actualizar Reserva (Indicar numero del cliente al final) :   http://localhost:8000/reservaciones/update/10
11. Borrar Reserva  (Indicar numero del cliente al final) :    http://localhost:8000/reservaciones/delete/8
12. Ver lista de Reservas:                                     http://localhost:8000/api/ReservasHotel/ 


## Instrucciones: Aplicación conteiner de Docker:

1.	Hacer un “PULL” por consola para descargar el contenedor de la aplicación, al siguiente repositorio de DockerHub: 

“docker pull lukasredfield/todolist:1.0”

2.	Luego introducir por consola el comando para correr la aplicación y levantarla en el servidor: 

“docker run -p 8000:8000 lukasredfield/todolist:1.0” 

3.	Introducir en el browser “locashost:8000” para acceder a la aplicación. En la página de inicio hacer login y acceder al administrador con el siguiente usuario y contraseña:

Usuario: admin
Contraseña: 12345

4.	Aquí podemos realizar todas las acciones y las funcionalidades anteriormente descritas, pero ahora corriendo desde el contenedor de Docker.


