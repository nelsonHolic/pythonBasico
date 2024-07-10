import random
from typing import Protocol


class Sender(Protocol):

    def send(self, message: str) -> bool:
        ...


class Notifier:
    def __init__(self, sender: Sender):
        self.__sender = sender

    def send(self, message: str) -> bool:
        was_send = self.__sender.send(message)

        if was_send:
            print(f"message '{message}' was successfully sent")
        else:
            print(f"message '{message}' could not be sent")

        return was_send


class EmailSender:

    def send(self, message: str) -> bool:
        return random.choice([True, False])


if __name__ == "__main__":
    sender = Notifier(EmailSender())
    sender.send("Hola carlos espero  este mensaje te pueda llegar")
