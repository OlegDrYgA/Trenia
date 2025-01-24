class User:
    age = 0
    email = 'qwerty@mail.com'

    def __init__(self, name):
        print('Я создался')
        self.username = name

    def sayName(self):
        print('Меня зовоут', self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card

    def addEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email
