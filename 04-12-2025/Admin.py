class User:
    def __init__(self, user_type):
        self.type = user_type
        self.li = []

    def power(self):
        print(f"{self.type} power")

    def display(self):
        print(self.li)


class Admin(User):
    def __init__(self):
        super().__init__("Admin")

    def add_user(self, name):
        self.li.append(name)
        print(f"Added {name}")

    def power(self, name):
        if name in self.li:
            self.li.remove(name)
            print(f"Deleted {name}")
        else:
            print(f"{name} not found")


a = Admin()
a.add_user('a')
a.add_user('b')
a.display()
a.power('b')