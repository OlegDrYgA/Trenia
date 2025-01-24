from user import User
from card import Card
from email import Email


jon = User('jon')
Simon = User('Simon')

jon.sayName()
jon.setAge(33)
jon.sayAge()

card = Card('0000 0000 0000 0000', '11/30', 'jon S')

jon.addCard(card)
jon.getCard().pay(1900)

email = Email('qwerty@.com')

Simon.addEmail(email)
Simon.getEmail.email_Us
