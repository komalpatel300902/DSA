def bubble_sort(arr):
    n = len(arr) # SC: O(1)  TC: O(1)
    for i in range(n): # TC: O(n)
        for j in range(0, n-i-1): 
            '''
            CASE:
            n = 5
            i=0 j=[1,2,3,4] | n-1
            i=1 j=[1,2,3] | n-2
            i=2 j=[1,2] | n-3 
            i=3 j=[1] | n-4 -> 1
            exp : n-1, n-2 + n-3 , n-4 , n-5 ... 1
            '''
            if arr[j] > arr[j+1]: # TC: O(1)
                arr[j], arr[j+1] = arr[j+1], arr[j] #TC: O(1)
    return arr #TC: O(1)

'''
Space Complexity : O(1)
Time Comlexity: sn = n(2a+(n-1)d)/2
sn = (n-1)[2 + n-2]/2 => [n**2 -n]/2 => O(n**2)
'''

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array is:", bubble_sort(arr))

