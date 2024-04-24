class Factorial:

    @staticmethod
    def factorial(number: int) -> int:
        if number < 1:
            return 1

        return number * Factorial.factorial(number - 1)


if __name__ == "__main__":
    number: int = 6
    print(f"El factorial de {number} es {Factorial.factorial(number)}")

    mi_factorial = Factorial()
    mi_factorial.factorial(5)
