class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __repr__(self):
        return self.time


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def date(self):
        return f"{self.year}/{self.month}/{self.day}"

    def __repr__(self):
        return self.date


class CalendarClock(Clock, Calendar):
    def __init__(self,
                 hours, minutes, seconds,
                 year, month, day):

        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, year, month, day)

    @property
    def date_and_time(self):
        return f"{self.date}\n{self.time}"

    def __repr__(self):
        calendar_repr = Calendar.__repr__(self)
        clock_repr = Clock.__repr__(self)
        return f"{calendar_repr}\n{clock_repr}"


jacob = CalendarClock(2, 49, 30, 2012, 5, 4)

print(jacob.date)
print(jacob.time)
print("-" * 15)
print(jacob.date_and_time)
print("-" * 15)
print(jacob)