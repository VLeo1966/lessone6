# lessone6

 #### Домашнее задание в файле user_and_admin.py

+++++++++++++++++++++++++++++++++++++++++++++++++++
 
#### Класс `User`: 
* **Инкапсулирует данные о пользователе**: идентификатор, 
* имя и уровень доступа.
* **Методы для получения и установки значений атрибутов**. 
#### Класс `Admin`:
* **Наследуется от класса `User`**.
* **Инициализирует администратора с уровнем доступа `admin`**.
* **Методы `add_user` и `remove_user` для добавления и удаления пользователей из списка**. 
#### Инкапсуляция данных: 
* **Все атрибуты инкапсулированы и защищены от прямого доступа**. 
* **Методы-геттеры и сеттеры для доступа и изменения атрибутов**. 

Этот пример демонстрирует создание и управление пользователями
с использованием администраторского аккаунта.

C:\Users\valle\OneDrive\Документы\GitHub\lessone6\venv\Scripts\python.exe C:\Users\valle\OneDrive\Документы\GitHub\lessone6\user_and_admin.py 

User Admin1234-Коля added by admin Admin1234-Коля.
User Admin4567-Леша added by admin Admin4567-Леша.
User Вася added by admin Admin1234-Коля.
User Петя added by admin Admin1234-Коля.
ID: 1, Name: Admin1234-Коля, Access Level: admin
ID: 2, Name: Admin4567-Леша, Access Level: admin
ID: 3, Name: Вася, Access Level: user
ID: 4, Name: Петя, Access Level: user
User Admin4567-Леша removed by admin Admin1234-Коля.
ID: 1, Name: Admin1234-Коля, Access Level: admin
ID: 3, Name: Вася, Access Level: user
ID: 4, Name: Петя, Access Level: user

Process finished with exit code 0





