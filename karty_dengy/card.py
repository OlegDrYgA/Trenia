class Card:
    number = '0000 0000 0000 0000'
    valiDate = '01/99'
    holder = 'unnknown'

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.validDate = date

    def pay(self, amount):
        print('C  карты', self.number, 'списали', amount)
