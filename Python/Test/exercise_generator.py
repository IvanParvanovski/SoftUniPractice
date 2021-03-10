def dedupe(items):
    seen = list()
    for item in items:
        if item not in seen:
            yield item
            seen.append(item)


a = [1, 7, 2, 1, 9, 1, 7, 11]
print(list(dedupe(a)))
