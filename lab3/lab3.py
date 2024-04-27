import matplotlib.pyplot as plt
import numpy as np


def task1():
    # Визначення діапазонів x та y
    x = np.linspace(-np.pi / 2, np.pi / 2, 100)
    y = np.linspace(-np.pi / 2, np.pi / 2, 100)

    # Створення сітки для побудови скалярного поля
    X, Y = np.meshgrid(x, y)

    # Обчислення значень скалярного поля u(x, y)
    U = np.arcsin((2 * Y) / ((X ** 2) + (Y ** 2)))

    # Побудова контурів скалярного поля
    plt.figure(figsize=(8, 6))
    contour = plt.contourf(X, Y, U, cmap='viridis')
    plt.colorbar(contour, label='u(x, y) = arcsin((2y) / (x^2 + y^2))')
    plt.title("Візуалізація скалярного поля")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    # Визначення часткових похідних для градієнта
    du_dx = -((4 * X * Y) / (((X ** 2) + (Y ** 2)) ** 2))
    du_dy = (2 * (X ** 2 - Y ** 2) / (((X ** 2) + (Y ** 2)) ** 2))

    # Побудова плоского векторного поля для градієнта
    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, du_dx, du_dy, color='black')
    plt.title("Візуалізація градієнта скалярного поля як векторного поля")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    plt.show()


def task2():
    # Визначення діапазону значень x та y
    x = np.linspace(-11, 11, 20)  # Вибір кількості точок у діапазоні
    y = np.linspace(-11, 11, 20)

    # Створення сітки для побудови векторного поля
    X, Y = np.meshgrid(x, y)

    # Визначення компонентів векторного поля F = (2xy - y; x^2 + x)
    Fx = 2 * X * Y - Y
    Fy = X ** 2 + X

    # Побудова векторного поля
    plt.figure(figsize=(10, 6))
    plt.quiver(X, Y, Fx, Fy, color='b', label='F = (2xy - y; x^2 + x)')
    plt.title("Векторне поле за допомогою векторів")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Побудова ліній току для векторного поля
    plt.figure(figsize=(10, 6))
    plt.streamplot(X, Y, Fx, Fy, color='r', density=1.0)  # Додатковий параметр density контролює щільність ліній
    plt.title("Векторне поле за допомогою ліній току")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    plt.show()


def task3():
    # Визначення діапазонів значень x, y та z
    x = np.linspace(-11, 11, 20)
    y = np.linspace(-11, 11, 20)
    z = np.linspace(-11, 11, 20)

    # Створення 3D-сітки для побудови векторного поля
    X, Y, Z = np.meshgrid(x, y, z)

    # Визначення компонентів векторного поля F = ((((2x)/(y))+1); ((x^2)/(y^2)); -6 * z^2)
    Fx = ((2 * X) / Y) + 1
    Fy = (X ** 2) / (Y ** 2)
    Fz = -6 * (Z ** 2)

    # Побудова векторного поля
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.quiver(X, Y, Z, Fx, Fy, Fz, length=1, normalize=True,
              color='b')

    # Налаштування осей та заголовка
    ax.set_title("Тривимірна візуалізація векторного поля")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.show()


def task4():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    # Значення epsilon для уникнення ділення на нуль
    epsilon = 1e-6

    # Функція для створення 3D сітки та тензорного поля
    def create_3d_mesh():
        x = np.linspace(-5, 5, 5)
        y = np.linspace(-5, 5, 5)
        z = np.linspace(-5, 5, 5)
        X, Y, Z = np.meshgrid(x, y, z)
        return X, Y, Z

    # Функція для створення тензорного поля з коригуванням ділення на нуль
    def tensor_field(x, y, z):
        sq = (x ** 2 + y ** 2 + z ** 2) + epsilon
        return np.array([
            [(np.sin(x + y) / sq), x, y],
            [0, (np.cos(y + z) / sq), z],
            [0, 0, (np.cos(x + z) / sq)]
        ], dtype=np.float64)

    # Функція для створення еліпсоїдів
    def create_ellipsoid(center, eigenvalues, eigenvectors, scale=1.0):
        radii = scale * np.sqrt(np.abs(eigenvalues))
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 50)
        x = np.outer(np.cos(phi), np.sin(theta))
        y = np.outer(np.sin(phi), np.sin(theta))
        z = np.outer(np.ones_like(phi), np.cos(theta))

        x *= radii[0]
        y *= radii[1]
        z *= radii[2]

        coord = np.array([x, y, z])
        coord = np.einsum('ij,jkl->ikl', eigenvectors, coord)
        coord += np.array(center).reshape(3, 1, 1)

        return coord

    # Функція для створення кубоїдів
    def create_cuboid(center, eigenvalues, eigenvectors, scale=1.0):
        radii = scale * np.sqrt(np.abs(eigenvalues))
        vertices = np.array([
            [1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1],
            [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1]
        ]) * radii.reshape(1, 3)

        vertices = vertices @ eigenvectors.T.astype(np.float64)
        vertices += np.array(center).reshape(1, 3)

        faces = [
            [vertices[j] for j in [0, 1, 2, 3]],  # Верхня грань
            [vertices[j] for j in [4, 5, 6, 7]],  # Нижня грань
            [vertices[j] for j in [0, 3, 7, 4]],  # Передня грань
            [vertices[j] for j in [1, 2, 6, 5]],  # Задня грань
            [vertices[j] for j in [2, 3, 7, 6]],  # Права грань
            [vertices[j] for j in [0, 1, 5, 4]],  # Ліва грань
        ]

        return faces

    # Функція для створення циліндрів
    def create_cylinder(center, eigenvalues, eigenvectors, scale=1.0, height=1.0):
        radius = scale * np.sqrt(np.abs(eigenvalues[0]))
        phi = np.linspace(0, 2 * np.pi, 100)
        z = np.linspace(-height / 2, height / 2, 10)
        X = np.outer(np.cos(phi), np.ones_like(z)) * radius
        Y = np.outer(np.sin(phi), np.ones_like(z)) * radius
        Z = np.outer(np.ones_like(phi), z)

        coords = np.array([X, Y, Z])
        coords = np.einsum('ij,jkl->ikl', eigenvectors, coords)
        coords += np.array(center).reshape(3, 1, 1)

        return coords

    # Побудова візуалізацій на одному полотні
    X, Y, Z = create_3d_mesh()
    tensor_values = [tensor_field(x, y, z) for x, y, z in zip(X.flatten(), Y.flatten(), Z.flatten())]

    ellipsoids = [create_ellipsoid([xi, yi, zi], *np.linalg.eigh(tensor)) for xi, yi, zi, tensor in
                  zip(X.flatten(), Y.flatten(), Z.flatten(), tensor_values)]
    cuboids = [create_cuboid([xi, yi, zi], *np.linalg.eigh(tensor), scale=0.5) for xi, yi, zi, tensor in
               zip(X.flatten(), Y.flatten(), Z.flatten(), tensor_values)]
    cylinders = [create_cylinder([xi, yi, zi], *np.linalg.eigh(tensor), scale=0.5, height=2.0) for xi, yi, zi, tensor in
                 zip(X.flatten(), Y.flatten(), Z.flatten(), tensor_values)]

    fig = plt.figure(figsize=(12, 12))

    # Субграфік для еліпсоїдів
    ax1 = fig.add_subplot(131, projection='3d')
    for ellipsoid in ellipsoids:
        ax1.add_collection3d(Poly3DCollection(ellipsoid.T, alpha=0.3, facecolor='c'))
    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")
    ax1.set_zlabel("Z-axis")
    ax1.set_title("Тривимірна візуалізація еліпсоїдів")

    # Субграфік для кубоїдів
    ax2 = fig.add_subplot(132, projection='3d')
    for cuboid in cuboids:
        ax2.add_collection3d(Poly3DCollection(cuboid, alpha=0.3, facecolor='c'))
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax2.set_zlabel("Z-axis")
    ax2.set_title("Тривимірна візуалізація кубоїдів")

    # Субграфік для циліндрів
    ax3 = fig.add_subplot(133, projection='3d')
    for cylinder in cylinders:
        ax3.add_collection3d(Poly3DCollection(cylinder.T, alpha=0.3, facecolor='c'))
    ax3.set_xlabel("X-axis")
    ax3.set_ylabel("Y-axis")
    ax3.set_zlabel("Z-axis")
    ax3.set_title("Тривимірна візуалізація циліндрів")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    match int(input()):
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()