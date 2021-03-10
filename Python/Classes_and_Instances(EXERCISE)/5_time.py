def add_zero_behind(part):
    if len(str(part)) == 1:
        return f"0{part}"
    return part


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def next_second(self):
        self.seconds += 1

        if self.seconds > Time.max_seconds:
            self.minutes += 1
            self.seconds = 0

        if self.minutes > Time.max_minutes:
            self.hours += 1
            self.minutes = 0

        if self.hours > Time.max_hours:
            self.hours = 0

        return self.get_time()

    def get_time(self):
        self.seconds = add_zero_behind(self.seconds)
        self.minutes = add_zero_behind(self.minutes)
        self.hours = add_zero_behind(self.hours)

        return f"{self.hours}:{self.minutes}:{self.seconds}"


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
