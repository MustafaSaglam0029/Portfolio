def highandlow(numbers):
        number_list = numbers.split()
        number_list = [int(num) for num in number_list]
        highest = number_list[0]
        lowest = number_list[0]
        for num in number_list[1:]:
            if num > highest:
                highest = num
            elif num < lowest:
                lowest = num
        return f"{highest} {lowest}"
print(highandlow("1 2 3 4 5"))
print(highandlow("1 2 -3 4 5"))
print(highandlow("1 9 3 4 -5"))
#do it without min and max




















