num1 = 42 #variable declaration, integer
num2 = 2.3 #variable declaration, float
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple, initialize
print(type(fruit)) #print function, type check
print(pizza_toppings[1])#print function, accessing list value
pizza_toppings.append('Mushrooms')#adding list value
print(person['name'])# print function, accessing key value
person['name'] = 'George' #changing key value
person['eye_color'] = 'blue' #adding key value pair
print(fruit[2]) # print function, accessing tuple value

if num1 > 45: #if conditional
    print("It's greater")#print function, string
else: # else conditonal
    print("It's lower") #print function, string

if len(string) < 5: # if conditional, length
    print("It's a short word!") # print function, string
elif len(string) > 15: # else if conditional, length
    print("It's a long word!")# print function, string
else:# else condtional
    print("Just right!") #print function, string

for x in range(5): # for loop
    print(x) # print function
for x in range(2,5): # for loop
    print(x) # print function
for x in range(2,10,3):# for loop
    print(x)# print function
x = 0 # variable declaration, integer
while(x < 5): #while loop
    print(x)# print function
    x += 1 #adding to variable

pizza_toppings.pop() # delete last list value
pizza_toppings.pop(1) # delete 2nd list value

print(person) # print function
person.pop('eye_color') #delete key value pair
print(person) # print function

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # if conditional
        continue #continues if true
    print('After 1st if statement')#print function
    if topping == 'Olives':#if conditional
        break # break if true

def print_hello_ten_times(): #function declaration
    for num in range(10):# for loop
        print('Hello') # print function

print_hello_ten_times() # print function

def print_hello_x_times(x): #function declarartion
    for num in range(x): # for loop
        print('Hello') # print function

print_hello_x_times(4) # print function

def print_hello_x_or_ten_times(x = 10): # function declaration
    for num in range(x): # for loop
        print('Hello') # print function

print_hello_x_or_ten_times()# print function
print_hello_x_or_ten_times(4)# print function
