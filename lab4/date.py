#1
from datetime import datetime, timedelta
now = datetime.now()
task=now-timedelta(days=5)
print("vychislenie 5dnei:", task)

#2
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("yesterd:", yesterday)
print("today:", today)
print("tomorrow:", tomorrow)

#3
from datetime import datetime

now=datetime.today()
now2=now.replace(microsecond=0)
print("without micro:", now2)

#4
from datetime import datetime

now=datetime.now()
date1=datetime(2025, 2, 16, 15, 30, 0)
date2=datetime(2025, 2, 10, 5, 0, 1)
dif=date1-date2
print("difference:", dif)

seconds=dif.total_seconds()
print("in seconds:", seconds)