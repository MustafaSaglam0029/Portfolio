def chs(names):
    return [name for i, name in enumerate(names) if round(i) == i]
name=["Ali","Ahmet","Mehmet","Mustafa"]
print(chs(name))