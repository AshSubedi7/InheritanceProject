class Animal:
    alive = True
    def eat(self):
        print("Animal is eating.")

    def sleep(self):
        print("Animal is sleeping.")

class Fox(Animal):
    def hunt(self):
        print('Foxes are great hunters.')

class Eagle(Animal):
    def fly(self):
        print('Eagles can fly very well.')

class Salmon(Animal):
    def swim(self):
        print('Salmon are excelent swimmers.')

fox = Fox()
eagle = Eagle()
salmon = Salmon()

fox.hunt()
eagle.fly()
salmon.swim()
