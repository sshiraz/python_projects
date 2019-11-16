import heapq


def get_kth_smallest(k, heap):
    result = list()
    for i in range(k):
        result.append(heapq.heappop(heap))
    return result
    

def get_kth_largest(k, heap):
    result = list()
    for i in range(k):
        result.append(-heapq.heappop(heap))
    return result

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

print("4 largest items ", get_kth_largest(4, maxchunk))
print("3 smallest items ", get_kth_smallest(3, minchunk))

