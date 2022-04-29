class Phone:
    def phone_type(self):
        print('I am an ' + self.type)

class Carrier:
    def carrier_self(self):
        print('Welcome to ' + self.name)

class Headphones:
    def headphones_self(self):
        print('These are ' + self.brand)

class Android(Phone):
    type = 'Andriod'

p1 = Phone()
p1.type = 'iPhone'
p1.model = 'iPhone 13'
p1.price = '$1300'

p2 = Phone()
p2.type = 'Andriod'
p2.model = 'Samsung Galaxy Z Fold3'
p2.price = '$1800'

c1 = Carrier()
c1.name = 'At&t'
c1.signal = '5G'

h1 = Headphones()
h1.brand = 'Beats by Dre'
h1.model = 'Studio 3'

print('I am listening to music on my ' + p1.model + ' on spotify using ' + c1.signal + ' on ' + c1.name + ' with my favorite headphones the ' + h1.brand + ' ' + h1.model + '.')
