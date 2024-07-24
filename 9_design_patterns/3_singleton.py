class Database:
    global_instance: 'Database'

    def __init__(self):
        print("instanciando")

    @classmethod
    def get_instance(cls) -> 'Database':
        if not hasattr(cls, 'global_instance'):
            cls.global_instance = cls()

        return cls.global_instance

    def query(self, body: str) -> str:
        return "results"


my_db = Database.get_instance()  # also you can instantiate using a global variable


if __name__ == "__main__":
    db = Database.get_instance()
    print(db.query("this is my awesome query"))

    db_2 = Database.get_instance()

    print(db.query("this is my second awesome query"))
