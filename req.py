import requests
import json

from requests.api import request
api=('http://saral.navgurukul.org/api/courses')
url=requests.get(api)
# print(saral)

data=url.json()
with open ("saral_data.json","w") as saral_data:
    json.dump(data,saral_data,indent=4 )

print("Welcome to navgurukul and learn basic programming language *** ")

serial_no=0
for i in data["availableCourses"]:
    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1
    print("")
user=int(input("enter your courses number that you want to learn "))
parent_id=data["availableCourses"][user-1]["id"]
print(data["availableCourses"][user-1]["name"])

print(" ")
print("WELCOME TO NAVGURUKUL AND LEARN BASIC PROGRAMMING LANGUAGE ***")
print(" ")

user_input_1=input("if you want next or previous n/p: ")
if user_input_1=="p":
    i=0
    while i<len(data["availableCourses"]):
        Courses = (data["availableCourses"][i]["name"])
        print(i+1," ",Courses,data["availableCourses"][i]["id"])
        i=i+1
    user_input = int(input("Enter your courses number that you want to learn:-"))
    print(data["availableCourses"][user_input-1]["name"])

# calling parents api

parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user-1]["id"])+"/exercises"
parent_url = requests.get(parent_api)
# print(parent_url)

parents_data=parent_url.json()
with open ("parents_url.json","w")as f:
    json.dump(parents_data,f,indent=4)

serial_no_1=0
for i in parents_data["data"]:
    print("      ",serial_no_1+1,".",i["name"])
    if len(i["childExercises"])>0:
        s= 0
        for j in i['childExercises']:
            s = s+ 1
            print( "               ",s,j['name'])
    else:
        print("    1",i["slug"])
    serial_no_1+=1

topic_no = int(input("Enter topic number that's you want to learn:- "))
serial_no_3= 0
my_list=[]
for l in parents_data['data']:
    serial_no_3+=1
    if topic_no == serial_no_3:
        user_input_3=input("Enter topic number that's you want to learn previous or next or n/p:- ")
        if user_input_3=="p":
            serial_no_1=0
            for i in parents_data["data"]:
                print("      ",serial_no_1+1,".",i["name"])
                if len(i["childExercises"])>0:
                    s= 0
                    for j in i['childExercises']:
                        s = s+ 1
                        print( "               ",s,j['name'])
                else:
                    print("                1",i["slug"])
                serial_no_1+=1
topic_no = int(input("Enter topic number that's you want to learn:- "))
m = 0
while m < len(parents_data["data"][topic_no-1]["childExercises"]):
    print("     ", m+1 ,parents_data["data"][topic_no-1]["childExercises"][m]["name"])
    slug = (parents_data["data"][topic_no-1]["childExercises"][m]["slug"])

    # calling a child exercise 

    child_exercises_url = ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
    Data_3 = requests.get(child_exercises_url)

    # converting data into a json file

    convert_data = Data_3.json()
    with open("Topic.json","w") as f:
        json.dump(convert_data,f,indent=4)
    my_list.append(convert_data["content"])
    m = m + 1
# And then taking a user input in a choose the questions....

questions_no = int(input("choose the specific questions no :- "))
question=questions_no-1
print(my_list[question])
while questions_no > 0 :

# Here a taking user input in a previous or next

    next_question = input("do you next question or previous question n/p :- ")
    if questions_no == len(my_list):
        print("next page")
    if next_question == "p" :
        if questions_no == 1:
            print("no more questions")
            break
        elif questions_no > 0:
            questions_no = questions_no - 2
            print(my_list[questions_no])
    elif next_question == "n":
        if questions_no < len(my_list):
            index = questions_no + 1
            print(my_list[index-1])
            question = question + 1
            questions_no = questions_no + 1 
            if question == (len(my_list)-1) :
                print("next page")
                break