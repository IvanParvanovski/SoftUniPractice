lenght = int(input())
width = int(input())
height = int(input())
deff = float(input())

full_V = lenght * width * height
V1 = full_V * 0.001
V2 = V1 * (1-deff * 0.01)

print(f"{V2:.3f}")