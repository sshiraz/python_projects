import heapq


def get_kth_smallest(k, heap):
    result = 0
    for i in range(k):
        result = heapq.heappop(heap)
    return result
    

def get_kth_largest(k, heap):
    result = 0
    for i in range(k):
        result = heapq.heappop(heap)
    return -result

minchunk = list()
maxchunk = list()
# List to be k-way merged
minheap_list = [[4, 8, 12],[3, 6, 9],[2, 4, 6],[5, 10, 15], [0, 1, 7, 11, 13, 14]]
print("min heap list is ", minheap_list)


while len(minheap_list) > 0:
    # remove and collect first item from each list
    minchunk.extend(sublist.pop(0) for sublist in minheap_list if sublist)
    # heapq doesn't provide a max heap so make one with negated values
    maxchunk = [-x for x in minchunk]
    # remove empty lists
    minheap_list = list(filter(None, minheap_list))
    # k-way merge 
    heapq.heapify(minchunk)
    heapq.heapify(maxchunk)
    
    
print("After merging into minheap ", list(minchunk))
print("After merging into maxheap ", list(maxchunk))

#def get_kth_largest(k, heap):
print("4th largest item ", get_kth_largest(4, maxchunk))
print("3rd smallest item ", get_kth_smallest(3, minchunk))

