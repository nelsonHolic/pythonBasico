import random


class Person:
    name: str
    age: int
    height: float

    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        print(f'Hi I am {self.name}')

    def __str__(self) -> str:
        return (
            "\n------------------------\n"
            f"name = {self.name}\n"
            f"age = {self.age}\n"
            f"height = {self.height} cm\n"
        )

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    carlos = Person(name="Carlos", age=45, height=140)
    print(carlos)
    print(carlos.name)
    carlos.introduce()

    juan = Person(name="Juan", age=15, height=190)

    print(juan)
    print(juan.name)
    juan.introduce()

    users = [
        Person(
            name=f"user #{i}",
            age=random.randint(15, 40),
            height=random.randrange(140, 210)
        )
        for i in range(10)
    ]

    print(list(p for p in users))

    print(list(p for p in sorted(users, key=lambda p: p.age)))
