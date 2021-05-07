def temperature(value):
    if (value > 25):
        return 'Hot'
    elif (value > 15 and value <= 35):
        return 'Warm'
    else:
        return 'Cold'


user_input = int(input("Enter the temperature : "))
print(temperature(user_input))


# two

def foo(name):
    return 'Hi %s' % name


username = input('Enter the name')
print(foo(username))

# For Loop

phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print("00%s" % value[1:])


#

def foo(list_data):
    return [temp for temp in list_data if temp > 0 ]
    
def foo(user_list):
    return [temp if not isinstance(temp,str) else 0 for temp in user_list]