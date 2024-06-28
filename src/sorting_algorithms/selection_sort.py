def selection_sort(arr):
    n = len(arr) # SC: O(1) TC: O(1)
    for i in range(n): # TC: O(n)
        min_idx = i # SC: O(1)
        for j in range(i+1, n): 
            '''
            CASE:
            i=0 j=1
            i=1 j=2
            '''
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Sorted array is:", selection_sort(arr))
