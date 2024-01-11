import timeit
import random

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quicksort
from shell_sort import shell_sort
from radix_sort import radix_sort

if __name__ == '__main__':
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]

    # time_small_bubble = timeit.timeit(lambda: bubble_sort(data_small[:]), number=10)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time_small_selection = timeit.timeit(lambda: selection_sort(data_small[:]), number=10)
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_small_quicksort = timeit.timeit(lambda: quicksort(data_small[:]), number=10)
    time_small_shell = timeit.timeit(lambda: shell_sort(data_small[:]), number=10)
    time_small_radix = timeit.timeit(lambda: radix_sort(data_small[:]), number=10)
    time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=10)
    time_small_timsort_s = timeit.timeit(lambda: data_small[:].sort(), number=10)

    # time_medium_bubble = timeit.timeit(lambda: bubble_sort(data_medium[:]), number=10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time_medium_selection = timeit.timeit(lambda: selection_sort(data_medium[:]), number=10)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_medium_quicksort = timeit.timeit(lambda: quicksort(data_medium[:]), number=10)
    time_medium_shell = timeit.timeit(lambda: shell_sort(data_medium[:]), number=10)
    time_medium_radix = timeit.timeit(lambda: radix_sort(data_medium[:]), number=10)
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=10)
    time_medium_timsort_s = timeit.timeit(lambda: data_medium[:].sort(), number=10)

    print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
    # print(f"{'| Bubble sort': <20} | {time_small_bubble:<20.5f} | {time_medium_bubble:<20.5f}")
    print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f}")
    print(f"{'| Selection sort': <20} | {time_small_selection:<20.5f} | {time_medium_selection:<20.5f}")
    print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f}")
    print(f"{'| Quicksort': <20} | {time_small_quicksort:<20.5f} | {time_medium_quicksort:<20.5f}")
    print(f"{'| Shell sort': <20} | {time_small_shell:<20.5f} | {time_medium_shell:<20.5f}")
    print(f"{'| Radix sort': <20} | {time_small_radix:<20.5f} | {time_medium_radix:<20.5f}")
    print(f"{'| Tim sort sorted': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f}")
    print(f"{'| Tim sort sort': <20} | {time_small_timsort_s:<20.5f} | {time_medium_timsort_s:<20.5f}")
