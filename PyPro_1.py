#Exercise 1
class Market:
    """
    Desc:
    First = price
    Second = desc
    Third = vol
    """
    def __init__(self, price, desc, vol):
        self.price = price
        self.desc = desc
        self.vol = vol

    def __str__(self):
        return f'{self.price} {self.desc} {self.vol}.'


perfume1 = Market(4000,'Chanel Bleu De','100ml')
perfume2 = Market(4500,'Chanel Allure','150ml')
print(perfume1, perfume2, sep='\n')


#Exercise 2
class buyer:
    """
    Desc:
    First = First name
    Second = Last name
    Third = Phone number
    Fourth = Birthday
    """
    def __init__(self, first_name, last_name, phone, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.birthday}.'


buyer1 = buyer('Tom','Cruise','+1(212)653-11-21','03.04.1962')
buyer2 = buyer('Kate','Noel','+1(344)172-12-13','19.12.1978')
print(buyer1, buyer2, sep='\n')
