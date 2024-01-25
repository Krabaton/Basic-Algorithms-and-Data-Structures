import heapq

numbers = [5, 8, 4, 2, 9, 1, 7, 6, 3]

# heapq.heapify(numbers)
# print(numbers)

# max heap
# new_numbers = [el * -1 for el in numbers]
# print(new_numbers)
# heapq.heapify(new_numbers)
# print(new_numbers)

heapq.heapify(numbers)
heapq.heappush(numbers, 0)
heapq.heappush(numbers, 42)
print(numbers)

min_el = heapq.heappop(numbers)
print(min_el, numbers)
# -----------------------
new_element = -13
min_el = heapq.heappushpop(numbers, new_element)
print(min_el, numbers)

min_el = heapq.heapreplace(numbers, -4)
print(min_el, numbers)

print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))
print(numbers)
