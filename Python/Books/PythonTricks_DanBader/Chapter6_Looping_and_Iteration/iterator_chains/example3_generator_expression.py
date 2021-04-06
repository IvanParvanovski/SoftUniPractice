integers = range(9)
squared = (i * i for i in integers)
negated = (-i for i in squared)
print(negated)


for x in negated:
    print(x)
