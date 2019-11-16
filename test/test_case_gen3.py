import random


def get_test_input(_min, _max, max_list_len, _type):
    test_list = list()
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

    test_item = []

    for i in range(_min, _max):
        test_item.append(i)
        test_list.append(list(test_item))
        if len(test_item) > max_list_len:
            break

    test_item = []

    
    for i in range(_max, _min, -1):
        test_item.append(i)
        test_list.append(list(test_item))
        if len(test_item) > max_list_len:
            break

    test_item = []
    

    for i in range(max_list_len + 1):
        num = i ** 2
        if num <= _max:
            test_item.append(num)
            test_list.append(list(test_item))
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])

    test_list.append(test_item)
    test_item = []

    for i in range(max_list_len + 1):
        num = i ** 3
        if num <= _max:
            test_item.append(num)
            test_list.append(list(test_item))
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
    test_item = []

    for i in range(max_list_len + 1):
        test_item.append(0)
        test_list.append(test_item)
    test_item = []

    for i in range(max_list_len + 1):
        num = i * 2
        if num <= _max:
            test_item.append(num)
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
        
    test_list.append(test_item)
    test_item = []

    for i in range(max_list_len + 1):
        num = i * 3
        if num <= _max:
            test_item.append(num)
        else:
            break

    for j in range(i, max_list_len + 1):
        test_item.append(test_item[j % i])
        
    test_list.append(test_item)
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
    print("number of lists is ", len(test_list))


get_test_input(-10, 20, 30, "INT")
