def mergeThreeSortedLists(listA, listB, listC):
    result = []
    i, j, k = 0, 0, 0

    while i < len(listA) and j < len(listB) and k < len(listC):
        a, b, c = listA[i], listB[j], listC[k]
        if a <= b and a <= c:
            result.append(a)
            i += 1
        elif b <= a and b <= c:
            result.append(b)
            j += 1
        else:
            result.append(c)
            k += 1

    while i < len(listA) and j < len(listB):
        if listA[i] <= listB[j]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listB[j])
            j += 1

    while i < len(listA) and k < len(listC):
        if listA[i] <= listC[k]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listC[k])
            k += 1

    while j < len(listB) and k < len(listC):
        if listB[j] <= listC[k]:
            result.append(listB[j])
            j += 1
        else:
            result.append(listC[k])
            k += 1

    while i < len(listA):
        result.append(listA[i])
        i += 1

    while j < len(listB):
        result.append(listB[j])
        j += 1

    while k < len(listC):
        result.append(listC[k])
        k += 1

    return result


# Test
print(mergeThreeSortedLists([1, 5, 9], [2, 6, 10], [3, 4, 7]))
print(mergeThreeSortedLists([1, 4, 7], [2, 5, 8], [3, 6, 9]))
print(mergeThreeSortedLists([], [1, 3], [2, 4]))
print(mergeThreeSortedLists([5], [1, 2], [3, 4, 6]))


# Output:

[1, 2, 3, 4, 5, 6, 7, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]