
# class BaseModel:
#     @classmethod
#     def get_by_id(cls, id):
#         print(f"select * from {cls.table_name} where id={id}")
#         return cls()
    
#     @staticmethod
#     def f():
#         print("test")

# class User(BaseModel):
#     table_name = "user"
#     # def get_by_id(self, id):
#     #     print(f"select * from {self.table_name} where id={id}")
#     #     return User()

# class Order(BaseModel):
#     table_name = "order"
#     # def get_by_id(self, id):
#     #     print(f"select * from {self.table_name} where id={id}")
#     #     return Order()


# u = User()
# o = Order()
# u.get_by_id(10)
# o.get_by_id(10)

# print(User.get_by_id(55))
# print(Order.get_by_id(55))
# User.f()
# u = User.f()
