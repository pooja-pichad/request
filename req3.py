import requests
import json
# i am using this link for give data
url1=requests.get("https://api.merakilearn.org/courses") 
# then i create a json file for storing this link data in course.json file
var1=url1.json()
with open("course.json","w")as f:
    json.dump(var1,f,indent=4)
# then i run one loop for numbers coming in line by line and print names and their id
serial_no=1
for i in var1:
    print(serial_no,i["name"],i["id"])
    serial_no=serial_no+1
# after runing loop i give one user input for choose the number
course_no_1=int(input("enter your number do you want in id"))
print(var1[course_no_1-1]["name"])
idd=var1[course_no_1-1]["id"]
np=input("what do you want privious(p).....or next(n).......")
if np=="p":
    url1=requests.get("https://api.merakilearn.org/courses") 
    var1=url1.json()
    with open("course.json","w")as f:
        json.dump(var1,f,indent=4)
    serial_no=1
    for i in var1:
        print(serial_no,i["name"],i["id"])
        serial_no=serial_no+1
    course_no_1=int(input("enter your number do you want in id"))
    print(var1[course_no_1-1]["name"])
    idd=var1[course_no_1-1]["id"]


url2=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
var2=url2.json()
with open("topic.json","w")as h:
    json.dump(var2,h,indent=5)
    serial_no2=1
    list1=[]
    list2=[]
for j in var2["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial_no2,j["name"])
        print("      ",serial_no2,j["slug"])
        serial_no2+=1
        list1.append(j)
        list2.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial_no2,j["name"])
        serial_no2+=1
        new_no=1
        list1.append(j)
    for t in var2["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print("       ",new_no,j["name"])
            new_no+=1
            list2.append(j)
            break
with open("topic1.json","w")as f:
    json.dump(list1,f,indent=4)
point=int(input("enter the point"))
for k in list1:
    if k["parent_exercise_id"]==k["id"]:
        print(list1[point-1]["name"])
        num=(list1[point-1]["id"])
        break
var=[]
var3=[]
new_no1=1
for n in list2:
    if n["parent_exercise_id"]==num:
        print("    ",new_no1,n["name"])
        var.append(n["name"])
        var3.append(n["content"])
        new_no1+=1
np1=input("what do you want privious(p).......or next(n)........")
if np=="p":

    url2=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
    var2=url2.json()
    with open("topic.json","w")as h:
        json.dump(var2,h,indent=5)
        serial_no2=1
        list1=[]
        list2=[]
    for j in var2["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_no2,j["name"])
            print("      ",serial_no2,j["slug"])
            serial_no2+=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial_no2,j["name"])
            serial_no2+=1
            new_no=1
            list1.append(j)
        for t in var2["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("       ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
    point=int(input("enter the point"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[point-1]["name"])
            num=(list1[point-1]["id"])
            break
    var=[]
    var3=[]
    new_no1=1
    for n in list2:
        if n["parent_exercise_id"]==num:
            print("    ",new_no1,n["name"])
            var.append(n["name"])
            var3.append(n["content"])
            new_no1+=1

questions_no = int(input("choose the specific questions no :- "))
question=questions_no-1

print(var[question])
print(var3[question])

while questions_no > 0 :
    next_question = input("do you next question or previous question n/p :- ")
    if questions_no == len(var3):
        print("next page")
    if next_question == "p" :
        if questions_no == 1:
            print("no more questions")
            # break
        else:
            questions_no = questions_no  -1
            print(var3[questions_no])
    elif next_question == "n":
        if questions_no < len(var3):
            index = questions_no + 1
            print(var3[index-1])
            question = question + 1
            questions_no = questions_no + 1 
            if question == (len(var3)-1) :
                print("next page")
                break