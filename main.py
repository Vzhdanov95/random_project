# PEB 8 
# Carbage collector 
# Mutable
some_list = [2, 4, 5, 40]
some_set = {"Audi", "Toyota", "Audi"}
some_dict = {"car_1": "Chevrolet", "car_2": "Hundai"}

some_set.add("Garage")
# print(some_set)

# Immutable

not_change = frozenset(("Audi", "Toyota", "BMW"))

some_tuple = (1, 1, 3, 4, 5, 6)
# print(some_tuple)

friends = ["John", "Gordon", "Vasiliy"]

for friend in friends:
    print(friend)

result = 40
while True:
    print(40)
    result = 42
    break
print(result)

print(friends)