import random
import sympy

def get_test_input(_min, _max, max_list_len, _type):
    test_list = list()
    test_item = list()
    test_item2 = list()
    test_item3 = list()
    test_item4 = list()

    test_list.append(list())
    rand = 0
    prime = 0
    prime_n = 0
    prev_prime = 0
    next_prime = 0

    # Random number test case
    for i in range(max_list_len+1):
        rand = random.randrange(_min, _max+1)
        test_item.append(rand)
    
    test_list.append(test_item)
    test_item = []
    
    for i in range(max_list_len+1):
        num = i**2
        if num <= _max:
            test_item.append(num)
        else:
            break
    
    for j in range(i, max_list_len+1):
        test_item.append(test_item[j%i])

    test_list.append(test_item)

    test_item = []
    

    for i in range(max_list_len+1):
        num = i**3
        if num <= _max:
            test_item.append(num)
        else:
            break
    
    for j in range(i, max_list_len+1):
        test_item.append(test_item[j%i])
        
    test_list.append(test_item)
    test_item = []


    for i in range(max_list_len+1):
        num = i**4
        if num <= _max:
            test_item.append(num)
        else:
            break
    
    for j in range(i, max_list_len+1):
        test_item.append(test_item[j%i])
    test_list.append(test_item)
    test_item = []
    
    if _min < 0:
        
        for i in range(max_list_len+1):
            rand = random.randrange(_min, 0)
            test_item.append(rand)
    test_list.append(test_item)
    test_item = []
    
    for i in range(max_list_len+1):
        test_item.append(0)
    test_list.append(test_item)
    test_item = []

    
    for i in range(max_list_len+1):
        prime = sympy.primerange(_min, _max+1)
        prime_n = sympy.prime(n)
        prev_prime = sympy.prevprime(n)
        next_prime = sympy.nextprime(n)
        test_item.append(prime)
        test_item2.append(prime_n)
        test_item3.append(prev_prime)
        test_item4.append(next_prime)

    test_list.append(test_item)
    test_list.append(test_item2)
    test_list.append(test_item3)
    test_list.append(test_item4)
    
    test_item = []
    test_item2 = []
    test_item3 = []
    test_item4 = []

        
    for item in test_list:
        print("test_list", item)
