import random
import heapq


def get_test_input(_min, _max, max_list_len, _type):
    test_list = list()
    sorted_list = list()
    rev_sorted_list = list()
    test_item = list()
    #sample_list = [0, 1, 2, 5, 10, 50, 100, 1000, 10000]
    sample_list = [0, 1, 2, 5, 10, 15, 20, 25, 30]

    test_list.append(list())
    sorted_list.append(list())
    rev_sorted_list.append(list())
    rand = 0
    prime = 0
    value = 0

    # Random number test case
    for val in sample_list:
        for i in range(val+1):
            rand = random.randrange(_min, _max + 1)
            test_item.append(rand)
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
        test_item = []

    for val in sample_list:
        for i in range(val+1):
            test_item.append(i)
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
        if len(test_item) > max_list_len:
            break
        test_item = []

    for val in sample_list:
        for i in range(val,-1,1):
            test_item.append(i)
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
        if len(test_item) > max_list_len:
            break
        test_item = []

    for val in sample_list:
        for i in range(val+1):
            num = i ** 2
            if num <= _max:
                test_item.append(num)
            else:
                break
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
        test_item = []

    for val in sample_list:
        for i in range(val + 1):
            num = i ** 3
            if num <= _max:
                test_item.append(num)
            else:
                break
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
        test_item = []

    for val in sample_list:
        for i in range(val + 1):
            num = i ** 4
            if num <= _max:
                test_item.append(num)
                test_list.append(list(test_item))
                sorted_list.append(sorted(list(test_item)))
                rev_sorted_list.append(sorted(list(test_item), reverse=True))
            else:
                break
        test_item = []

    if _min < 0:

        for val in sample_list:
            for i in range(val + 1):
                rand = random.randrange(_min, 0)
                test_item.append(rand)
            test_list.append(test_item)
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
            test_item = []

    for val in sample_list:
        for i in range(val + 1):
            test_item.append(0)
            test_list.append(test_item)
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
        test_item = []

    for val in sample_list:
        for i in range(val + 1):
            num = i * 2
            if num <= _max:
                test_item.append(num)
                sorted_list.append(sorted(list(test_item)))
                rev_sorted_list.append(sorted(list(test_item), reverse=True))
            else:
                break
        test_item = []

    for val in sample_list:
        for i in range(val + 1):
            num = i * 3
            if num <= _max:
                test_item.append(num)
                test_list.append(test_item)
                sorted_list.append(sorted(list(test_item)))
                rev_sorted_list.append(sorted(list(test_item), reverse=True))
        else:
            break
        test_item = []

    for val in sample_list:
        for i in range(val + 1):
            num = i * 4
            if num <= _max:
                test_item.append(num)
            else:
                break
        test_item = []

    test_item = []

    print("number of lists is ", len(test_list))
    for item in test_list:
        print("item is ", item)
    print("number of lists is ", len(test_list))
    return [test_list, sorted_list, rev_sorted_list]


def write_tests():
    result = get_test_input(-10, 20, 30, "INT")
    with open("input.txt", "w") as outfile:
        for line in result[0]:
            outfile.write(str(line))
            outfile.write("\n")
    outfile.close()

    with open("sorted.txt", "w") as sort_file:
        for line in result[1]:
            sort_file.write(str(line))
            sort_file.write("\n")
    sort_file.close()

    with open("rev_sorted.txt", "w") as rev_sort_file:
        for line in result[2]:
            rev_sort_file.write(str(line))
            rev_sort_file.write("\n")
    rev_sort_file.close()
    return result

#write_tests()
