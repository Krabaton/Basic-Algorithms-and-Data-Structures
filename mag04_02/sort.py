import heapq


def heap_sort(nums: list, descending: bool = False) -> list:  # O(n log n)
    sign = -1 if descending else 1
    iterable = nums[:]  # O(n)
    iterable = [sign * num for num in iterable]  # O(n)
    heapq.heapify(iterable)
    return [sign * heapq.heappop(iterable) for _ in range(len(iterable))]  # O(n log n)


def heap_sort_modify(nums: list, descending: bool = False) -> list:  # O(n log n)
    iterable = nums[:]  # O(n)
    heapq.heapify(iterable)
    result = [heapq.heappop(iterable) for _ in range(len(iterable))]  # O(n log n)
    return result if not descending else result[::-1]


if __name__ == "__main__":
    print("Heap sort")
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(nums)
    print(heap_sort(nums))
    print(heap_sort(nums, True))

    print(heap_sort_modify(nums))
    print(heap_sort_modify(nums, True))

