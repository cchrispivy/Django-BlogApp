from .base import *

if os.environ['blog'] == 'prod':
   from .prod import *
else:
   from .devl import *

