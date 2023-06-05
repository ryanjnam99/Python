# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
sports_directory['basketball'][1] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print(x,students,sports_directory,z)

# 2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range (len(students)):
        print("first_name" + " - " + students[i]['first_name'] + "," + " last_name" + " - " + students[i]['last_name'])
iterateDictionary(students) 

# 3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name,some_list):
    for i in range (len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for i in some_dict:
        print(str(len(some_dict[i])),i)
        for j in range(len(some_dict[i])):
            print(some_dict[i][j])
        print("")
        

printInfo(dojo)

# alternative
def printInfo(some_dict):
    for key in some_dict.keys():
        print(str(len(some_dict[key])),key)
        for val in some_dict.values():
            print(some_dict[key])
            break
        

printInfo(dojo)



