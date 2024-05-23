import sys
import datetime 
from datetime import datetime, timedelta

t1=datetime.now()
# Increase the limit for integer string conversion
sys.set_int_max_str_digits(100000000) 
for i in range(43):
    value = 2**i
    print(value)
    print("")

t2=datetime.now()
d=t2-t1
p=d.total_seconds()
print("seconds:"+str(p))
print("")
print("done")