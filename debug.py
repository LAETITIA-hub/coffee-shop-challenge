from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

c1.create_order(coffee1, 4.5)
c1.create_order(coffee1, 5.0)
c2.create_order(coffee1, 6.0)
c2.create_order(coffee2, 3.0)

print(f"{coffee1.name} has {coffee1.num_orders()} orders.")
print(f"{coffee1.name} average price: {coffee1.average_price()}")

print("Most aficionado of Espresso:", Customer.most_aficionado(coffee1).name)
