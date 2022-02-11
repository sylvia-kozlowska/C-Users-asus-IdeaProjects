import copy


def my_deepcopy(d: dict) -> dict:
   """
    Copy a dictionary, creating copies of the 'list' or 'dict' values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

   :param d: The dictionary to copy
   :return: A copy of 'd', with the values being copies of the original values.

   """
   new_dict ={}
   for key, value in d.items():
       new_value = value.copy()
       new_dict[key] = new_value
   return new_dict


animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

answer = my_deepcopy(animals)
print(answer)
# Perform a shallow copy
things = animals.copy()

# Perform a deep copy
# things = copy.deepcopy(animals)

# animals["teddy"] = "toy"
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])
print(id(answer["teddy"]), answer["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
