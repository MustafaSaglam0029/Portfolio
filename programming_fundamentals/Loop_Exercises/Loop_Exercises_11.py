def sumik(arr):
    num_list=sorted(arr)
    if len(num_list) > 3:
        return num_list[0]+num_list[1]
print(sumik([19, 5, 42, 2, 77]))
print(sumik([10, 343445353, 3453445, 3453545353453]))