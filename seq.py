shoplist = ['apple','mango','carrot','banana']
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item start to end is', shoplist[:])

# 在字符串中使用切片
name = 'Swaroop'
print('characters 1 to 3 is', name[1:3])
print('characters 1 to -1 is', name[1:-1])


# 对象与参考
shoplist = ['apple','mango','carrot','banana']
mylist = shoplist
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
mylist = shoplist[:]
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)