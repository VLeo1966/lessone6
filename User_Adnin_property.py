class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Геттеры для атрибутов
    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def access_level(self):
        return self.__access_level

    # Сеттеры для атрибутов
    @name.setter
    def name(self, name):
        self.__name = name

    @access_level.setter
    def access_level(self, level):
        self.__access_level = level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.access_level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"User {user.name} added by admin {self.name}.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.user_id == user_id:
                user_list.remove(user)
                print(f"User {user.name} removed by admin {self.name}.")
                return
        print(f"User with ID {user_id} not found.")


# Пример использования
if __name__ == "__main__":
    # Создаем список пользователей
    user_list = []

    # Создаем администраторов
    admin1 = Admin(1, "Admin1234-Коля")
    admin2 = Admin(2, "Admin4567-Леша")

    # Создаем пользователей
    user1 = User(3, "Вася")
    user2 = User(4, "Петя")

    # Добавляем админов через администратора
    admin1.add_user(user_list, admin1)
    admin2.add_user(user_list, admin2)

    # Добавляем пользователей через администратора
    admin1.add_user(user_list, user1)
    admin1.add_user(user_list, user2)

    # Проверяем список админов и пользователей
    print("\nСписок пользователей:")
    for user in user_list:
        print(f"ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")

    # Удаляем пользователя через администратора
    admin1.remove_user(user_list, 2)

    # Проверяем список пользователей после удаления
    print("\nСписок пользователей после удаления:")
    for user in user_list:
        print(f"ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")
