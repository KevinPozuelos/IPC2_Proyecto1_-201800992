# IPC2_Proyecto1_-201800992
LABORATORIO INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 Sección D
Sección B+
Proyecto 1 - 201800992


##Proyecto 1
En este proyecto se han implementado estructuras basicas de datos y sus diferentes funcionaes. 

###TDA

```
-Lista doblemente enlazada

-Lista simplemente enlazada

```

###Metodos de TDA'S
```
      ---------------------------------------------------------------------------------------------------
      |  Metodo       |                               Descripción                                       |
      |-------------  | --------------------------------------------------------------------------------|
      | Insert        |  Este metodo sirve para guardar los datos nombre, n y m de la matriz.           |
      |-------------  | --------------------------------------------------------------------------------|
      | Mostrar       |  Muestra los datos guardados en la lista doblementen enlazada.                  |
      |               |  Nombre, fila, columna y Matriz                                                 |
      |-------------  | --------------------------------------------------------------------------------|
      | Reducir       |  Este metodo muestra que filas tienen el mismo patron de 1 y 0 de su atributo   |
      |               |  accessM                                                                        |
      |-------------  | --------------------------------------------------------------------------------|
      | graph         |  Este metodo grafica mediante el parametro de busqueda "nombre" y escribe un    |
      |               |  un archivo .dot para generar una imagen del mismo.                             |
      |-------------  | --------------------------------------------------------------------------------|
      | mostrarnom    |  Metodo que muestra un listado de los nombres de las matrices almacenadas.      |
      |-------------  | --------------------------------------------------------------------------------|
      |Lista simple   |  Metodo para insertar los datos: x, y, dato y accessM.                          |
      |   insert      |                                                                                 |
      |-------------  | --------------------------------------------------------------------------------|
      | Lista simple  |  {T.nodo = Nodo(temporal = getTemporal())                                       |
      | getNodo       |Metodo para comparar nodos mediante su atributo access                           |
      |-------------  | --------------------------------------------------------------------------------|
      | Lista simple  | Metodo para mostrar el contenido de los nodos de la lista simple                |
      | mostrar       |                                                                                 |
      |-------------  | --------------------------------------------------------------------------------|
     

```

### Implementacion en python
####Clase Nodo
Clase que nos permite almacenar nuestras matrices y posteriormente para crear una lista doblemente enlazada.

####Clase Dato
Clase que nos permite almacenar el contenido de nuestras matrices y posterior mente crear una lista simplemente enlazada. 

####Clase Matriz
Clase donde se implementa los metodos de una lista simplemente enlazada. 

####ListaMatriz
Clase que nos permite guardar los datos generales de nuestra matriz y nuestras matrices en una lista doblemente enlazada. 

####Lector
Clase que nos permite leer y guardar los datos de un archivo xml en nuestras listas enlazadas.

####Menu
lase menu para mostrar las funcionabilidades solicitadas.

####Main
Clase que permite la ejecucion de todo el codigo.
