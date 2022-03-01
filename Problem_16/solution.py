# Day 16
# Problem 16
# Date 25 Feb 2022
# Time 5:00 PM

class OrderRecord:

    def __init__(self, size):
        self.orders = list()
        self.size = size

    def __repr__(self):
        return str(self.orders)

    def addOrders(self, order_id):
        self.orders.append(order_id)
        if len(self.orders) > self.size:
            self.orders = self.orders[1:]

    def lastOrder(self, i):
        return self.orders[-i]


orderLog = OrderRecord(5)

orderLog.addOrders(1)
orderLog.addOrders(2)
orderLog.addOrders(3)

print(orderLog.orders)
print(orderLog.size)
print(orderLog.lastOrder(3))
