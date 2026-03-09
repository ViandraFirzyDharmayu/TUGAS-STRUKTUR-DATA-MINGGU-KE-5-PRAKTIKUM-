def bubbleSort(arr):
    lst = arr.copy()
    n = len(lst)
    total_comparisons = 0
    total_swaps = 0
    passes_used = 0

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            total_comparisons += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                total_swaps += 1
                swapped = True

        passes_used += 1
        print(f"  Pass {passes_used}: {lst}")

        # Early termination — tidak ada swap berarti sudah terurut
        if not swapped:
            break

    return (lst, total_comparisons, total_swaps, passes_used)


# ── Test 1 ──────────────────────────────────────────
print("Input: [5, 1, 4, 2, 8]")
result = bubbleSort([5, 1, 4, 2, 8])
print(f"  sorted_list       : {result[0]}")
print(f"  total_comparisons : {result[1]}")
print(f"  total_swaps       : {result[2]}")
print(f"  passes_used       : {result[3]}")

print()

# ── Test 2 ──────────────────────────────────────────
print("Input: [1, 2, 3, 4, 5]")
result = bubbleSort([1, 2, 3, 4, 5])
print(f"  sorted_list       : {result[0]}")
print(f"  total_comparisons : {result[1]}")
print(f"  total_swaps       : {result[2]}")
print(f"  passes_used       : {result[3]}")

# Output:

Input: [5, 1, 4, 2, 8]
pass1: [1, 4, 2, 5, 8]
pass2: [1, 2, 4, 5, 8]
pass3: [1, 2, 4, 5, 8]
sorted_list       : [1, 2, 4, 5, 8]
total_comparisons : 9
total_swaps       : 4
passes_used       : 3  # ← butuh 3 pass karena ada banyak elemen salah posisi

Input: [1, 2, 3, 4, 5]
pass1: [1, 2, 3, 4, 5]
sorted_list       : [1, 2, 3, 4, 5]
total_comparisons : 4
total_swaps       : 0
passes_used       : 1   
input  # <- cukup 1 pass karena sudah terurut