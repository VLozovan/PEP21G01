# variables

number_3 = '3'
print(number_3)
number_three = 3
print(number_three)

# types

response = type(number_3)
print(response)

response = type(number_three)
print(response)

# print(type(3))
# print(type('3'))

# integers

var1 = 123
result =type(var1)
print('This is an integer:', result)

# integer base

bin_number = 0b10
print(bin_number)

oct_number = 0o10
print(oct_number)

hex_number = 0x10
print(hex_number)

# integer operations

print('Sum of 2+8:', bin_number + oct_number)

# add method

print('Sum of 2+8:', bin_number.__add__(oct_number))

# print('Sum of 2+8:', oct_number.__add__(bin_number))

print("Dif of 8-2 is:", oct_number - bin_number)
print("Dif of 8-2 is:", oct_number.__sub__(bin_number))

# mul method

print('Multiplication 2 * 8:', bin_number.__mul__(oct_number))

print("Multiplication 3 * 3 * 3:", (3).__mul__(3).__mul__(3))
print("Multiplication 3 * 3 * 3:", 3 * 3 * 3)
print("Multiplication 3 * 3 * 3:", number_three.__mul__(number_three.__mul__(number_three)))

# raise to power

print('Power of:')
number_3 = 3
print(number_3.__pow__(3))
print(pow(number_3, 3))
print(number_3 ** 3)

# division

result = number_3 / 3
print(result)
print(type(result))
print('True div:', number_3.__truediv__(3))

# ex: using methods

a = 3
b = 4
c = 5

_4ac = (4).__mul__(a.__mul__(c))
b_sqr = b.__pow__(2)
sqr_result = b_sqr.__sub__(_4ac)
sqrt_result = pow(sqr_result, (1).__truediv__(2))
minus_b = (0).__sub__(b)
# div_up = minus_b.__add__(sqrt_result)
div_up = sqrt_result.__add__(minus_b)
div_down = (2).__mul__(a)
result = div_up.__truediv__(div_down)
print(result)

# strings

string1 = 'My String1\nThis is a new line'
print(string1)
string2 = "My String2"
print(string2)
string3 = '''My String3
This is a new line
This is another new line'''
print(string3)

print(type(string1), type(string2), type(string3))

# methods

print(string1 + string2)
print(string1.__add__(string2))

# ex: write: This is my code 100 times

string12 = 'This is my code\n'
print(string12.__mul__(100))
print((100).__mul__(string12)) #this is not implemented so it will do String12.__mul__(100)

# string types

formatable_string = f'Start: {string1} End: {string2}'
print(formatable_string)

#ex:

nume = 'Ab'
prenume = 'Cd'
declaratie = 'qwerty'
formatable_string = f'Subsemnatul {nume} {prenume}\nDeclar ca {declaratie}'
print(formatable_string)

raw_string = r'1\nThere is no new line\n2'
print(raw_string)

string1 = 'My string: {}'
result = string1.format('String Name')
print(result)

string2 = 'Subsemnatul {} {}\nDeclar ca {}'
result = string2.format('Ab', 'Cd', 'qwerty')
print(result)

result = string1.replace('{', '(')
result = result.replace('}', ')')
print(result)


