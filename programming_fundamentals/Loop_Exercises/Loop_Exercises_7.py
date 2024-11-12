def remove(string):
    if len(string) >2:
        r_string=string[1:len(string)-1]
        return r_string
    else:
        return string
print(remove("mustafa"))
