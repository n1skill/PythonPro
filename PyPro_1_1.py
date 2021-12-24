class Product:
    """
    Describers product
    """
    def __init__(self, title, price, description=''):
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f'{self.title}: {self.price} грн.'


class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.phone}'


class Order:
    def __init__(self, customer: Customer, products=None):
        self.customer = customer
        self.__products = products

    def __str__(self):
        res = '\n'.join(map(str, self.__products))
        return f'{self.customer}\n{res}\nTotal price: {self.total_price()} грн.'

    def add_product(self, value: Product):
        if isinstance(value, Product):
            self.__products.append(value)

    def remove_product(self, value):
        if value in self.__products:
            self.__products.remove(value)

    def total_price(self):
        s = 0
        for item in self.__products:
            s += item.price
        return s


if __name__ == '__main__':
    x = Product('cola', 25)
    y = Product('fan', 24)
    z = Product('pepsi', 28)

    customer_1 = Customer('Tom', 'Cruse', '15317826661')
    customer_2 = Customer('Sam', 'Jerry', '15317826661')

    order_1 = Order(customer_1, [x, y, y, z])
    order_2 = Order(customer_2, [x, z])

    print(order_1)
    print(order_2)
