import cocina
from cocina import preparar_comida
from my_package import preparar_a
from my_package.otra_cocina import *  # not recommended

if __name__ == "__main__":
    print("Bienvenido porfavor pase")

    plato: str = input("Porfavor indique su plato: ")

    cocina.preparar_comida(plato)
    preparar_comida(plato)
    preparar_b()
    preparar_c()
