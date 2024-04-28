# Лабораторна робота №12 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі створюємо документ у форматі LaTeX, який містить особисту інформацію, освітній та професійний досвід, технології, якими володіє користувач, а також інші досягнення та сертифікації. Документ можна використовувати як резюме або CV.

---

### Заголовок та структура документу
```latex
\documentclass{article}
\usepackage{graphicx}

\begin{document}

\title{Resume}
\author{Vitaliy Andriyovich Kharchenko}
\date{}

\maketitle
```
- **Тип документа**: Використовуємо клас `article` для створення резюме.
- **Заголовок та автор**: Вказуємо назву та автора документа.
- **Пакет `graphicx`**: Дозволяє вставляти зображення (наприклад, фото).

---

### Особиста інформація
```latex
\section*{Personal Information}
\begin{itemize}
    \item Full Name: Vitaliy Andriyovich Kharchenko
    \item Contact: +380980080718, 100operator5154@gmail.com
    \item Address: 10a Karakulna St, Zhytomyr, Ukraine
    \item Photo: \includegraphics[width=3cm]{1710884794904}
\end{itemize}
```
- **Особиста інформація**: Створюємо секцію з ім'ям, контактною інформацією, адресою та фотографією.
- **Фотографія**: Вставляємо зображення з використанням `\includegraphics`.

---

### Освіта
```latex
\section*{Education}
\begin{itemize}
    \item Bachelor: Zhytomyr Polytechnic Institute, 2019-2023
    \item Master: Kharkiv Polytechnic University, 2023-2025
\end{itemize}
```
- **Освіта**: Описуємо рівні освіти, з зазначенням навчальних закладів та років навчання.

---

### Професійний досвід
```latex
\section*{Work Experience}
\begin{itemize}
    \item INP-Software: Full-time developer, current
    \item DCode Consulting LTD: Developer, 04.2023-04.2024
    \item ITStep Academy: Part-time developer, current
\end{itemize}
```
- **Професійний досвід**: Перераховуємо місця роботи, роль, та періоди роботи.

---

### Технології
```latex
\section*{Technologies}
\begin{item list}
    \item Unity, Python, Django, JavaScript (EcmaScript), C\#, C, Asp.Net
\end{item list}
```
- **Технології**: Описуємо, з якими технологіями та мовами програмування працює користувач.

---

### Інші досягнення
```latex
\section*{Other Achievements}
\begin{item list}
    \item Student Dean of Faculty of Computer Science and Technology
    \item Certifications:
    \begin{itemize}
        \item Advanced Python
        \item Cert Prep: Unity Certified Associate Game Developer UI and 2D Games
        \item Cert Prep: Unity Certified Associate Game Developer UI and 2D Games (LinkedIn)
        \item DevNet Associate
        \item CCNA: Introduction to Networks
        \item PCAP - Programming Essentials in Python
    \end{itemize}
\end{item list}
```
- **Досягнення та сертифікації**: Перераховуємо інші досягнення, включно зі студентськими лідерськими ролями та сертифікаціями, які підтверджують навички та компетенції.

---

Цей код створює LaTex-документ, який містить інформацію, необхідну для резюме чи CV. Він включає особисті дані, освітній і професійний досвід, технології, досягнення та сертифікації. Така структура дозволяє ефективно відображати інформацію для резюме.


![](https://media.discordapp.net/attachments/917547349864230912/1234268969805021194/image.png?ex=66301e0e&is=662ecc8e&hm=9a18eed9ea62c6b104e0516cb614434981c30319ebc0450f00db62f175b160d9&=&format=webp&quality=lossless)


Детально можна переглянути у lab12.tex, та скомпільований результат у lab12.md