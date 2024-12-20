import numpy as np
import matplotlib.pyplot as plt

# Visualizar ángulos en un círculo

def plot_unit_circle_with_angle(grados, radio=1):
# Convertir el ángulo a radianes
    radianes = np.radians(grados)

# Coordenadas de los puntos
    A = (0, 0)  # Origen
    B = (radio, 0)  # Punto en el eje x (radio)
    C = (radio * np.cos(radianes), radio * np.sin(radianes))  # Punto en el círculo
    D = (radio * np.cos(radianes), 0)  # Proyección sobre el eje x

# Crear el círculo
    linea = np.linspace(0, 2 * np.pi, 500)
    x_circ = radio * np.cos(linea)
    y_circ = radio * np.sin(linea)

# Graficar
    plt.figure(figsize=(6.5, 6.5))
    plt.plot(x_circ, y_circ, 'lime', label="Círculo")  # Círculo
    plt.plot([A[0], C[0]], [A[1], C[1]], 'red', label=f"sin({grados}°) = {np.sin(radianes):.4f}")  # Línea hipotenusa
    plt.plot([C[0], D[0]], [C[1], D[1]], 'blue', label=f"cos({grados}°) = {np.cos(radianes):.4f}")  # Línea seno
    plt.plot([D[0], B[1]], [D[1], B[1]], 'red')  # Línea coseno

# Añadir puntos en la leyenda
    plt.scatter(*A, color="black", label="A (0, 0)")
    plt.scatter(*C, color="black", label=f"C ({C[0]:.2f}, {C[1]:.2f})")
    plt.scatter(*D, color="black", label=f"D ({D[0]:.2f}, 0)")

# Configurar la gráfica
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-radio - 0.2, radio + 0.5)
    plt.ylim(-radio - 0.2, radio + 0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(loc='upper left', bbox_to_anchor=(0.645, 1), borderaxespad=0.)
    plt.title("Calculador de razones trigonométricas")
    plt.show()

# Solicitar datos al usuario
radio = float(input("¿Qué radio quieres? "))
angulo = int(input("¿Qué ángulo quieres calcular? "))
plot_unit_circle_with_angle(angulo, radio)