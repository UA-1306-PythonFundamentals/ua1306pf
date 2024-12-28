import uuid
import random


class User:
    def __init__(self, name, age, email):
        self.id = uuid.uuid4()  # Automatically generate a unique ID
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        """
        Converts the user instance to a dictionary.

        :return: Dictionary representation of the user instance.
        """
        return {"id": self.id, "name": self.name, "age": self.age, "email": self.email}

    def __str__(self):
        """
        Returns a string representation of the user instance.

        :return: String representation of the user instance.
        """
        return (
            f"User(id={self.id}, name={self.name}, age={self.age}, email={self.email})"
        )


def generate_random_users(num_users):
    first_names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",
        "Hank",
        "Ivy",
        "Jack",
    ]
    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        "Wilson",
        "Moore",
        "Taylor",
    ]
    domains = ["example.com", "testmail.com", "email.com", "mailbox.org"]

    users = []
    for _ in range(num_users):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 60)
        email = f"{name.lower().replace(' ', '.')}@{random.choice(domains)}"
        user = User(name, age, email)
        users.append(user)

    return users


if __name__ == "__main__":
    # Example usage:
    user = User("Alice", 30, "alice@example.com")
    print(user.to_dict())

    # Generate and print 10 random users
    random_users = generate_random_users(10)
    for u in random_users:
        print(u)
