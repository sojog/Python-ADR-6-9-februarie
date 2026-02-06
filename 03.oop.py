from typing import Optional

class STBCard:
    def __init__(self, user: Optional[str], available_trips: int, credit: int):
        self.user = user
        # protected / internal 
        self._available_trips = available_trips
        ## private
        self.__credit = credit

        if user == None:
            self.user = 'Nenominal'

    ## str(obj) -> print(str(obj))
    def __str__(self) -> str:
        return f"{self.user} are {self._available_trips} calatori si {self.__credit} credit"

    def __int__(self) -> int:
        return self.__credit
    
    def __call__(self, *args, **kwds):
        print("Obiectul a fost chemat cu functia __call__")
        self.validate_trip()

    ## obiect1 > obiect2
    def __gt__(self, other):
        return self.credit > other.credit
    
    ## obiect1 += 10 -> obiect = obiect + 10
    def __iadd__(self, suma):
        self.__credit += suma
        return self


    @property
    def credit(self):
        return self.__credit 

    def validate_trip(self) -> None:
        if self._available_trips > 0:
            self._available_trips -= 1
            print('Calatorie placuta.')
        else:
            self.buy_trip_by_card()
            self.validate_trip()

    def buy_trip_by_card(self) -> None:
        if self.__credit >= 3:
            self._available_trips += 1
            self.__credit -=3
        else:
            raise ValueError(f'Insufficient credit available. Needed 3$, but only {self.__credit} available. Please top-up.')

    def top_up(self) -> None:
        value = int(input('Valoare top-up:'))
        self.__credit += value
        print(f'Soldul curent al creditului este: {self.__credit}')




card1 = STBCard("Alin", 3, 10)
print(card1)

card2 = STBCard("Florina", 5, 21)
print(card2)


credit_card1 = int(card1)
print("Credit card 1:", credit_card1, type(credit_card1))


card1._available_trips = 20
print(card1)

# card1.__credit = 20
# print(card1.__credit)

print(card1._STBCard__credit )
print(card1.credit)


card1()

card1.validate_trip()

print(dir(card1))

# gt

print(card1 > card2)

print(card1 < card2)

print(card1)
card1 += 100
print(card1)