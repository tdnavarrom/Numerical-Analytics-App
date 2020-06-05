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
