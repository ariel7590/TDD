from Bubble.test_bubble_sort import *


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(0, n):

        # Last i elements are already in place
        for j in range(0, n):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr


inlist = input("Enter numbers: ").split(' ')
temp = []
for i in inlist:
    temp.append(i)

if valid_list_exist(inlist) == True:
    print(inlist)

    if not valid_list_type(inlist):
        print('bad array')

    inlist = bubbleSort(inlist)

    if valid_output(inlist) == False:
        print('bad array')
    else:
        if valid_equal(temp, inlist) == True:
            if is_sorted(inlist) == True:
                print(f"good array: {inlist}")
