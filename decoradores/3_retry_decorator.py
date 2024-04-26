import random


def dividir(a: int, b: int) -> int:
    try:
        return a // b
    except ZeroDivisionError:
        return 0

def error_random():
    if random.choice([True, False]):
        raise Exception("Falle")


def retry(n_retries: int) -> callable:
    def my_internal(my_func: callable):
        def my_other_internal(*args, retries=n_retries, **kwargs):
            try:
                result = my_func(*args, **kwargs)
            except Exception as e:  # solo se ejecuta si hubo un error
                if retries <= 0:
                    raise e
                print(f"Tuve un error, quedan {retries - 1} re intentos")
                result = my_other_internal(*args, retries=retries-1, **kwargs)
            else:  # se ejecuta solo si no hubo error dentro del try
                print("Aqui no hubo un error")
            finally:  # Siempre se ejecutara sin importar si hubo o no error en el try
                print("Siempre me voy a ejecutar")

            return result
        return my_other_internal

    return my_internal


@retry(n_retries=5)
def fallar():
    if random.choice([True, True, True, True, True, False]):
        raise Exception("fallar")

if __name__ == "__main__":
    result = dividir(5, 2)
    print(result)
    result = dividir(5, 0)
    print(result)

    error = False

    while not error:
        try:
            error_random()
        except Exception:
            error = True

    fallar()