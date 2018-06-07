# 使用字典
ab = {'Swaroop' : 'swaroopch@byteofpython.info',
      'Larry' : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org' ,
'Spammer' : 'spammer@hotmail.com'}
print("Larry's address is %s" % ab['Larry'])	
# 使用索引操作符可以增加一个新的键值对
ab['Gundo'] = 'guido@python.org'
print('now the new dictionary is :', ab)
del ab['Spammer']
for name,address in ab.items():
	print('Contact %s at %s' % (name,address))

if 'Swaroop' in ab:   # 注意这个if语句块和上面for...in语句块没关系，即这个没包含在上面的缩进语句里：
		print("\nSwaroop's address is %s" % ab['Swaroop'])