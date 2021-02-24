# slice

string1 = 'My string'
result = string1[8]
print(result)

result = string1[0:4]
print(result)

result = string1[4:]
print(result)

result = string1[4:8]
print(result)

# T E X T
# 0 1 2 3
#-4-3-2-1

result = string1[4:-1]
print(result)

result = string1[-5:-1]
print(result)

result = string1[0:8:2]
print(result)

encode = 'My test to encode'

result = encode[::-1]
print(result)
result = result[::-1]
print(result)

result = encode[5:] + encode[0:5]
print(result)

result = result[-5:] + result[:-5]
print(result)

# chr, ord

print(chr(100))
print(ord('d'))

print(chr(33))
print(ord('!'))

encode = 'abc'
result = chr(ord(encode[0]) + 1) + chr(ord(encode[1]) + 1) + chr(ord(encode[2]) + 1)
print(result)

# cast

print(ord('1'))
print(int('1'))
print(type(int('112')))

# ex: time difference

start_time = '22:30'
end_time = "30:10"
start_time_m = int(start_time[0:2])
start_time_s = int(start_time[3:])
start_time_conv = 60 * start_time_m + start_time_s
end_time_m = int(end_time[0:2])
end_time_s = int(end_time[3:])
end_time_conv = 60 * end_time_m + end_time_s
diff = end_time_conv - start_time_conv
print(diff)

# input

# my_input = input('Enter text here:')
# print('You typed:', my_input)
#
# start_time =input("Start time: ")
# end_time = input("End time:")
# start_time_m = int(start_time[0:2])
# start_time_s = int(start_time[3:])
# start_time_conv = 60 * start_time_m + start_time_s
# end_time_m = int(end_time[0:2])
# end_time_s = int(end_time[3:])
# end_time_conv = 60 * end_time_m + end_time_s
# diff = end_time_conv - start_time_conv
# print(diff)
#
# my_input = float(input('Enter text here:'))
# print('You typed:', my_input)
#
# my_input = complex(input('Enter text here:'))
# print('You typed:', my_input)

# None

print_result = print('This is an example')
print('Result is:', print_result)
print(type(print_result))

# operations

# var_1=float(input("Primul numar: "))
# var_2=float(input("Al doilea numar: "))
# print("Primul numar este mai mic:",var_1<var_2)
# print("Primul numar este mai mare",var_1>var_2)
# print("egalitate:",var_1==var_2)
# print("diferenta:",var_1!=var_2)

print('Greater or equal 1 >= 0', (1).__ge__(0))
print('abc less than abd:', 'abc'.__lt__('abd'))

# a = str(input('a = '))
# b = str(input('b = '))
# print('a > b: ',a.__gt__(b))
# print('a < b: ',a.__lt__(b))
# print('a >= b: ',a.__ge__(b))
# print('a <= b: ',a.__le__(b))
# print('a == b: ',a.__eq__(b))
# print('a != b: ',a.__ne__(b))

var1 = 'abc'
var2 = 'abc'
print('=', var1 == var2)
print('Is', var1 is var2)
