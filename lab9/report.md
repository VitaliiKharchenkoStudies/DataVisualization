# Лабораторна робота №9 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі ми створюємо граф зв'язків між акаунтами в Instagram, відображаючи взаємозв'язки між підписниками та тими, на кого підписані. Для цього використовуємо бібліотеку `instaloader` для отримання інформації з Instagram і `networkx` для візуалізації графів.

Мій основний акаунт — це `mrendermeshka`. Через повідомлення про "too many requests" я створив інший акаунт, щоб отримати необхідну інформацію. Новий акаунт підписався на мене, а також на кількох інших користувачів, щоб створити граф. Слід зазначити, що API для роботи з Instagram, який рекомендували раніше, більше не актуальний через зміни в дизайні сторінки для десктоп версії.

---

### Імпорт бібліотек
```python
import instaloader
import networkx as nx
import matplotlib.pyplot as plt
```
- **`instaloader`**: Для завантаження даних з Instagram.
- **`networkx`**: Для побудови та візуалізації графів.
- **`matplotlib.pyplot`**: Для візуалізації графа.

---

### Ініціалізація та збір даних
```python
L = instaloader.Instaloader()  # Створення об'єкта Instaloader
L.login("thisaccountcananyoneuse", "thisispassword2024")  # Вхід в акаунт

# Отримання метаданих профілю
profile = instaloader.Profile.from_username(L.context, "thisaccountcananyoneuse")

# Списки підписників та підписників
followers_list = []
following_list = []

# Збір підписників
for follower in profile.get_followers():
    followers_list.append(follower.username)

# Збір тих, на кого підписані
for following in profile.get_followees():
    following_list.append(following.username)
```
- **Логін у акаунт**: Логін через `instaloader` з використанням облікових даних.
- **Збір підписників та тих, на кого підписані**:
  - Збираємо списки підписників і тих, на кого підписані.
  - Дані зберігаються у відповідних списках.

---

### Створення та візуалізація графа
```python
# Ініціалізація графа
G = nx.Graph()  # Створення нового графа
main_account = "thisaccountcananyoneuse"  # Основний акаунт

# Додавання вузла для основного акаунта
G.add_node(main_account)

# Додавання зв'язків між основним акаунтом і підписниками
for follower in followers_list:
    G.add_edge(main_account, follower)

# Додавання зв'язків між основним акаунтом і тими, на кого підписані
for following in following_list:
    G.add_edge(main_account, following)
```
- **Створення графа**: Ініціалізуємо новий граф з основним вузлом, який представляє акаунт.
- **Зв'язки між акаунтами**:
  - Додаємо зв'язки від основного акаунта до підписників та тих, на кого підписані.
  - Це створює базову структуру графа.

---

### Додавання зв'язків між підписниками
```python
# Функція для отримання даних у вигляді множини
def GetDataToSet(data):
    return {info.username for info in data}

# Додавання зв'язків між підписниками, якщо вони підписані один на одного
for follower in followers_list:
    follower_profile = GetDataToSet(instaloader.Profile.from_username(L.context, follower).get_followers())
    for following in following_list:
        following_profile = GetDataToSet(instaloader.Profile.from_username(L.context, following).get_followees())
        if follower_profile.intersection(following_profile) or follower_profile.intersection(follower) or following_profile.intersection(following):
            G.add_edge(follower, following)
```
- **Функція `GetDataToSet`**: Перетворює список даних на множину користувачів.
- **Додавання зв'язків між підписниками**:
  - Якщо підписники або ті, на кого підписані, взаємно підписані один на одного, додаємо зв'язок між ними в графі.
  - Це допомагає визначити додаткові зв'язки у структурі графа.

---

### Візуалізація графа
```python
plt.figure(figsize=(8, 8))  # Встановлення розміру графа
nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
plt.title("Граф підписчиків Instagram")  # Заголовок графа
plt.show()  # Відображення графа
```
- **Розмір графа**: Встановлюємо розмір візуалізації `figsize=(8, 8)`.
- **Візуалізація графа**:
  - Використовуємо `nx.draw()` для відображення графа з підписами вузлів.
  - Встановлюємо розмір і колір вузлів, розмір шрифту та інші параметри для візуалізації.
  - Відображаємо граф за допомогою `plt.show()`.

---


![](https://media.discordapp.net/attachments/917547349864230912/1234257584572076082/image.png?ex=66301373&is=662ec1f3&hm=53f9f051db729b3281c27286e518ae1c263c6b8cc3dadd2cb9b57a66a13634e3&=&format=webp&quality=lossless&width=671&height=671)