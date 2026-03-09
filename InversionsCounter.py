import random
import time

# ── a) Brute Force O(n²) ─────────────────────────────────────
def countInversionsNaive(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count


# ── b) Merge Sort O(n log n) ─────────────────────────────────
def countInversionsSmart(arr):
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst, 0

        mid = len(lst) // 2
        left, left_inv  = merge_sort(lst[:mid])
        right, right_inv = merge_sort(lst[mid:])

        merged = []
        inversions = left_inv + right_inv
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                # semua elemen left[i:] lebih besar dari right[j]
                inversions += len(left) - i
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged, inversions

    _, total = merge_sort(arr)
    return total


# ── Verifikasi hasil sama ─────────────────────────────────────
print("=" * 50)
print("VERIFIKASI HASIL")
print("=" * 50)

test_cases = [
    [2, 4, 1, 3, 5],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [3, 1, 2],
]

for tc in test_cases:
    naive  = countInversionsNaive(tc)
    smart  = countInversionsSmart(tc)
    status = "OK" if naive == smart else "MISMATCH"
    print("Array  :", tc)
    print("Naive  :", naive)
    print("Smart  :", smart)
    print("Status :", status)
    print("-" * 30)


# ── Benchmark waktu eksekusi ─────────────────────────────────
print()
print("=" * 50)
print("BENCHMARK WAKTU EKSEKUSI")
print("=" * 50)
print(f"{'Size':>8} | {'Naive (s)':>12} | {'Smart (s)':>12} | {'Speedup':>10}")
print("-" * 50)

random.seed(42)
sizes = [1000, 5000, 10000]

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]

    start = time.time()
    countInversionsNaive(data)
    naive_time = time.time() - start

    start = time.time()
    countInversionsSmart(data)
    smart_time = time.time() - start

    speedup = naive_time / smart_time if smart_time > 0 else 0
    print(f"{size:>8} | {naive_time:>12.4f} | {smart_time:>12.4f} | {speedup:>9.1f}x")


# Output:
__________________________________________________
VERIFIKASI_HASIL
__________________________________________________
Array  : [2, 4, 1, 3, 5]
Naive  : 3
Smart  : 3
Status : OK
_____________________________
Array  : [5, 4, 3, 2, 1]
Naive  : 10
Smart  : 10
Status : OK
_____________________________
Array  : [1, 2, 3, 4, 5]
Naive  : 0
Smart  : 0
Status : OK
_____________________________
Array  : [3, 1, 2]
Naive  : 2
Smart  : 2
Status : OK
______________________________

_________________________________________________
BENCHMARK_WAKTU_EKSEKUSI
_________________________________________________
Size |    Naive (s) |    Smart (s) |    Speedup
__________________________________________________
1000 |       0.0469 |       0.0012 |      39
5000 |       1.1800 |       0.0071 |     166
10000|       4.7200 |       0.0153 |     308