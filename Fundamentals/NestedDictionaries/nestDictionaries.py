# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]

# for i in range(0,len(x)):
#     for j in range(0,len(x[i])):
#         if x[i][j] == 10:
#             x[i][j] = 15

# print(x)

# # Change the last_name of the first student from 'Jordan' to 'Bryant'

# students[0]["last_name"] = "Byrant"

# print(students)

# # In the sports_directory, change 'Messi' to 'Andres'

# sports_directory["soccer"][0] = "Andres"

# print(sports_directory)

# # Change the value 20 in z to 30

# z[0]['y'] = 30

# print(z)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students_list):
    for student in students_list:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")


iterateDictionary(students) 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def iterateDictionary2(key_word,students_list):
    for student in students_list:
        print(student[key_word])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for key_word in dictionary:
        print(f"{len(dictionary[key_word])} {key_word.upper()}")
        for value in range(len(dictionary[key_word])):
            print(dictionary[key_word][value])

printInfo(dojo)

