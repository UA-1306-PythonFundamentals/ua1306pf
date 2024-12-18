from utils import *
from models import *

functions = []
for module in [admin, user, formatter, logger]:
    functions.extend(attr_name for attr_name in dir(module) if not attr_name.startswith("__"))

print(functions)
