class Bird:
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поет - {self.voice}")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f"{self.name} гуляет")

    def sing(self):
        print(f"{self.name} поет - курлык курлык")

# Создаем объект класса Pigeon
bird1 = Pigeon(name="Гоша", voice="курлык", color="серый", favorite_food="хлебные крошки")

# Используем различные функции для объекта класса
bird1.sing()
bird1.info()
bird1.walk()

# Создаем объект класса Bird
bird2 = Bird(name="Маша", voice="чирик", color="коричневый")

# Используем различные функции для объекта класса Bird
bird2.sing()
bird2.info()
