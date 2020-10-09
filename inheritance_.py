class Date(object):
    def get_date(self):
        print("2016-05-14")


class Time(Date):
    def get_time(self):
        print("07:00:00")

# Creating an instance from `Date`
dt = Date()
dt.get_date()  # Accesing the `get_date()` method of `Date`
print("--------")

# Creating an instance from `Time`.
tm = Time()
tm.get_time()   # Accessing the `get_time()` method from `Time`.
# Accessing the `get_date() which is defined in the parent class `Date`.
tm.get_date()