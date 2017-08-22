import platform
from base import *

if platform.node() == 'MacBook-Pro.local':
    from dev import *
else:
    from product import *
