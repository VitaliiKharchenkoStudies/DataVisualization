# Лабораторна робота №4 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович,  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі створюється анімація 2D-спіралі та 3D-спіралі за допомогою бібліотек `matplotlib` та `numpy`. Давайте розглянемо код із поясненням кожної частини.

---

### Імпорт бібліотек
```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
```

### Ініціалізація даних
```
# Параметри для 2D-спіралі
r2d = np.linspace(0, 10, 100)
theta2d = np.linspace(0, 10 * np.pi, 100)

# Параметри для 3D-спіралі
r3d = np.linspace(0, 10, 100)
theta3d = np.linspace(0, 10 * np.pi, 100)
z = np.linspace(0, 10, 100)

# Координати для 2D-спіралі
x2d = r2d * np.cos(theta2d)
y2d = r2d * np.sin(theta2d)

# Координати для 3D-спіралі
x3d = r3d * np.cos(theta3d)
y3d = r3d * np.sin(theta3d)
```

### Створення фігури для анімації
```
fig = plt.figure(figsize=(12, 6))

# 2D-спіраль
ax2d = fig.add_subplot(121)
ax2d.set_xlim(-12, 12)
ax2d.set_ylim(-12, 12)
circle2d, = ax2d.plot([], [], 'bo', ms=10)

# 3D-спіраль
ax3d = fig.add_subplot(122, projection='3d')
ax3d.set_xlim(-12, 12)
ax3d.set_ylim(-12, 12)
ax3d.set_zlim(0, 12)
sphere3d, = ax3d.plot([], [], 'bo', ms=10)
```

### Ініціалізація анімації
```
# Функція ініціалізації
def init():
    circle2d.set_data([], [])
    sphere3d.set_data([], [])
    sphere3d.set_3d_properties([])
    return circle2d, sphere3d
```

### Оновлення анімації
```
# Функція оновлення анімації
def update(frame):
    # Оновлення 2D-анімації
    circle2d.set_data([x2d[frame]], [y2d[frame]])
    
    # Оновлення 3D-анімації
    sphere3d.set_data([x3d[frame]], [y3d[frame]])
    sphere3d.set_3d_properties([z[frame]])
    
    return circle2d, sphere3d
```

### Створення та збереження анімації
```
# Створення анімації
ani = FuncAnimation(
    fig, 
    update, 
    frames=len(x2d), 
    init_func=init, 
    blit=True
)

# Збереження анімації у форматі GIF
ani.save('spiral_2d_3d_animation.gif', writer='pillow', fps=30)

# Відображення анімації
plt.show()
```

---

Цей код демонструє створення анімації двох спіралей — 2D та 3D, використовуючи `FuncAnimation`. Кожна функція, включно з ініціалізацією, оновленням, та створенням фігури, має своє призначення у створенні анімації та збереженні її у форматі GIF.

#### Соціальні мережі

Одним із завдань було викласти це у соціальні мережі, це можна переглянути на моєму [LinkedIn](https://www.linkedin.com/posts/mrendermeshka_i-think-everyone-who-follows-my-linkedin-activity-7190081215784210432-coaq/?utm_source=share&utm_medium=member_desktop), а також на скріншоті

![alt linkedin post](https://media.discordapp.net/attachments/917547349864230912/1233874341943578756/image.png?ex=662eae87&is=662d5d07&hm=0291ef11cc0188dc226d904b29de252dae05862ea71caffeb8bde7f432a7e42b&=&format=webp&quality=lossless)