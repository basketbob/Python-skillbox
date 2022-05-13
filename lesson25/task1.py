class Property:

    def __init__(self, worth):
        self.worth = worth

    def nalogCalc(self):
        pass


class Apartment(Property):
    def __init__(self, cost):
        self.cost = cost
        super().__init__(cost)

    def nalogCalc(self):
        return self.cost / 1000


class Car(Property):
    def __init__(self, cost):
        self.cost = cost
        super().__init__(cost)

    def nalogCalc(self):
        return self.cost / 200


class CountryHouse(Property):
    def __init__(self, cost):
        self.cost = cost
        super().__init__(cost)

    def nalogCalc(self):
        return self.cost / 500


cash = int(input('сколько денег у тебя?'))
what = int(input('тип имущества?'))
cost = int(input('сколько стоит?'))

prop = 0
if what in (1, 2, 3):
    if what == 1:
        prop = Apartment(cost)
    elif what == 2:
        prop = Apartment(cost)
    elif what == 3:
        prop = Apartment(cost)

    if prop.nalogCalc() <= cash:
        print('Денег хватает!')
    else:
        print('Иди работай!')
else:
    print('Тип имущества только 1, 2 или 3!!!')

print('FINISH!!!')
