import random


def get_test_input(_min, _max, max_list_len, _type):
    test_list = list()
    sorted_list = list()
    rev_sorted_list = list()
    test_item = list()

    test_list.append(list())
    rand = 0
    prime = 0
    value = 0

    # Random number test case
    for i in range(max_list_len + 1):
        rand = random.randrange(_min, _max + 1)
        test_item.append(rand)
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))

    test_item = []

    for i in range(_min, _max):
        test_item.append(i)
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))

        if len(test_item) > max_list_len:
            break

    test_item = []

    
    for i in range(_max, _min, -1):
        test_item.append(i)
        test_list.append(list(test_item))
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
        if len(test_item) > max_list_len:
            break

    test_item = []
    

    for i in range(max_list_len + 1):
        num = i ** 2
        if num <= _max:
            test_item.append(num)
            test_list.append(list(test_item))
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
        test_list.append(test_item)
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))

    test_item = []

    for i in range(max_list_len + 1):
        num = i ** 3
        if num <= _max:
            test_item.append(num)
            test_list.append(list(test_item))
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])

    test_list.append(test_item)
    test_item = []

    for i in range(max_list_len + 1):
        num = i ** 4
        if num <= _max:
            test_item.append(num)
            test_list.append(list(test_item))
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
    test_list.append(test_item)
    test_item = []

    if _min < 0:

        for i in range(max_list_len + 1):
            rand = random.randrange(_min, 0)
            test_item.append(rand)
            test_list.append(test_item)
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
    test_item = []

    for i in range(max_list_len + 1):
        test_item.append(0)
        test_list.append(test_item)
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
    test_item = []

    for i in range(max_list_len + 1):
        num = i * 2
        if num <= _max:
            test_item.append(num)
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
        test_list.append(test_item)
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))
    test_item = []

    for i in range(max_list_len + 1):
        num = i * 3
        if num <= _max:
            test_item.append(num)
            test_list.append(test_item)
            sorted_list.append(sorted(list(test_item)))
            rev_sorted_list.append(sorted(list(test_item), reverse=True))

        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
        test_list.append(test_item)
        sorted_list.append(sorted(list(test_item)))
        rev_sorted_list.append(sorted(list(test_item), reverse=True))

    test_item = []

    for i in range(max_list_len + 1):
        num = i * 4
        if num <= _max:
            test_item.append(num)
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
        
    test_list.append(test_item)
    test_item = []


    for item in test_list:
        print("test_list", item)
    
    for item in sorted_list:
        print("sorted ", item)
    for item in rev_sorted_list:
        print("rev sorted ", item)

    print("number of lists is ", len(test_list))

get_test_input(-10, 20, 30, "INT")
