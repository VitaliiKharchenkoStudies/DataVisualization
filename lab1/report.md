# Лабораторна робота №1 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович,  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі було виконано п'ять завдань, кожне з яких створювало різні типи графіків за допомогою бібліотеки `matplotlib` та `numpy`. Нижче наводиться короткий опис кожної функції, що відповідає за візуалізацію даних.

---

## Функція `task1()`
- Створює графіки двох функцій: `y` та `z`.
- **Вхідні дані**: Вектор `x`, що містить 100 рівномірно розподілених значень у діапазоні від -2 до 2.
- **Обчислення `y`**: `(1 + (x + 5) ** (1 / 3)) / (1 + np.sqrt(2 + x + x ** 2))`.
- **Обчислення `z`**: У залежності від значення `x` застосовуються різні формули: 
  - Якщо `x < 0`, то `z = (1 + x + x ** 2) / (1 + x ** 2)`.
  - Якщо `0 <= x < 1`, то `z = np.sqrt(1 + (5 * x) / (1 + x ** 3))`.
  - Якщо `x >= 1`, то `z = 5 * np.abs(0.7 * np.cos(x) + np.sin(x))`.
- **Вивід**: Два графіки на одній площині з відповідними підписами та легендою.


![alt task1](https://media.discordapp.net/attachments/917547349864230912/1233794158771306597/image.png?ex=662e63da&is=662d125a&hm=d4d32bcc83775d6186f1116af3e054992efe18316e6fcb0bef08b70f7f15cbbd&=&format=webp&quality=lossless)
---

## Функція `task2()`
- Створює 3D-графік поверхні.
- **Вхідні дані**: Два вектори `x` та `y`, кожен із 100 рівномірно розподілених значень у діапазоні від -2 до 2.
- **Обчислення `Z`**: `7 * np.exp(-0.5 * X - 1) * (X ** 3) - 4 * (Y ** 4)`.
- **Вивід**: 3D поверхневий графік із встановленими осями та відповідною палітрою кольорів.


![alt task2](https://media.discordapp.net/attachments/917547349864230912/1233794180913041439/image.png?ex=662e63df&is=662d125f&hm=e016910cb4eed26ae1c8c7053cf3c6ce1aa49c91bdb73958115322247a401618&=&format=webp&quality=lossless)
---

## Функція `task3()`
- Створює графіки у полярних координатах.
- **Вхідні дані**: Вектор `phi`, що містить 100 значень, рівномірно розподілених від 0 до 2π.
- **Обчислення `p_upper` та `p_lower`**:
  - `p_upper = a / np.sin(phi) + l`
  - `p_lower = a / np.sin(phi) - l`
- **Вивід**: Графіки двох конхоїд на полярній площині з відповідними підписами та легендою.


![alt task3](https://media.discordapp.net/attachments/917547349864230912/1233794198805942292/image.png?ex=662e63e3&is=662d1263&hm=afb6d8824ce7e2f63577524bc5532ddb0782e6d27ca827a9a4acaabd19d1d59f&=&format=webp&quality=lossless)
---

## Функція `task4()`
- Створює 3D-графік еліптичного циліндра.
- **Вхідні дані**: Два вектори `x` та `y`, кожен із 100 рівномірно розподілених значень у діапазоні від -2 до 2.
- **Обчислення `Z`**: `np.sqrt(1 - (X ** 2 / a ** 2)) * b`.
- **Вивід**: Два поверхневі графіки (верхня та нижня половини еліптичного циліндра) із встановленими осями, назвою та палітрою кольорів.


![alt task4](https://media.discordapp.net/attachments/917547349864230912/1233794218833612841/image.png?ex=662e63e8&is=662d1268&hm=3ec7fa37f2ae2a424160f7fac66ec9236224de58446c6302f72c09a3b48b446e&=&format=webp&quality=lossless)
---

## Функція `task5()`
- Створює 2D та 3D стовпчикові діаграми.
- **Вхідні дані**: Списки значень для різних країн у певні роки.
  - Список років: `1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000`.
  - Значення для США, Німеччини, Франції, Італії та СРСР.
- **2D діаграма**:
  - Відображає значення різних країн у різні роки на одній діаграмі.
- **3D діаграма**:
  - Відображає тривимірні стовпчики для різних країн.
- **Вивід**: 2D і 3D діаграми на одній візуалізації, з встановленими осями, назвою та підписами.


![alt task5](https://media.discordapp.net/attachments/917547349864230912/1233794239494619206/image.png?ex=662e63ed&is=662d126d&hm=6fcdefa074d63363806b8c69ee096e00590d750d6ce98a26ea991aa171143a08&=&format=webp&quality=lossless&width=839&height=671)
---

Це підсумок лабораторної роботи №1, що показує різноманітні способи візуалізації даних з використанням `matplotlib` та `numpy`.