def mi_funcion() -> None:
    pass

def mi_funcion_elipsis() -> None:
    ...

def hola(nombre: str) -> None:
    print(f"hola {nombre}")


def estoy_feliz() -> bool:
    return True

def funcion_muchos_params(a,b,c,d,e,f,g,h,i) -> None:
    print(a,b,c,d,e,f,g,h,i)

# a argument is the only required argument as others have default values
def funcion_muchos_params_default(a,b=1,c=1,d=1,e=1,f=1,g=1,h=1,i=1) -> None:
    print(a,b,c,d,e,f,g,h,i)

mi_funcion()

mi_valor = hola("juan")

print(mi_valor)
print(mi_valor is None)

print(estoy_feliz())

print(estoy_feliz)
print(callable(estoy_feliz))

funcion_muchos_params(1,2,3,4,5,6,7,8,9)

funcion_muchos_params_default(5, 2)
funcion_muchos_params_default(b=2, a=5)  # this is not recommended as you should keep the same order as it is defined in the function
