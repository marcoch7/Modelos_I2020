# Tarea 3
#### Por: Marco Chacon Soto B6168
## Dependencias

Se requiere tener instalado un compilador para python o python3

## Compilar y ejecutar

Para correr el programa basta con escribir en consola:

```c
python3 tarea3.py
```

## Descripcion del programa

En este codigo se obtienen datos como curvas de mejor ajuste, funciones de densidad y momentos para variables aleatorias multiples a partir de los datos que se encuentran en el documento "xyp.csv".


## Informacion adicional

### Problema 1

Las funciones de densidad marginal de X y Y, asi como la curva que mejor se ajusta a estas se encuentran en las figuras BestfitX.png y BestfitY.png. Se obtienen los parametros mu y sigma para cada una, donde para X:
1. param[0] = Mu, param[1] = Sigma
Para Y:
2. paramy[0] = Mu, paramy[1] = Sigma

### Problema 2

Dado que se asume independencia de X y Y, Se multiplican ambas funciones de densidad marginal para obtener la funcion de densidad conjunta. Entonces, fx,y es fx*fy. Esta ecuacion se encuentra en la linea 102, con el tag "f_dens".
### Problema 3

El significado de cada uno de los momentos es el siguiente:

1. Correlacion: es el grado en el cual dos o mas cantidades estan linealmente asociadas, se dice que dos variables se encuentran correlacionadas cuando los valores de una variable se modifican respecto a los valores de otra. Esta correlacion no implica, por si misma, ninguna relacion de causalidad.

2. Covarianza: este valor indica el grado de variacion conjunta de dos variables alreatorias respecto a sus medias. Esta caracteristica permite saber como se comporta una variable en funcion de lo que hace otra.

3. Coeficiente de correlacion de Pearson: es una medida de dependencia lineal entre dos variables aleatorias cuantitativas. Se diferencia de la covarianza ya que este coeficiente es independiente de la escala de medida de las variables.

### Problema 4
Las graficas de las funciones de densidad marginal se obtienen a partir de las curvas de mejor ajuste obtenidas en el problema 1. Estas figuras son Xmarginal.png y Ymarginal.png.<br />
La grafica para la funcion de densidad conjunta se obtiene a partir de la ecuacion del problema 3 y la figura es threed.png

### Comentarios

-El codigo se encuentra dentro de la carpeta src.<br />
-Los resultados del problema 3 se imprimen en la pantalla al correr el codigo.<br />
-Las graficas del problema 1 se encuentran en la carpeta images.<br />
-Para graficar la curva de mejor ajuste para la funcion de densidad marginal de X, se utilizo la funcion "gau" de la linea 58 del codigo, cuyo Mu = 3.84983738 ya que este presenta una mejor aproximacion de la curva.



