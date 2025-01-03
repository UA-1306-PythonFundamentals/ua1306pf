class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Welcome, {self.name}!')

    @classmethod
    def species(cls):
        print('You are a human. Species: Homo Sapiens.')

    @staticmethod
    def compliment():
        print('You look nice today!')


sarah = Human(name='Sarah')
sarah.greeting()
sarah.species()
sarah.compliment()
