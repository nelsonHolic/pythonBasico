import logging


class Logger:

    def __init__(self, function: callable):
        self.__inner_function = function

    def __call__(self, *args, **kwargs):
        result = self.__inner_function(*args, **kwargs)
        print(f"result for {args} and {kwargs} = {result}")
        return result


def suma(a: int, b: int) -> int:
    return a + b

@Logger
def invert_word(word: str):
    return word[::-1]


if __name__ == "__main__":
    suma(1, 2)
    decorated_suma = Logger(suma)
    decorated_suma(1, 2)
    invert_word("carlos habla al reves")
