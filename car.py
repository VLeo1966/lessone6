class Car:
    def __init__(self, make, model):
        self.make = make  # Публичный атрибут
        self._model = model  # Защищенный атрибут
        self.__year = 2022  # Приватный атрибут

    # Публичный метод
    def public_method(self):
        print(f"This is a public method. This car is made by {self.make}.")

    # Защищенный метод
    def _protected_method(self):
        print("This is a protected method.")

    # Приватный метод
    def __private_method(self):
        print("This is a private method.")


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size  # Публичный атрибут

    def get_details(self):
        return {
            'make': self.make,  # Публичный
            'model': self._model,  # Защищенный
            'battery_size': self.battery_size  # Публичный
        }


# Создаем объект tesla класса ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)

# Доступ к публичным атрибутам и методам
print(tesla.make)  # Публичный атрибут
tesla.public_method()  # Публичный метод

# Доступ к защищенным атрибутам и методам
print(tesla._model)  # Защищенный атрибут
tesla._protected_method()  # Защищенный метод

# Попытка доступа к приватному атрибуту через манглинг (mangling)
print(tesla._Car__year)  # Приватный атрибут

# Получение деталей через метод get_details
details = tesla.get_details()
print(f"Make: {details['make']}, Model: {details['model']}, Battery Size: {details['battery_size']}")
