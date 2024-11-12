def smllst(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest
print(smllst([-34, 345, -1, 100]))
#without min
