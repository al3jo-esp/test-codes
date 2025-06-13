import numpy as np
import matplotlib.pyplot as plt

def plot_circle_basic(grados, radio=1):
    radianes = np.radians(grados)

    A = (0, 0)
    B = (radio, 0)
    C = (radio * np.cos(radianes), radio * np.sin(radianes))
    D = (C[0], 0)

    linea = np.linspace(0, 2 * np.pi, 500)
    x_circ = radio * np.cos(linea)
    y_circ = radio * np.sin(linea)

    plt.figure(figsize=(7, 7))
    plt.plot(x_circ, y_circ, 'lime', label="Círculo")
    plt.plot([A[0], C[0]], [A[1], C[1]], 'red', label="Radio")
    plt.plot([D[0], C[0]], [D[1], C[1]], 'blue', label=f"sin({grados}°) = {np.sin(radianes):.4f}")
    plt.plot([A[0], D[0]], [A[1], D[1]], 'orange', label=f"cos({grados}°) = {np.cos(radianes):.4f}")

    arco = np.linspace(0, radianes, 100)
    plt.plot(0.5 * np.cos(arco), 0.5 * np.sin(arco), color='purple')
    plt.text(0.6 * np.cos(radianes/2), 0.6 * np.sin(radianes/2), f"{grados}°", ha='center', color='purple', fontsize=10)

    plt.scatter(*A, color="black")
    plt.scatter(*C, color="black")
    plt.scatter(*D, color="black")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-radio - 0.5, radio + 0.5)
    plt.ylim(-radio - 0.5, radio + 0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(loc='upper left')
    plt.title(f"Ángulo: {grados}°")
    plt.show()


def plot_circle_pro(grados, radio=1):
    radianes = np.radians(grados)

    A = (0, 0)
    C = (radio * np.cos(radianes), radio * np.sin(radianes))
    D = (C[0], 0)

    linea = np.linspace(0, 2 * np.pi, 500)
    x_circ = radio * np.cos(linea)
    y_circ = radio * np.sin(linea)

    plt.figure(figsize=(7, 7))
    plt.plot(x_circ, y_circ, 'lime', label="Círculo unitario")
    plt.plot([A[0], C[0]], [A[1], C[1]], 'red', label="Hipotenusa (Radio)")
    plt.plot([D[0], C[0]], [D[1], C[1]], 'blue', label=f"Cateto opuesto (sen({grados}°) = {np.sin(radianes):.4f})")
    plt.plot([A[0], D[0]], [A[1], D[1]], 'orange', label=f"Cateto adyacente (cos({grados}°) = {np.cos(radianes):.4f})")

    arco = np.linspace(0, radianes, 100)
    plt.plot(0.5 * np.cos(arco), 0.5 * np.sin(arco), color='purple')
    plt.text(0.65 * np.cos(radianes/2), 0.65 * np.sin(radianes/2), f"{grados}°", ha='center', va='center', color='purple', fontsize=10)

    plt.scatter(*A, color="black")
    plt.scatter(*C, color="black")
    plt.scatter(*D, color="black")
    plt.text(C[0] + 0.3, C[1], f"({C[0]:.2f}, {C[1]:.2f})", fontsize=9)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-radio - 0.5, radio + 0.5)
    plt.ylim(-radio - 0.5, radio + 0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(loc='upper left')
    plt.title(f"Ángulo: {grados}°")
    plt.show()


# --- Programa principal ---

print("Bienvenido al visualizador de círculo trigonométrico.")
while True:
    modo = input("¿Qué modo quieres usar? (1 = Normal / 2 = PRO): ").strip()
    if modo in ['1', '2']:
        break
    print("Opción inválida. Escribe 1 o 2.")

radio = float(input("¿Qué radio quieres? "))

while True:
    angulo = float(input("¿Qué ángulo quieres calcular? "))
    
    if modo == '1':
        plot_circle_basic(angulo, radio)
    else:
        plot_circle_pro(angulo, radio)

    while True:
        continuar = input("¿Quieres calcular otro ángulo? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            break
        print("Entrada no válida. Escribe 's' o 'n'.")

    if continuar == 'n':
        print("¡Gracias por usar el programa!")
        break
