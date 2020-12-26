from datetime import datetime as dt, timedelta as td, timezone

s1 = 'Sun 10 May 2015 13:54:36 -0700'
s2 = 'Sun 10 May 2015 13:54:36 -0000'

t1 = dt.strptime(s1, '%a %d %b %Y %H:%M:%S %z')
t2 = dt.strptime(s2, '%a %d %b %Y %H:%M:%S %z')
#t1 = td(days=t.date, seconds=t.second, hours=t.hour, minutes=t.minute )
ts1 = t1.replace(tzinfo=timezone.utc).timestamp()
ts2 = t2.replace(tzinfo=timezone.utc).timestamp()
print(t1-t2)