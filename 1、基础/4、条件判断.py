# if 语句

age = 20

if age >= 18:
    print('your age is', age)

age = 15

if age >= 18:
    print('your age is', age)
else:
    print('You are too young')


age = 15

if age >= 18:
    print('your age is', age)

elif age >= 15:
    print('You are too young')

else:
    print('You should go to school.')


# if语句执行有个特点，它是从上往下判断,当某个判断为True 时，后面的if语句会被忽略

age = 15

if age >= 15:
    print('You are too young')              # 输出 You are too young
elif age >= 18:
    print('your age is', age)
else:
    print('You should go to school.')


s = input('birth:')

birth = int(s)

# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数

if birth < 2000:
    print('00前')
else:
    print('00后')