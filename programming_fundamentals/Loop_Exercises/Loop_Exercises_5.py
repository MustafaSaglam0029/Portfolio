def square(numbers):
    square_list=[]
    for num in numbers:
        num = int(num)
        square_list.append(str(int(num)**2))
    return "".join(square_list)
print(square("456"))
print(square("7896"))
print(square("5546"))


