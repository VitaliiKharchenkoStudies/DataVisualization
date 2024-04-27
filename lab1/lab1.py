import sys
import matplotlib.pyplot as plt
import numpy as np

def task1():
    def y_function(x):
        return (1 + (x + 5) ** (1 / 3)) / (1 + np.sqrt(2 + x + x ** 2))

    def z_function(x):
        if x < 0:
            return (1 + x + x ** 2) / (1 + x ** 2)
        elif 0 <= x < 1:
            return np.sqrt(1 + (5 * x) / (1 + x ** 3))
        else:
            return 5 * np.abs(0.7 * np.cos(x) + np.sin(x))

    x = np.linspace(-2, 2, 100)
    y = [y_function(val) for val in x]
    z = [z_function(val) for val in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='y = ((1+(x+5)^(1/3))/(1+√(2+x+x^2))')
    plt.plot(x, z, label='z based on condition')
    plt.title('Graphs of y and z Functions')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()



def task2():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)

    X, Y = np.meshgrid(x, y)

    Z = 7 * np.exp(-0.5 * X - 1) * (X ** 3) - 4 * (Y ** 4)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title('3D Surface Plot: z = 7 * exp(-0.5 * x - 1) * (x^3) - 4 * y^4')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    plt.show()

def task3():
    a = 1
    l = 0.5

    phi = np.linspace(0, 2 * np.pi, 100)

    p_upper = a / np.sin(phi) + l
    p_lower = a / np.sin(phi) - l

    plt.figure(figsize=(8, 6))
    plt.polar(phi, p_upper, label='p = a/sin(phi) + l')
    plt.polar(phi, p_lower, label='p = a/sin(phi) - l')
    plt.title('Графік конхоїди у полярних координатах')
    plt.legend()
    plt.grid(True)
    plt.show()

def task4():
    a = 2
    b = 1

    x = np.linspace(-a, a, 100)
    y = np.linspace(-b, b, 100)

    X, Y = np.meshgrid(x, y)

    Z = np.sqrt(1 - (X ** 2 / a ** 2)) * b

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, -Z, cmap='viridis', alpha=0.7)  # Верхня і нижня половини

    ax.set_title("Еліптичний циліндр")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.show()

def task5():
    # Дані з таблиць
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
    usa = [43, 56, 69, 76.5, 93.5, 105, 128.5, 146, 157.5, 175]
    germany = [16, 19, 20, 21.5, 23, 29, 37, 40.5, 46.5, 52.5]
    france = [21.5, 22, 22.5, 23, 23.5, 29.5, 47, 53, 65, 76.5]
    italy = [13.5, 14.5, 16, 17, 18.5, 30.5, 42, 44.5, 49, 56]
    ussr = [37, 50.5, 58.8, 63, 75, 81.5, 87.5, 98, 120, 100]

    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.bar(years, usa, width=3, label='США')
    plt.bar(years, germany, width=3, label='Германія', bottom=usa)
    plt.bar(years, france, width=3, label='Франція', bottom=[usa[i] + germany[i] for i in range(len(usa))])
    plt.bar(years, italy, width=3, label='Італія', bottom=[usa[i] + germany[i] + france[i] for i in range(len(usa))])
    plt.bar(years, ussr, width=3, label='СРСР',
            bottom=[usa[i] + germany[i] + france[i] + italy[i] for i in range(len(usa))])
    plt.title('2D Стовпчикова діаграма')
    plt.xlabel('Роки')
    plt.ylabel('Значення')
    plt.legend()
    plt.grid(True)

    ax = plt.subplot(2, 1, 2, projection='3d')  # Друга діаграма у другому рядку
    x_pos = np.array(years)
    y_pos = np.zeros(len(years))
    z_pos = np.zeros(len(years))
    dx = np.ones(len(years)) * 2
    dy = np.ones(len(years)) * 2

    ax.bar3d(x_pos, y_pos, z_pos, dx, dy, usa, color='b', label='США')
    ax.bar3d(x_pos, y_pos + 2, z_pos, dx, dy, germany, color='g', label='Германія')
    ax.bar3d(x_pos, y_pos + 4, z_pos, dx, dy, france, color='r', label='Франція')
    ax.bar3d(x_pos, y_pos + 6, z_pos, dx, dy, italy, color='y', label='Італія')
    ax.bar3d(x_pos, y_pos + 8, z_pos, dx, dy, ussr, color='m', label='СРСР')

    ax.set_xlabel('Роки')
    ax.set_ylabel('Країни')
    ax.set_zlabel('Значення')
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_yticklabels(['США', 'Германія', 'Франція', 'Італія', 'СРСР'])
    plt.title('3D Стовпчикова діаграма')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    match int(input("task\n->")):
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case 5:
            task5()