from functools import reduce

L = reduce(lambda x, y: x + y, [[i] * i for i in range(1, 6)])
print(L)


# def num():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in num()])

# """
# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# """
#
# list1 = [1, 2, 3, 4, 5]
#
#
# def test(x):
#     return x ** 2
#
#
# res = map(test, list1)
# res = [i for i in res if i > 10]
# print(res)
