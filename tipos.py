strings: str = "soy la variable"
number: int = 1
decimal: float = 1.0
dictionaries: dict = {}
lists: list = []  # iterator
objecto: object = object
booleans: bool = True
tupla: tuple = (1,)
conjuntos: set = {1}


def print_lists() -> None:
    products: list[str] = ["tomatoes", "potatoes", "onions"]
    print(f"My first product is {products[0]}")

    i = 0
    while i < len(products):  # for i=0; i< len(products); i++
        print(f"My product #{i} is {products[i]}")
        i += 1

    for product in products:
        print(f"My product is {product}")

    for i, product in enumerate(products):
        print(f"My product #{i} is {product}")


def print_dicts() -> None:
    prices: dict[str, int] = {
        "tomatoes": 2000,
        "potatoes": 3000,
        "onions": 2500,
    }

    print("Tomatoes price is: " + str(prices["tomatoes"]) + " and potatoes price is" + str(prices["potatoes"]))
    print("Tomatoes price is: {0}".format(prices["tomatoes"]))
    print("Tomatoes price is: {price}".format(price=prices["tomatoes"]))
    print(f"Tomatoes price is: {prices['tomatoes']}")

    for key in prices.keys():
        print(f"product is {key}")

    for val in prices.values():
        print(f"price is {val}")

    for key, val in prices.items():
        print(f"{key} price is {val}")


def print_hi(name: str) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Carlos")
    print_lists()
    print_dicts()
