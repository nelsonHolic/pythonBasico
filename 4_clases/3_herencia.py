class Animal:
    kind: str
    height: float
    legs: int

    def __init__(self, kind: str, height: float, legs: int):
        self.kind = kind
        self.height = height
        self.legs = legs

    def make_a_sound(self):
        pass

    def poop(self):
        print("pooping")


class Dog(Animal):

    def __init__(self, height: float, legs: int):
        super().__init__("dog", height, legs)

    def make_a_sound(self):
        print("dog goes woof")


class Feline(Animal):

    def __init__(self, height: float, legs: int):
        super().__init__("feline", height, legs)

    def make_a_sound(self):
        print("feline goes roar")


class Cat(Feline):
    def make_a_sound(self):
        print("cat goes meow")


class Roach(Animal):

    def __init__(self, height: float, legs: int):
        super().__init__("roach", height, legs)


def call_animal(animal: Animal):
    animal.make_a_sound()


if __name__ == "__main__":
    cat = Cat(height=0.3, legs=4)
    call_animal(cat)

    dog = Dog(height=0.3, legs=4)
    call_animal(dog)

    roach = Roach(height=0.01, legs=6)
    call_animal(roach)
