def countOccurrences(sortedList, target):
    def findLeft(arr, t):
        lo, hi, result = 0, len(arr) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == t:
                result = mid
                hi = mid - 1  # keep searching left
            elif arr[mid] < t:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    def findRight(arr, t):
        lo, hi, result = 0, len(arr) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == t:
                result = mid
                lo = mid + 1  # keep searching right
            elif arr[mid] < t:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    left = findLeft(sortedList, target)
    if left == -1:
        return 0
    right = findRight(sortedList, target)
    return right - left + 1

# Test
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 4))  # → 4
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 5))  # → 0


# Output
4
0