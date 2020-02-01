import random


def toss_coins(count):
    result = []
    for i in range(count):
        result.append(random.randint(0, 1))
    return result


def guess_simple(list1, list2):
    a = random.randint(0, len(list2) - 1)
    b = random.randint(0, len(list1) - 1)
    return list1[b] == list2[b]


def guess_method1(list1, list2):
    a = 0 if list1[0] == 0 else 1
    b = 0 if list2[0] == 0 and list2[1] == 1 else 1
    return list2[a] == list1[b]


def guess_method2(list1, list2):
    a = 0
    for i in range(len(list1) - 1):
        if not list1[a]:
            break
        else:
            a += 1    
    b = 0
    for i in range(len(list2) - 1):
        if not list2[b]:
            break
        else:
            b += 1
    return list2[a] == list1[b]


COUNT = 10
TEST_COUNT = 10000

right_simple = 0
right_method1 = 0
right_method2 = 0
for i in range(TEST_COUNT):
    savva = toss_coins(COUNT)
    pobed = toss_coins(COUNT)    
    if guess_simple(savva, pobed):
        right_simple += 1
    if guess_method1(savva, pobed):
        right_method1 += 1
    if guess_method2(savva, pobed):
        right_method2 += 1

print(right_simple / TEST_COUNT)
print(right_method1 / TEST_COUNT)
print(right_method2 / TEST_COUNT)

