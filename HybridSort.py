import random

# ── Pure Insertion Sort ──────────────────────────────────────
def insertionSort(arr):
    lst = arr.copy()
    comparisons, swaps = 0, 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            comparisons += 1
            lst[j + 1] = lst[j]
            swaps += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        lst[j + 1] = key
    return lst, comparisons, swaps

# ── Pure Selection Sort ──────────────────────────────────────
def selectionSort(arr):
    lst = arr.copy()
    n = len(lst)
    comparisons, swaps = 0, 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if lst[j] < lst[min_idx]:
                min_idx = j
        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
            swaps += 1
    return lst, comparisons, swaps

# ── Hybrid Sort ──────────────────────────────────────────────
def hybridSort(theSeq, threshold=10):
    lst = theSeq.copy()
    n = len(lst)
    comparisons = 0
    swaps = 0

    if n <= threshold:
        # Insertion Sort
        for i in range(1, n):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                comparisons += 1
                lst[j + 1] = lst[j]
                swaps += 1
                j -= 1
            if j >= 0:
                comparisons += 1
            lst[j + 1] = key
    else:
        # Selection Sort
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                comparisons += 1
                if lst[j] < lst[min_idx]:
                    min_idx = j
            if min_idx != i:
                lst[i], lst[min_idx] = lst[min_idx], lst[i]
                swaps += 1

    return lst, comparisons, swaps

# ── Benchmark ────────────────────────────────────────────────
sizes = [50, 100, 500]
random.seed(42)

header = f"{'Size':>6} | {'Algorithm':>18} | {'Comparisons':>12} | {'Swaps':>8} | {'Total Ops':>10}"
separator = "-" * 65

print(header)
print(separator)

for size in sizes:
    data = [random.randint(1, 1000) for _ in range(size)]

    _, ic, iswaps = insertionSort(data)
    _, sc, sswaps = selectionSort(data)
    _, hc, hswaps = hybridSort(data, threshold=10)

    rows = [
        ("Insertion Sort", ic, iswaps),
        ("Selection Sort", sc, sswaps),
        ("Hybrid Sort",    hc, hswaps),
    ]

    for idx, (name, c, s) in enumerate(rows):
        size_label = str(size) if idx == 0 else ""
        print(f"{size_label:>6} | {name:>18} | {c:>12,} | {s:>8,} | {c+s:>10,}")

    print(separator)


# Output:

Size |          Algorithm |  Comparisons |    Swaps |  TotalOps
_________________________________________________________________
50 |        insertionSort |          613 |      563 |      1,176
50 |        selectionSort |        1,225 |       44 |      1,269
50 |           hybridSort |        1,225 |       44 |      1,269
__________________________________________________________________
100 |       insertionSort |        2,526 |    2,426 |      4,952
100 |       selectionSort |        4,950 |       92 |      5,000
100 |          hybridSort |        4,950 |       92 |      5,000
__________________________________________________________________
500 |       insertionSort |       62,813 |   62,313 |    125,126
500 |       selectionSort |      124,750 |      468 |    125,218
500 |          hybridSort |      124,750 |      468 |    125,218
____________________________________________________________________