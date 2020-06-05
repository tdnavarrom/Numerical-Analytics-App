from gi.repository import Gtk, Gdk
import gi

gi.require_version('Gtk', '3.0')


class Help():
    def non_linear_equation_help(self, method):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, method)
        if method == "Incremental":
            text = "El objetivo del método es encontrar un intervalo que contenga al menos una raíz, y se basa en el teorema del valor intermedio.\n\nPara aplicar este método la función f(x) debe ser real y continúa, además se debe tener cuidado al elegir el incremento (Delta) al que se va evaluar la función, si el incremento es muy pequeño se corre el riesgo de volver el proceso muy dispendioso, y si es muy grande se corre el riesgo de no detectar la raíz.\n\n"
            text += "El procedimiento a seguir para la aplicación del método es el siguiente:\n\n"
            text += "1. Se determina un dominio de la función de interés.\n"
            text += "2. Se evalúa la función tomando un pequeño incremento y un valor inicial (Xo) seleccionado del dominio  arbitrariamente.\n"
            text += "3. Analizar el signo del producto de la evolución de un valor actual con el anterior y deducir con el si existe o no la raíz.  Si el signo del producto es negativo, se puede dar como confirmado un intervalo que contiene la raíz, de otro modo no existe el intervalo.\n"
        elif method == "Bisection":
            text = "El objetivo del método es buscar la raíz de una función, tomando un intervalo inicial y reduciendo gradualmente a la mitad este, hasta hallar una aproximación o la raíz que satisface la función.\n\n"
            text += "El procedimiento a seguir para la aplicación del método es el siguiente:\n\n"
            text += "1. Se elige un intervalo inicial para función f(x)\n"
            text += "2. Luego se busca localizar la raíz con mayor exactitud dentro del intervalo dividiendo a la mitad y observando si se conservan las condiciones iniciales.\n"
            text += "3. Se compara el Xmed con cada uno de los límites del intervalo y se observa que producto cambia de signo y se asigna un nuevo intervalo.\n"
            text += "4. Se vuelve a repetir el proceso, y se va poniendo pequeño el intervalo hasta llegar a una aproximación de la raíz o la raíz exacta."
        elif method == "False Rule":
            text = "EL objetivo de este método es encontrar la intersección de una recta conformada por los puntos a y b con el eje x, y obtener nuevos intervalos mas pequeños, lo la cual  permite una  aproximación a una raíz.\n\n"
            text += "Este método conserva todas las características y condiciones que posee el método de bisección, excepto por la forma de calcular el punto  intermedio del intervalo\n\n"
            text += "El procedimiento a seguir para la aplicación del método es el siguiente:\n\n"
            text += "1. Si se tiene dos puntos (a, f(a)) y(b, f(b)) y se traza la recta que une a estos dos puntos, se puede observar que un punto esta por debajo del eje x y otro por encima de este, y un punto intermedio (Xm,0), con este punto intermedio se puede comparar los limites y obtener un nuevo intervalo\n"
            text += "2. Si  f(A) y f(B)<0, entonces la raíz se encuentra al lado izquierdo del intervalo.\n"
            text += "3. Si  f(A) y f(B)>0, entonces la raíz se encuentra al lado derecho del intervalo.\n"
            text += "4. Para hallar la intersección de la recta con el eje X usamos la siguiente fórmula: Xm= a - ((f(a)*(b - a))/(f(b) - f(a)))\n\n"
            text += "El método de Regla Falsa converge más rápidamente que el de bisección porque al permanecer uno de sus valores iniciales fijo el número de cálculos se reduce mientras que el otro valor inicial converge hacia la raíz."
        elif method == "Fixed Point":
            text = "El objetivo de este método es buscar una raíz de una función a partir de un valor inicial, una tolerancia y un número de iteraciones, para este caso no es necesario tener un intervalo.\n\n"
            text += "A partir de una ecuación F(X)=0 se genera una ecuación X=g(X), a la cual se le busca una solución, y se debe tener en cuenta lo siguiente"
            text += "1. Se busca un valor de X que al reemplazarlo en g, el resultado sea X.\n"
            text += "2. Se debe elegir una aproximación inicial Xo\n"
            text += "3. Se calcula X1=g(Xo)\n"
            text += "4. Y se repite el paso anterior hasta llegar a una aproximación."
        elif method == "Newton":
            text = "El objetivo de este método es buscar una raíz de una función a partir de un valor inicial, una tolerancia y un número de iteraciones, para este caso no es necesario tener un intervalo.\n\nEl método de newton por su rapidez y efectividad, es uno de los métodos más utilizados; este método es una variable del método de punto fijo, por lo cual se debe calcular una función g , esta función g se puede calcular de la forma:\ng(X) = X – (f(X)/f ‘ (x))\n\nUna vez definida la función g, se debe realizar los siguientes pasos, como en el método de punto fijo.\n\n"
            text += "1. Se debe elegir una aproximación inicial Xo\n"
            text += "2. Se calcula X1=g(Xo)\n"
            text += "3. Se calcula X2=g(X1)\n"
            text += "4. Se calcula Xn=g(Xn-1)\n"
            text += "5. Se repite el paso anterior hasta llegar a una aproximación de la raiz."
        elif method == "Secant":
            text = "El objetivo de este método es buscar una raíz de una función a partir de dos valores iniciales, una tolerancia y un número de iteraciones, para este caso no es necesario tener un intervalo.\n\nEl método de la secante se define como una variante del método de Newton. A partir de la ecuación iterativa que define el método de Newton, se sustituye la derivada por una expresión que la aproxima:\n\nX2 = X1 – ((f(X1)*(X1-Xo))/(f(X1)-f(Xo))\n\n"
            text += "1. Se debe elegir dos aproximaciones iniciales X1 y X0\n"
            text += "2. Se calcula X2= Expresión  ---------- Xn = Expresión (n-1)\n"
            text += "3. Y se repite el paso anterior hasta llegar a una aproximación.\n"
        elif method == "Multiple Roots":
            text = "Buscar una raíz de una función a partir de dos valores iniciales, una tolerancia y un número de iteraciones, para este caso no es necesario tener un intervalo.\n\nUna de las condiciones para garantizar la convergencia del método de Newton es que f´(Xv) tiene que ser diferente de cero . Si al ejecutar el método de Newton se observa que f´(xn)  se aproxima a cero, la rapidez del método disminuye y hay una posible raíz múltiple.\n\nEl método de raíz múltiple también es conocido como el método de Newton mejorado, y básicamente su estructura es muy similar excepto de que se debe hallar la segunda derivada y se debe tomar en cuenta  la siguiente expresión:\n\nXn+1 = Xn – ((f(Xn)*f´(Xn))/((f`(Xn)^2 - (f(Xn)*f´´(Xn)))\n\n"
            text += "Una vez definida la expresión anterior, se procede de una forma similar al método de Newton\n"
            text += "1. Se debe elegir una aproximación iniciales X0\n"
            text += "2. Se calcula X1= Expresión  ---------- Xn = Expresión (n-1)\n"
            text += "3. Y se repite el paso anterior hasta llegar a una aproximación.\n"
        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()

    def linear_equations_help(self, method):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, method)
        if method == "Simple Gaussian":
            text = "El metodo de eliminacion Gausseana se aplica para resolver sistemas lineas de la forma Ax = b, Donde A es una matriz con los coeficientes de las ecuaciones organizadas en forma descendiente y b es un vector con las Ys de las ecuaciones.\n"
            text += "Se comienza generando una Matriz Aumentada (Ab) e iterativamente se calculan los coeficientes de tal manera que se haga la parte inferior de la matriz 0.\n"
            text += "Luego de tener la matriz resuelta se le aplica sustitución regresiva para conocer los valores que satisfacen el sistema de ecuaciones."
        elif method == "Parcial Pivot":
            text = "Las estrategias de pivoteo son normalmente utilizadas conjuntamente con el metodo de eliminacion Gaussiana, sirven para reducir los efectos del error de redondeo.\n\n"
            text += "- Para el pivoteo parcial, se pretende que el elemento de la diagonal sea el máximo en valor absoluto y se elige con los elementos de la misma columna a partir del akk, luego se realiza el intercambio entre la fila donde esta el mayor elemento y la fila k.\n\n"
        elif method == "Total Pivot":
            text = "Las estrategias de pivoteo son normalmente utilizadas conjuntamente con el metodo de eliminacion Gaussiana, sirven para reducir los efectos del error de redondeo.\n\n"
            text += "- Para el pivoteo total, se pretende buscar en la k-ésima etapa el el elemento mayor en valor absoluto entre todos los elementos, una vez se disponga del elemento mayor, se realizan cambios cambios entre filas y columnas con el objetivo de ubicar el mayor en la diagonal sobre la fila que actualmente se esta pivotando."
        elif method == "Crout":
            text = "Hace parte de los métodos de LU para la factorización de matrices, donde una matriz A se factoriza en L(Triangular superior) y U(Triangular inferior).\n"
            text += "Dado Ax= b, se tendría LUx = b  y si Ux = z, entonces Lz = b. En este método especifico, La diagonal de L y U son iguales U[i][i] = 1.\n"
            text += "Luego de que se tiene la matriz factorizada, se hace sustitución progresiva con la matriz L y los resultados b para hallar los valores de z, luego se utiliza sustitución regresiva para hallar los valores de x, que serian la solución del sistema.\n"
        elif method == "Doolittle":
            text = "Hace parte de los métodos de LU para la factorización de matrices, donde una matriz A se factoriza en L(Triangular superior) y U(Triangular inferior).\n"
            text += "Dado Ax= b, se tendría LUx = b  y si Ux = z, entonces Lz = b. En este método especifico, La diagonal de L y U son iguales L[i][i] = 1.\n"
            text += "Luego de que se tiene la matriz factorizada, se hace sustitución progresiva con la matriz L y los resultados b para hallar los valores de z, luego se utiliza sustitución regresiva para hallar los valores de x, que serian la solución del sistema."
        elif method == "Cholesky":
            text = "Hace parte de los métodos de LU para la factorización de matrices, donde una matriz A se factoriza en L(Triangular superior) y U(Triangular inferior).\n"
            text += "Dado Ax= b, se tendría LUx = b  y si Ux = z, entonces Lz = b. En este método especifico, La diagonal de L y U son iguales L[i][i] = U[i][i].\n"
            text += "Luego de que se tiene la matriz factorizada, se hace sustitución progresiva con la matriz L y los resultados b para hallar los valores de z, luego se utiliza sustitución regresiva para hallar los valores de x, que serian la solución del sistema.\n"
        elif method == "Jacobi":
            text = "Jacobi es un método iterativo para determinar la solución de ecuaciones. Se basa en generar aproximaciones al resultado en base a una aproximación inicial.\n"
            text += "El método primero trata de convertir la matriz dada en una matriz diagonalmente dominante mediante permutaciones de filas y columnas. Posteriormente, se toma cada ecuación y se pone la variable de la diagonal en términos de las otras variables, luego de esto se haya la primera aproximación asignando valores iniciales a las variables usando las ecuaciones generadas anteriormente, los valores asignados se obtienen mediante los cálculos realizados en el mismo ciclo. Se repite este proceso hasta que el valor de la dispersión sea menor que el de la tolerancia, o hasta que se superen el número de iteraciones.\n"
        elif method == "Gauss-Seidel":
            text = "Gauss-Seidel es un método iterativo para determinar la solución de ecuaciones. Se basa en generar aproximaciones al resultado en base a una aproximación inicial.\n"
            text += "El método primero trata de convertir la matriz dada en una matriz diagonalmente dominante mediante permutaciones de filas y columnas. Posteriormente, se toma cada ecuación y se pone la variable de la diagonal en términos de las otras variables, luego de esto se haya la primera aproximación asignando valores iniciales a las variables usando las ecuaciones generadas anteriormente, los valores asignados se obtienen mediante los cálculos realizados en el mismo ciclo. Se repite este proceso hasta que el valor de la dispersión sea menor que el de la tolerancia, o hasta que se superen el número de iteraciones.\n"

        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()

    def interpolacion_help(self, method):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, method)
        if method == "Newton":
            text = "El metodo de interpolacion de Newton, toma como parámetros un conjunto de puntos y un valor a evaluar y usando una aproximación de las series de Taylor, calcula el polinomio correspondiente y evalúa el valor.\n\n"
            text += "p(x) = b0 + b1(x-x0) + b2(x-x0)(x-x1) + b3(x-x0)(x-x1)(x-x2)\n\n"
            text += "Donde los bi son la diagonal de la matriz aux y se calculan teniendo en cuenta las filas anteriores. Así\n"
            text += "b0 = f[x0]\nb1 = f[x1, x0]\nb2 = f[x2, x1, x0]\nbn = f[xn,...,x0]"
        elif method == "Lagrange":
            text = "El objetivo del método es encontrar un polinomio interpolante que represente una función o un problema sin definición exacta, que pase por un conjunto de puntos dados."
            text += "El polinomio interpolante de Lagrange se presenta de la siguiente manera:\n\n"
            text += "1. Se consideran n los puntos x dados de la función, con su respectivo valor de y; dados estos puntos existe un único polinomio de grado a lo sumo de n-1 que pase por ellos. \n"
            text += "2. Para poder definir el polinomio se hallan los valores de cada Li(x) con i desde 1 hasta n.\n"
            text += "3. Una vez calculados los valores de L, podemos confirmar el polinomio y posteriormente, algunos cálculos adicionales.\n"
            text += "4. Los valores de L se pueden calcular de la siguiente estructura, adicionalmente se puede observar la estructura del polinomio de Lagrange."
        elif method == "Neville":
            text = "Dada una función definida para los puntos X0,..., Xn y donde los puntos no están repetidos, el polinomio interpolante es de grado n y es único. Sea pi,j un polinomio de grado j − i que pasa por los puntos (xk, yk) para k = i, i + 1, …, j. El pi,j cumple con la relación de recurrencia\n"
            text += "pi,i(x) = yi\n"
            text += "pi,j(x) = ((xj-x)pi,j-1(x)+(x-xi)pi+1,j(x))/(xj-xi)"
        elif method == "Spline":
            text = "Spline Help"
        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()
