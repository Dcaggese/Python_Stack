# countdown

def countdown(num):

    list = []
    for x in range(num,-1,-1):
        list.append(x)

    return list

print(countdown(5))

# Print and Return

def print_and_return(value1,value2):
    print(value1)
    return value2

print(print_and_return(1,2))

# First Plus Length

def first_plus_length(list):
    return list[0] + list[len(list)-1]

print (first_plus_length([1,2,3,4,5]))

# Values Greater than Second

def values_greater_than_second(list):
    new_list = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))

# This length, That Value

def length_value(length,value):
    list = []
    for i in range(0,length):
        list.append(value)
    return list
print(length_value(4,7))