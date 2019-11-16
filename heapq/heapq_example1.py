import heapq
heap = []
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for v in values:
    heapq.heappush(heap, v)

print("heap is ",heap)    
sorted_list = []

while heap:
    sorted_list.append(heapq.heappop(heap))
    
print("sorted list is ", sorted_list)
print("heap push 0 and pop min", heapq.heappushpop(heap,0))
values_list = values[:]
heapq.heapify(values)
print("Transform ", values_list, " into heap ", values)

merge_list = [[4, 8, 12],[3, 6, 9],[2, 4, 6],[5, 10, 15], [0, 1, 7, 11, 13, 14]]
print("merge list is ", merge_list)
merge_sorted = list(heapq.merge(merge_list[0], merge_list[1], merge_list[2], \
                    merge_list[3], merge_list[4]))
print("After merging into heap ", merge_sorted)
print("4 largest items ", heapq.nlargest(4,merge_sorted))
print("3 smallest items ", heapq.nsmallest(3,merge_sorted))

