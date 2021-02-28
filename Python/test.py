# import common as com
from datetime import datetime
s = str(datetime.now().date()).replace('-', '/')
print(s)

d_now = datetime.now().strftime("%Y/%m/%d")
print(d_now)
