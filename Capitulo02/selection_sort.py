#Function to find the index of the smallest element
def find_smallest(arr):
    smallest = arr[0]   #stores 1st item as the smallest value
    smallest_index = 0   #stores the index of the smallest value

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#Main Selection Sort function
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):   
        #Finds the smallest elemento in the array
        smallest = find_smallest(arr)  
        # ... pops it from the old array and appends to the new array
        new_arr.append(arr.pop(smallest))
    
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))
