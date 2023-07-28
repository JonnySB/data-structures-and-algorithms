# merge sort

# Merge function - helper function to combine two sorted list
def merge(arr1: list, arr2: list):
    arr3 = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    if i < len(arr1):
        arr3.extend(arr1[i:])
    else:
        arr3.extend(arr2[j:])
    return arr3







arr1 = []
arr2 = [2,4,7,8]

print(merge(arr1,arr2))
