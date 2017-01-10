users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
x=""
def Names(x):

    count=1
    for key, data in users.items():
        print key
        for value in data:
            print count,value["first_name"] +" "+ value["last_name"],len(value["first_name"])+len(value["last_name"])
            count=count+1
Names(x)
