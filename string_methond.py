name = 'Swaroop'
if name.startswith('Swa'):
	print('Yes,the string starts with "Swa"')
if 'a' in name:
	print('Yes, it contains the string "a"')
	print("Yes, it contains the string 'a'")    # 这样写不对～～
if name.find('war') != -1:                     # 不等于是：!= 而不是! =（中间没有空格）
	print('yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))  # 注：print后面括号中没有引号和双引号