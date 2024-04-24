def saludar_antes(my_func: callable):
    def my_internal(*args, **kwargs):
        print(f"Me gusta saludar `{my_func.__name__}` antes de ejecutar")
        return my_func(*args, **kwargs)

    return my_internal


def suma_sin_decorador(a: int, b: int) -> int:
    return a + b


result = suma_sin_decorador(4, 5)
print(result)

## decorar una funcion de forma directa

my_new_decorated_func = saludar_antes(suma_sin_decorador)

result = my_new_decorated_func(4, 5)
print(result)

@saludar_antes
def suma_con_decorador(a: int, b: int) -> int:
    return a + b


result = suma_con_decorador(1, 2)
print(result)