## Index
1. [Space  Complexity](#space-complexity)
1. [Time Complexity](#time-complexity)


## Space Complexity
Space complexity refers to the amount of memory space required by an algorithm as a function of the input size. Here are the main types of space complexity:

1. Constant Space Complexity (O(1))  
`Description`: The algorithm uses a fixed amount of space regardless of the input size.  
`Example`: Accessing a specific element in an array, performing arithmetic operations.  
    `Example`: Swapping two variables.
    ```python
    def swap(a, b):
        a, b = b, a
        return a, b
    ```
2. Logarithmic Space Complexity (O(log n))  
`Description`: The space required grows logarithmically with the input size.  
`Example`: Binary search in a sorted array.  
`Example`: Binary search.
    ```python
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    ```
3. Linear Space Complexity (O(n))  
`Description`: The space required grows linearly with the input size.
`Example`: Storing input data in an array, simple recursive algorithms without memoization.
`Example`: Copying an array.
    ```python

    def copy_array(arr):
        return arr[:]
    ```
4. Linearithmic Space Complexity (O(n log n))  
`Description`: The space required grows in proportion to 
𝑛
log𝑛
nlogn.  
`Example`: Merge sort, when considering the space required for temporary arrays.  
`Example`: Merge sort.
    ```python
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
    ```

5. Quadratic Space Complexity (O(n^2))  
`Description`: The space required grows quadratically with the input size.  
`Example`: Storing a matrix of size 𝑛×𝑛 n×n.  
`Example`: Dynamic programming solution for the longest common subsequence.
    ```python
    def lcs(X, Y):
        m = len(X)
        n = len(Y)
        L = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])

        return L[m][n]
    ```
6. Cubic Space Complexity (O(n^3))  
`Description`: The space required grows cubically with the input size.
`Example`: Storing a three-dimensional table.  
`Example`: 3D matrix initialization.
    ```python
    def init_3d_matrix(n):
        return [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]  
    ```

7. Polynomial Space Complexity (O(n^k))  
`Description`: The space required grows polynomially with the input size, where 𝑘 is a constant.  
`Example`: Dynamic programming algorithms with multiple dimensions.  
`Example`: k-dimensional dynamic programming table for a generalized problem.
    ```python
    def poly_dp(n, k):
        table = [[0] * (n + 1) for _ in range(k + 1)]
        # Fill the table based on the problem's recurrence relation
        return table
    ```
8. Exponential Space Complexity (O(2^n))  
`Description`: The space required grows exponentially with the input size.  
`Example`: Certain recursive algorithms without memoization, such as generating all subsets of a set.
`Example`: Generating all subsets of a set.
    ```python
    def generate_subsets(s):
        if len(s) == 0:
            return [[]]
        subsets = generate_subsets(s[1:])
        return subsets + [[s[0]] + subset for subset in subsets]
    ```
9. Factorial Space Complexity (O(n!))  
`Description`: The space required grows factorially with the input size.  
`Example`: Generating all permutations of a set.  
`Example`: Generating all permutations of a set.
    ```python
    def permute(s):
        if len(s) == 1:
            return [s]
        permutations = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                permutations.append(s[i] + p)
        return permutations
    ```

10. Super-Constant but Sub-Linear Space Complexity  
`Description`: The space required grows more than constant space but less than linear space.  
`Example`: Algorithms that require additional space for logarithmic factors or polylogarithmic space, such as O((log n)^k).  
`Example`: Example of an algorithm requiring logarithmic factors of space.
    ```python
    import math

    def super_constant_space(n):
        # Space complexity: O(log n)
        levels = int(math.log2(n))
        space = [0] * levels
        return space
    ```