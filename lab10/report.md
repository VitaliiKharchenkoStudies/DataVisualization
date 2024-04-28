# Лабораторна робота №10 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович,  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі ми вивчаємо різні методи пониження розмірності, використовуючи кілька технік машинного навчання, і обчислюємо інерцію для кластеризації в 2D і 3D просторах. Код також містить бібліотеки для обробки даних та візуалізації.

---

### Імпорт бібліотек
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA, TruncatedSVD, FactorAnalysis
from sklearn.manifold import TSNE, MDS
from sklearn.cluster import FeatureAgglomeration, KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import KernelPCA
```
- **`numpy` і `pandas`**: Для обробки даних.
- **`matplotlib.pyplot` та `seaborn`**: Для візуалізації.
- **`sklearn`**: Для різних методів пониження розмірності, кластеризації та інерції.

---

### Зчитування даних
```python
data = pd.read_csv("haberman.data", header=None)
```
- **Дані**: Читаємо CSV-файл з даними (`haberman.data`). Зазвичай, цей файл містить різні атрибути та значення, які будуть використовуватися для аналізу.

---

### Методи для зниження розмірності та розрахунку інерції
```python
# Метод для зниження до 2D та розрахунку інерції
def calculate_inertia_2D(method):
    transformed = method.fit_transform(data)
    kmeans = KMeans(n_clusters=2)  # Використання KMeans для обчислення інерції
    kmeans.fit(transformed)
    return kmeans.inertia_

# Метод для зниження до 3D та розрахунку інерції
def calculate_inertia_3D(method):
    transformed = method.fit_transform(data)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(transformed)
    return kmeans.inertia_
```
- **`calculate_inertia_2D` та `calculate_inertia_3D`**:
  - Визначають методи для пониження розмірності до 2D або 3D відповідно.
  - Після зниження розмірності використовується `KMeans` для кластеризації.
  - Повертається інерція (метрика для оцінки якості кластеризації).

---

### Список методів для зниження розмірності
```python
methods_2D = [
    (PCA(n_components=2), "PCA"),
    (TruncatedSVD(n_components=2), "TruncatedSVD"),
    (FactorAnalysis(n_components=2), "Factor Analysis"),
    (TSNE(n_components=2, random_state=42), "t-SNE"),
    (MDS(n_components=2, random_state=42), "MDS"),
    (KernelPCA(n_components=2, kernel='linear'), "Kernel PCA"),
    (FeatureAgglomeration(n_clusters=2), "Feature Agglomeration")
]

methods_3D = [
    (PCA(n_components=3), "PCA"),
    (TruncatedSVD(n_components=3), "TruncatedSVD"),
    (FactorAnalysis(n_components=3), "Factor Analysis"),
    (TSNE(n_components=3, random_state=42), "t-SNE"),
    (MDS(n_components=3, random_state=42), "MDS"),
    (KernelPCA(n_components=3, kernel='linear'), "Kernel PCA"),
    (FeatureAgglomeration(n_clusters=3), "Feature Agglomeration")
]
```
- **Методи 2D та 3D**: Списки з різними методами пониження розмірності.
- **Компоненти**: Встановлюємо кількість компонентів для 2D та 3D відповідно.
- **Імена методів**: Додаємо імена для ідентифікації різних методів.

---

### Обчислення інерції
```python
# Обчислення інерції для 2D
print("Inertia for 2D:")
for method, name in methods_2D:
    inertia = calculate_inertia_2D(method)
    print(f"{name}: {inertia:.2f}")

# Обчислення інерції для 3D
print("Inertia for 3D:")
for method, name in methods_3D:
    inertia = calculate_inertia_3D(method)
    print(f"{name}: {inertia:.2f}")
```
- **Обчислення інерції для 2D та 3D**:
  - Для кожного методу з відповідного списку обчислюється інерція після зниження розмірності та кластеризації.
  - Результати інерції виводяться для кожного методу з двох списків: `methods_2D` та `methods_3D`.

---

## Відображення 2D

![](https://media.discordapp.net/attachments/917547349864230912/1234252945407868938/image.png?ex=66300f21&is=662ebda1&hm=d3b9ea6f1ee1d1cb0d80ee7e90c8d3724ddf4403097f3c33072b49cc49982452&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252945663590420/image.png?ex=66300f21&is=662ebda1&hm=4dfa4427eb1ddb9338e412384794a7fc72d71aeaa46e5773501df5cbafc1ddfa&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252945902538803/image.png?ex=66300f21&is=662ebda1&hm=0e14e15d6d3d1bdddcbeb505c7d9e9780fa76d3b9b7a221c8b452666629f5ef9&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252946150260736/image.png?ex=66300f21&is=662ebda1&hm=9d4fc61fc4bfb0b584e05e21b015bda39c051da158a95a56ee53aecbe217d460&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252946418565211/image.png?ex=66300f21&is=662ebda1&hm=82493adadc1141684df38230f2b64efefaf957f3cf473fcd3ecdac8196fcd12b&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252946636542043/image.png?ex=66300f21&is=662ebda1&hm=5d96c1f7d10224e025d9bffe54117f69ba9baf4ab70bff44bada310c643635b8&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252946871681034/image.png?ex=66300f21&is=662ebda1&hm=3ec234f38d35832cdfa03b37cfc117fa67f34552a853729a7bbfcc9418277810&=&format=webp&quality=lossless)

## Відображення 3D
![](https://media.discordapp.net/attachments/917547349864230912/1234252947110625393/image.png?ex=66300f21&is=662ebda1&hm=0f2cc01b9313e48ecfd8004221fc0176cddc4055658857eb2cadd569167751d7&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252947664146472/image.png?ex=66300f22&is=662ebda2&hm=4796d346ed6898c60b1fcb3b753845690b531ad1dd5ab8c30fcd576b1ff4cf78&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252947869925426/image.png?ex=66300f22&is=662ebda2&hm=ed76e40eb6f293aff675cedda66b6f0359b0c65201c701390b5b081fcdb0574b&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252945407868938/image.png?ex=66300f21&is=662ebda1&hm=d3b9ea6f1ee1d1cb0d80ee7e90c8d3724ddf4403097f3c33072b49cc49982452&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252945663590420/image.png?ex=66300f21&is=662ebda1&hm=4dfa4427eb1ddb9338e412384794a7fc72d71aeaa46e5773501df5cbafc1ddfa&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252945902538803/image.png?ex=66300f21&is=662ebda1&hm=0e14e15d6d3d1bdddcbeb505c7d9e9780fa76d3b9b7a221c8b452666629f5ef9&=&format=webp&quality=lossless)
![](https://media.discordapp.net/attachments/917547349864230912/1234252945902538803/image.png?ex=66300f21&is=662ebda1&hm=0e14e15d6d3d1bdddcbeb505c7d9e9780fa76d3b9b7a221c8b452666629f5ef9&=&format=webp&quality=lossless)

___

У консоль виводить

```
Inertia for 2D:
PCA: 27430.68
TruncatedSVD: 15589.13
Factor Analysis: 400.79
t-SNE: 30504.32
MDS: 27845.05
Kernel PCA: 27346.90
Feature Agglomeration: 7417.94
Inertia for 3D:
PCA: 30512.68
TruncatedSVD: 30511.90
Factor Analysis: 713.32
t-SNE: 3714.68
MDS: 30673.73
Kernel PCA: 30622.68
Feature Agglomeration: 18947.30
```

Якщо розглядати значення інерції (Inertia), які отримали, можна зробити кілька висновків:

- **Найменше значення інерції у 2D** має метод **Factor Analysis (FA)** (400.79). Це вказує на те, що цей метод найкраще знижує розмірність даних до 2D, при цьому кластеризація досить щільна.
- **Найменше значення інерції у 3D** також має **Factor Analysis (FA)** (713.32), що підтверджує його ефективність у зниженні розмірності до 3D.
- Інші методи мають значно вищі значення інерції, що може означати, що вони не так добре групують дані або мають більш розкидані точки після зниження розмірності.

На основі цих результатів:
- Найкращим методом для пониження розмірності до **2D та 3D** є **Factor Analysis (FA)**.
- Якщо необхідно зменшити розмірність даних до 2D або 3D, використання Factor Analysis, ймовірно, надасть найкращі результати з точки зору інерції, що вказує на щільну кластеризацію даних.
