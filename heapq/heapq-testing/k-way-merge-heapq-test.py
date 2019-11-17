import random
import heapq
import re

from test_cases import *

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

def create_heap(minheap_list):
    minchunk = list()
    maxchunk = list()

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
        return [minchunk, maxchunk]



result = write_tests()
heap_list = list()
for item in result[0]:
    heap_list.append(item)
print("heap list is ", heap_list)
heaps = create_heap(heap_list)
print("length of minheap is ", heaps[0], " and length of maxheap is ", heaps[1])
print("minheap is ",len(heaps[0]))
print("maxheap is ",len(heaps[1]))


print("sorted 10 is ", result[1][1])
for i in range(10):
    print("k is ", i, " and its smallest is ", get_kth_smallest(i+1,heaps[0]))
    print("kth smallest is ", result[1][i+1])
'''
input = list()
sorted_list = list()
rev_sorted_list = list()
with open("input.txt", "r") as infile:
    lines = infile.readlines()
    for line in lines:
        input.append(line[1:-1])

with open("sorted.txt", "w+") as sort_file:
    lines = sort_file.readlines()
    for line in lines:
        sorted_list.append(line)

with open("rev_sorted.txt", "w+") as rev_sort_file:
    lines = rev_sort_file.readlines()
    for line in lines:
        rev_sorted_list.append(line)

arg_list = list()
for item in input:
    arg_list = re.findall(r'\[(.*?)\]',item)
    print("input is ", item)
    #arg_list.append(item)
    print("type of item is ", type(item))
    print("arg list is ", arg_list)
    #print("heap is ", heap)
print("arg list 0 type is ", type(arg_list[0]))

for item in input:
    print("item is ", item)
    print("list item is ", list(item))

for i in range(3):
    heap = create_heap(list(input[i]))
    print(" heap is ", heap)
'''
