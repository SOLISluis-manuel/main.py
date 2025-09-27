# Método de Newton-Raphson en Python
# Autor: [Tu nombre]
# Descripción: Implementación del método de Newton-Raphson para encontrar raíces de funciones.
# Se considera el criterio de convergencia y se hacen las iteraciones hasta la tolerancia deseada.

import math

# ==============================
# Definición de la función f(x)
# ==============================
def funcion_original(x):
    """Función f(x) = e^x - 2"""
    return math.exp(x) - 2

def primera_derivada(x):
    """Primera derivada f'(x) = e^x"""
    return math.exp(x)

def segunda_derivada(x):
    """Segunda derivada f''(x) = e^x"""
    return math.exp(x)

# =======================================
# Método de Newton-Raphson Generalizado
# =======================================
def newton_raphson(f, f1, f2, x0, tolerancia, max_iter):
    """
    Implementa el método de Newton-Raphson.
    Parámetros:
        f  : función original
        f1 : primera derivada
        f2 : segunda derivada
        x0 : valor inicial
        tolerancia : error máximo permitido (%)
        max_iter   : número máximo de iteraciones
    Retorna:
        La raíz aproximada y el número de iteraciones realizadas
    """
    for i in range(max_iter):
        # Verificación del criterio de convergencia
        criterio = abs((f(x0) * f2(x0)) / (f1(x0)**2))
        if criterio >= 1:
            print("Advertencia: El criterio de convergencia no se cumple en x =", x0)
            break

        # Fórmula del método de Newton-Raphson
        xn = x0 - (f(x0) / f1(x0))

        # Cálculo del error relativo porcentual
        er = abs((xn - x0) / xn) * 100

        # Mostrar avance en cada iteración
        print(f"Iteración {i+1}: xn = {xn}, error = {er:.6f}%")

        # Verificación de tolerancia
        if er < tolerancia:
            return xn, i+1

        # Actualizar x0
        x0 = xn

    # Si no converge en max_iter, devolver último valor
    return x0, max_iter

# ======================
# Función principal main
# ======================
def main():
    print("Método de Newton-Raphson para f(x) = e^x - 2\n")

    # Solicitar valores al usuario
    x0 = float(input("Ingrese el valor inicial de x0: "))
    tolerancia = float(input("Ingrese la tolerancia (%): "))
    max_iter = int(input("Ingrese el número máximo de iteraciones: "))

    # Llamar al método de Newton-Raphson
    raiz, iteraciones = newton_raphson(funcion_original, primera_derivada, segunda_derivada, x0, tolerancia, max_iter)

    print(f"\nLa raíz aproximada es {raiz} y se obtuvo en {iteraciones} iteraciones.")

# ======================
# Ejecución del programa
# ======================
if __name__ == "__main__":
    main()
