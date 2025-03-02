# Using range
print("Using range:")
my_list = ['a', 'b', 'c', 'd', 'e']
for i in range(len(my_list)):
    print(f"Index: {i}, Value: {my_list[i]}")

# Using enumerate
print("\nUsing enumerate:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# Using enumerate with a start index
print("\nUsing enumerate with start index:")
for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")
