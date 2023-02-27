values = []
while True:
    value = int(input("Enter an integer value (0 to end): "))
    if value == 0:
        break
    values.append(value) 
sorted_values = sorted(values, reverse=True)
print("Sorted values (excluding zero) in descending order:")
for value in sorted_values:
    if value != 0:
        print(value)
