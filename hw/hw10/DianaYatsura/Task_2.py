class Human:
    def __init__(self, name):
        self.name = name.capitalize() if isinstance(name, str) else 'Unknown'

    def welcome_message(self):
        print(f'Hello, {self.name}!')

    @classmethod
    def species_message(cls):
        return 'Homosapiens'

    @staticmethod
    def message():
        return 'You are welcome'