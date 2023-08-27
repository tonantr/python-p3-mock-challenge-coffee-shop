class Coffee:

    all = []

    def __init__(self, name):
        if len(name) <= 2:
            raise Exception
        if type(name) != str:
            raise Exception
        self._name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        total = 0
        for order in self.orders():
            total += 1
        return total
    
    def average_price(self):
        sum = 0
        for order in self.orders():
            sum += order.price
        return sum / len(self.orders())

class Customer:

    all = []

    def __init__(self, name):
        if 15 < len(name) or len(name) < 1:
            raise Exception
        self._name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if type(value) != str:
            raise Exception
        self._name = value
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if not isinstance(price, float):
            raise Exception
        if 1.0 > price or price > 10.0:
            raise Exception
        self._price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    