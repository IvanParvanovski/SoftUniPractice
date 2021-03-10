import re
pattern = r"(?P<day>\d{2})(\W)(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
result = re.finditer(pattern, input())
for date in result:
    print(f"Day: {date.group('day')}, Month: {date['month']}, Year: {date['year']}")