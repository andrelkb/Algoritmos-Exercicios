def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            right = mid -1
        else:
            left = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 5)) 
print (binary_search(my_list, 9))
print (binary_search(my_list, 8))       




        