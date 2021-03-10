people = int(input())
capacity = int(input())
courses_full = int(people / capacity)
courses_diff = people % capacity
if 0 < courses_diff < capacity:
    courses_diff = 1
courses_total = courses_full + courses_diff

print(courses_total)
