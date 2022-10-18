# Teoría cuántica básica Juan Pablo Camargo Teheran

## **¿Como usar la libreria?**

en **main.py**:

>```python
> opcion = 0  #opcion 0: El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
> opcion = 1  #opcion 1: El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
> opcion = 2  #opcion 2: Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
> opcion = 3  #opcion 3: Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
> opcion = 4  #opcion 4: El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
> ```

Dependiendo la opción elegida deberá responder a las preguntas que el programa le haga **por consola**

(la opcion debe ser cambiada dentro del programa)

## **¿Como Funciona?**

*para cualquier opción elegida el programa siempre va a pedir*

* "numero de Filas y Columnas del Sistemas"                

* Todos los ejercicios pediran duos de nuemros que reprensentaran un valor real y un valor imaginario para formar un numero complejo deseado
  
* solo recibe como entrada numeros reales


**la documentación de cada funcion se encuentra en formato DocString en el codigo**

este proyecto se realiza con fines educativos para la clase de Ciencia Naturales y Tecnologia en la [Escuela Colombiana de Ingenieria Julio Garavito](https://www.escuelaing.edu.co/es/)
    