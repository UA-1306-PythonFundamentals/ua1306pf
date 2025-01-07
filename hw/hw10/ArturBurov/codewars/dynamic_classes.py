import re


def class_name_changer(cls, new_name):
    if not new_name:
        raise ValueError("Class name cannot be empty")
    if not re.match(r"^[A-Z][a-zA-Z0-9]*$", new_name):
        raise ValueError(
            "Invalid class name. Must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name


class MyClass:
    pass


print("Original name:", MyClass.__name__)  # Output: Original name: MyClass

class_name_changer(MyClass, "UsefulClass")
print("New name:", MyClass.__name__)  # Output: New name: UsefulClass

class_name_changer(MyClass, "AnotherUsefulClass")
print("New name:", MyClass.__name__)  # Output: New name: AnotherUsefulClass

try:
    class_name_changer(MyClass, "invalid name")
except ValueError as e:
    print(e)  # Output: Invalid class name. Must start with an uppercase letter and contain only alphanumeric characters.
