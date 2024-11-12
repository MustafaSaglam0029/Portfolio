dictionary = {
    "name": "Rick",
    "age": "10000",
    "power": "Infinite",
    "purpose": "Pass the butter"
}
def change(dictionary):
    dictionary["name"]="Robot"
    dictionary["age"]="unknown"
    dictionary["power"]="1"
    return dictionary
print(change(dictionary))