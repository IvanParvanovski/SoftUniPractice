x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
user_x = float(input())
user_y = float(input())

if ((user_x == x1 or user_x == x2) and (y1 <= user_y <= y2)):
    print("Border")
elif ((x1 <= user_x <= x2) and (user_y == y1 or user_y == y2)):
    print("Border")
else:
    print("Inside / Outside")

