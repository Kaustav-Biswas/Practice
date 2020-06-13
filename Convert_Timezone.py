from datetime import datetime as dt
from pytz import timezone
s1 = 'Sat 02 May 2015 19:54:36 +0530'
s2 = 'Fri 01 May 2015 13:54:36 -0000'

t1 = dt.strptime(s1, '%a %d %b %Y %H:%M:%S %z')
t2 = dt.strptime(s2, '%a %d %b %Y %H:%M:%S %z')
# The astimezone() function form pytz will convert the current datetime obj to the timezone passed to it as argument.
# The argument should be a timezone() tzinfo method.
t1 = t1.astimezone(timezone('UTC'))
t2 = t2.astimezone(timezone('UTC'))
print(t1)



def change_timezone_of_datetime_object(date_time_object, new_timezone_name):
    """Return the *date_time_object* with it's timezone changed to *new_timezone_name*

    :param date_time_object: The datetime object whose timezone is to be changed
    :type date_time_object: datetime
    :param new_timezone_name: The name of the timezone to which the *date_time_object* is to be changed to
    :type new_timezone_name: str
    :rtype: datetime
    """
    # Create a pytz.timezone object for the new_timezone
    new_timezone_object = timezone(new_timezone_name)
    # Update the timezone of the datetime object
    date_time_object = date_time_object.astimezone(new_timezone_object)
    # Return the converted datetime object
    print( date_time_object)

# Testing
dtobj = dt.now(timezone('UTC'))
change_timezone_of_datetime_object(dtobj, 'Europe/London')
