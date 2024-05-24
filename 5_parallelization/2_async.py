import asyncio
import random
import time
from typing import Coroutine


async def print_message(message: str):
    delay = random.random()
    await asyncio.sleep(1)  # Simulamos una tarea que toma tiempo
    print(f"this is the message {message}, it took: {delay}")


# Otra función asíncrona que ejecuta varias veces la función saludo
async def main():
    start_time = time.time()
    for i in range(30):
        await print_message(f"mensaje numero {i}")

    print(f"se demoro: {time.time() - start_time}")

    # Creamos una lista para almacenar los hilos
    tasks: list[Coroutine] = []
    start_time = time.time()
    # Creamos y lanzamos 5 hilos que ejecuten la función lambda
    for i in range(30):
        tasks.append(print_message(f"mensaje numero {i}"))

    await asyncio.gather(*tasks)

    print(f"se demoro: {time.time() - start_time}")

# Creamos el event loop y ejecutamos la función main
if __name__ == "__main__":
    asyncio.run(main())
