# print("start app2")
# import app
# import p.app3
# print(f"__name__=>{__name__}")
# print(app.a)
# # print(app.aa) #AttributeError: module 'app' has no attribute 'aa'

# print("end app2")

# import math


# import app, p.app3

# from app import a

# print(a)
# # from p.app3 import a
# # from p import app3
# from p.app3 import a as a3

# print(a)
# # print(app3.a)
# print(a3)


# from constants import path as p, name ,email as e, age

# print(p, name, e, age)

# import p.app3 as p3
# print(dir())
# # print(p.app3.a)
# print(p3.a)
# import constants
# print(dir(constants))
import constants
constants.print_name()

from constants import print_name
print_name()