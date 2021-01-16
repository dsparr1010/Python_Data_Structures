"""Find missing value from arr by comparing two arrays"""

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]

arr3 = [1, 2, 3, 4, 5, 6, 7]
arr4 = [3, 5, 2, 1, 4, 6]

def finder(arr1, arr2):

    tracker = {}

    for num in arr1:
        if num not in tracker:
            tracker[num] = 1

    for num in arr2:
        if num in tracker:
            tracker[num] -=1

    for key, value in tracker.items():
        if value == 1:
            return key

# print(finder(arr1, arr2))
# print(finder(arr3, arr4))

def another_finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for index, value in enumerate(arr1):
        try:
            if value != arr2[index]:
                return value
        except IndexError:
            return arr1[-1]

# print(another_finder(arr1, arr2))
# print(another_finder(arr3, arr4))

def zipped_finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

# print(zipped_finder(arr1, arr2))
# print(zipped_finder(arr3, arr4))
