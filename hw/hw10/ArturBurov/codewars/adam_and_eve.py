class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


paradise = God()
print(isinstance(paradise[0], Man) and isinstance(paradise[0], Human))
print(isinstance(paradise[1], Woman) and isinstance(paradise[1], Human))
