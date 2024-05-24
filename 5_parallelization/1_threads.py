import random
import time
from threading import Thread
from time import sleep


def print_message(message: str):
    delay = random.random()
    sleep(delay)  # demorar la ejecucion ente 0 y 1 segundo
    print(f"this is the message {message}, it took: {delay}")


if __name__ == "__main__":

    start_time = time.time()
    for i in range(30):
        print_message(f"mensaje numero {i}")

    print(f"se demoro: {time.time() - start_time}")

    # Creamos una lista para almacenar los hilos
    threads: list[Thread] = []
    start_time = time.time()
    # Creamos y lanzamos 5 hilos que ejecuten la función lambda
    for i in range(30):
        thread = Thread(target=print_message, args=(i,))
        threads.append(thread)
        thread.start()

    # Esperamos a que todos los hilos terminen
    for thread in threads:
        thread.join()

    print(f"se demoro: {time.time() - start_time}")
