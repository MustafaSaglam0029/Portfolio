def my_friends(name_list):
    return {name for name in name_list if len(name) == 4}
print(my_friends({"Ryan", "Kieran", "Jason", "Yous"}))
print(my_friends({"Peter", "Stephen", "John"}))
# I can do it in one line
