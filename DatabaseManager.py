import pyrebase
import pickle
import csv

file = open("Data.pyrebaseConfig","rb")
config = {}
config = pickle.load(file)
file.close()

firebase = pyrebase.initialize_app(config)
db = firebase.database()

a = False

def insert():
    name = input("Enter the Name: ")
    all_users = db.child("User").get()
    for user in all_users.each():
        if(name == user.key()):
            print("Name already exists!")
            a = False
            break
        else:
            a = True
            continue
    if a == True:
        age = int(input("Enter the Age: "))
        dob = int(input("Enter the DOB(only year): "))
        path = "User/"+name+"/"
        data = {path:{"Age":age,"DOB":dob}}
        db.update(data)
        print("Data Successfully Inserted!")

def lists():
    all_users = db.child("User").get()
    print("***List of Users***")
    for user in all_users.each():
        name = user.key()
        data = user.val()
        Age = data['Age']
        DOB = data['DOB']
        print("\nName: ",name,"\nAge: ",Age,"\nDOB: ",DOB)
    print("\n\nListing Done.....")
        
def remove():
    name = input("Enter the Name: ")
    all_users = db.child("User").get()
    for user in all_users.each():
        if(name == user.key()):
            db.child("User").child(name).remove()
            print("User: ",name," removed Successfully!")
            a = True
            break
        else:
            a = False
            continue
    if a == False:
        print("Name does not exists!")
        
def show():
    name = input("Enter the Name: ")
    all_users = db.child("User").get()
    for user in all_users.each():
        if(name == user.key()):
            print("User found!....Showing Data")
            name = user.key()
            data = user.val()
            Age = data['Age']
            DOB = data['DOB']
            print("\nName: ",name,"\nAge: ",Age,"\nDOB: ",DOB)
            a = True
            break
        else:
            a = False
            continue
    if a == False:
        print("Name does not exists!")

def update():
    name = input("Enter the Name: ")
    all_users = db.child("User").get()
    for user in all_users.each():
        if(name == user.key()):
            age = int(input("Enter the Age: "))
            dob = int(input("Enter the DOB(only year): "))
            path = "User/"+name+"/"
            data = {path:{"Age":age,"DOB":dob}}
            db.update(data)
            print("Data Successfully Updated!")
            a = True
            break
        else:
            a = False
            continue
    if a == False:
        print("Name does not exists!")
        
def Exportcsv():
    fields = ['Name','Age','DOB']
    rows = []
    all_users = db.child("User").get()
    for user in all_users.each():
        temp = []
        data = user.val()
        temp = [user.key(),data['Age'],data['DOB']]
        rows.append(temp)
    with open("ExportedFile.csv",'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    print("Data Successfully Exported as .csv!")

def Importcsv():
    fields = []
    rows = []
    with open("ImportFile.csv","r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print("Data imported from .csv file and now Uploading.......")
        for i in rows:
            name = i[0]
            age = i[1]
            dob = i[2]
            path = "User/"+name+"/"
            data = {path:{"Age":age,"DOB":dob}}
            db.update(data)
        print("Data Uploaded!")
    
print(40*'*')
print("Pyrebase based Databse Manager")
print(40*('*'))
print("\n\n             Menu")
print(40*'*')
print('''1.Inserting a Data.
2.Removing a Data.
3.List all Data
4.Search a Data.
5.Update a Data.
6.Export the Data as .csv file.
7.Import a .csv file and upload it.''')
print(40*'*')
case = int(input("Enter a Operation(Its S.no): "))
if case == 1:
    insert()
elif case == 2:
    remove()
elif case == 3:
    lists()
elif case == 4:
    show()
elif case == 5:
    update()
elif case == 6:
    Exportcsv()
elif case == 7:
    Importcsv()
else:
    print("Operaion Does not Exists!\n\nERR: Not a valid input")

