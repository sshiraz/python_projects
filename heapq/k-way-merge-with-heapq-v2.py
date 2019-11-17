import heapq


heap = list()
# List to be k-way merged
minheap_list = [[4, 8, 12],[3, 6, 9],[2, 4, 6],[5, 10, 15], [0, 1, 7, 11, 13, 14]]
print("min heap list is ", minheap_list)


while len(minheap_list) > 0:
    # remove and collect first item from each list
    heap.extend(sublist.pop(0) for sublist in minheap_list if sublist)
    # remove empty lists
    minheap_list = list(filter(None, minheap_list))
    # k-way merge 
    heapq.heapify(heap)

    
print("After merging into minheap ", list(heap))

#def get_kth_largest(k, heap):
print("4th largest item ", heapq.nlargest(4, heap))
print("3rd smallest item ", heapq.nsmallest(3, heap))

