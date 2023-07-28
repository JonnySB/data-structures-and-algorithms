# merge sort

# Merge function - helper function to combine two sorted list
def merge(arr1: list, arr2: list):
    combined = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    while i < len(arr1):
        combined.append(arr1[i])
        i += 1
    while j < len(arr2):
        combined.append(arr2[j])
        j += 1
    return combined

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    midpoint = len(arr) // 2
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])

    return merge(left,right)

print(merge_sort([8,5,3,2,5]))
