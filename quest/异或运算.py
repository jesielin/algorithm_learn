
#数组中有一种数出现了奇数次，其他数出现了偶数次，求这个奇数次的数，要求时间复杂度是O(N)

def quest1():
    L = [1,1,2,2,3,3,4,4,4]

    eor = 0

    for i in L:
        eor ^= i

    print(i)

#数组中有两种不同的数出现了奇数次，其他数出现了偶数次，求这两个奇数次的数，要求时间复杂度是O(N)
def quest2():
    L = [1,1,2,2,3,3,4,4,4,5,5,5]

    #全部异或求出a^b
    eor = 0
    for i in L:
        eor ^= i

    #eor一定不为0，所以某一位是1，取出最右边的1
    right_one = eor & (~eor +1)
    a = 0
    #求出a或者b
    for i in L:
        if i&right_one != 0:
            a ^= i

    print(a,a^eor)

if __name__ == '__main__':
    quest1()
    quest2()