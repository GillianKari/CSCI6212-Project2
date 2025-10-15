import random, time

def find_max_in_rotated_array(A):
    """Return the maximum element in a rotated sorted array using O(log n) search."""
    low, high = 0, len(A) - 1

    # If array is not rotated
    if A[low] < A[high]:
        return A[high]

    while low <= high:
        mid = (low + high) // 2

        # Pivot condition
        if mid < len(A) - 1 and A[mid] > A[mid + 1]:
            return A[mid]
        elif A[mid] >= A[low]:
            low = mid + 1
        else:
            high = mid - 1

# --- Runtime Simulation ---
def simulate_runtime(n):
    """Generate a rotated sorted array of size n and measure search time."""
    arr = sorted(random.sample(range(1, n*5), n))
    # Random rotation
    k = random.randint(0, n - 1)
    rotated = arr[k:] + arr[:k]

    start = time.time()
    _ = find_max_in_rotated_array(rotated)
    end = time.time()
    return end - start

# Test for multiple input sizes
n_values = [10**3, 5*10**3, 10**4, 5*10**4, 10**5, 5*10**5]
for n in n_values:
    t = simulate_runtime(n)
    print(f"n={n:6d}, time={t:.8f}s, normalized={t / (math.log2(n)):.6e}")
