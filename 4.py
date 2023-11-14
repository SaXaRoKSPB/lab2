with open('sequence.txt') as file:
    reader_file = []
    for value in file:
        reader_file.append(float(value))
quantity_less = 0
quantity_more = 0
for index_value in range(len(reader_file)):
    if reader_file[index_value] < -5:
        quantity_less += 1
    else:
        if reader_file[index_value] <= 0:
            quantity_more += 1
print(f"\u001b[41;1m{' ' * quantity_less}\u001b[0m  < -5")
print(f"\u001b[42;1m{' ' * quantity_more}\u001b[0m  > -5")