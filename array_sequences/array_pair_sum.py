""" Given an integer array, output all the unique pairs that sum up to a specific value k. """


arr1 = [1, 3, 2, 2]
value = 4

arr2 = [3, 5, 5, 2, 8, 4, 4]
value2 = 8

def pair_sum(arr, val):

    if len(arr) < 2: # if array has less than 2 elements, return bc cannot add any pairs
        return

    #Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = val-num # target is number that needs to be reached/added to in order to hit the value
        # if val = 4 and num = 1 (element at position 0), target value is 3
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)), max(num, target)) )

    print ('\n'.join(map(str, list(output))))



print(pair_sum(arr1, value))
print(pair_sum(arr2, value2))