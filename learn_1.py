class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fuctos Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Carmel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('You got {} cal energy'.format(self.calories))


class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fuctos Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Carmel Color'
    ]


coke_a = CaffeineFree('CocaCola_FREE')
coke_a.drink()


class TestA:
    attr = 1


obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)


class TestB:
    attr = 1


obj_b = TestB()
obj_c = TestB()
obj_b.attr = 42
print(obj_c.attr)


class TestC:
    attr = 1

    def __init__(self):
        self.attr = 42


obj_d = TestC()
print(obj_d.attr)



