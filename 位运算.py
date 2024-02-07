# 交换
# a 和 b不能指向相同的内存地址
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == '__main__':
    a, b = 1, 1
    print(swap(a, b))
