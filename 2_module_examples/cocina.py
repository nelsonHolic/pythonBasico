"""
hdsjkhdjkhfdkjhkjdhkjsfhsjkd
"""
import random

def preparar_comida(plato: str) -> bool:

    preparar = random.choice([True, False])

    if preparar:
        print(f"preparando: {plato}")

    return preparar