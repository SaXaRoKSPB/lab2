plane = [[f"\u001b[47m "] * 5 for axis_OY in range(11)]
for values_OY in range(11):
    if values_OY % 3 == 0:
        plane[values_OY][values_OY // 3] = f"\u001b[44m "
for axis_OY in range(len(plane)-1, -1, -1):
    print(f"\u001b[47m{str(axis_OY)}", *plane[axis_OY])
axis_OX = ' ' * 2
for value_OX in range(4):
    axis_OX += f"{str(value_OX)} "
print(f"{axis_OX}\u001b[0m")
print(f"f(x)=3x")