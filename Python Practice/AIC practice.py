                                              # Practice  1
print ('     Grade')
Grade_A=80
Grade_B=70
Grade_C=60
Grade_D=50
Grade_F=40
print("urdu       =",B-6)
print("Chemisty   =",A-14)
print("English    =",C+13)
print("Physic     =",B-10)
print("Mathmentic =",B-12)

                #VARAIBLE
age =12
name ="Sami"
is_adult=False
temp_age=age
age=17
print(age,temp_age)
print(type(age),age)
print(name)
print(temp_age)


#1alpha =20 #SHOULD NOT START WITH NUMBER 
#alpha.beat=21 #SPECIAL CHARACTER NOT ALLOWED
alpha_beat=21 #OK
_=10           #OK
a=10           #OK


                  #remainder
print(15%2) 
print(122%3)


age=15
age +=1
print(age)
salary=100000
salary -=8000
print(salary)
print(salary+7000)


salary =10000
increment=12
salary-=increment
print(salary)

#Concentation

NAME="Abdul"
print(NAME,"Sami")
#-----------------------OR-------------------------
combining= 'Sami'
final_result=combining+'Wadho'
print(final_result)

#most important part we can't concente intger with variable to therefore we change it's datatype 
#for example
name = 'Sami'
final_result= name+ ' Wadho '
print('I am',final_result + str( 45) + ' year old'  )




#input

name = input('Enter your name !')
age=input("Enter your Age ! ")
print('Name = ',name)
print('age = ',age ,'the datatype is',type(age))

#NOTE It doesn't matter what datatype we enter . it datatype always string type you will seen the datype str 
#at the age section


#CALCULATER

operand1=input('enter number =')
operand2=input('enter number =')

result=operand1+operand2
print('\n\noperand1+operand2=',result)

#AS We know what ever datatype we input the number or boolen experssion the datatype remain in string type 
# till that we give that any datatype value like below example "int"

result=int(operand1)+int(operand2)
print('\n\noperand1+operand2 =',result)


#for showing operands values
print('\n',operand1+'+'+operand2+'=',+result)

              
#type   
Region = "Larkrana"
portal_number ="77215"
Nationatly ="Pakistan"
salary=("$100000")
print(type(Region),Region)
print(type (portal_number),portal_number)
print(Nationatly)
print(salary)
    
        #8 Concatenating text strings
print("Hello!","Sami")
greeting="Hello! Sami"
print(greeting)

greeting="Hello!"
full="Sami"
print(greeting+full)

    #0R
greeting="Hello!"
full="Sami"
whole=greeting+full
print(whole)



greeting ="Hello"
punc="!"
full = "Sami"
print(greeting+punc+full)

        #OR
greeting ="Hello"
punc="!"
full = "Sami"
whole=greeting+punc+full
print(whole)

a=  " AI"
b= " Artifical Intellgence"
con=a+b
c="PIAIC"+con
print(c)


Ahad1="Ahad1 = Hello, Sami!"
Sami="\nSami = Hey! Abdul Ahad"
Ahad2="\nAhad2= How are you Doing"
intro=Ahad1+Sami+Ahad2
print(intro)


first_name="Sami"
space=" "
last_name="Wadho"
greeting =first_name+space+last_name
print(greeting)



                        #9 IF CONDITON  10 ELSE CONDITION 11 ELIF CONDITION
shop =int(input('shop ma kya kya ha!= '))

if shop==1:
    print('Milk')
    print('oil')
    print('eggs')
else:
    print('the shop is empty')
    
    
    #2 making mark sheet 
    
    marks = int(input("Enter Marks = "))
if marks > 80:
    print("A")
elif marks >70: 
    print("B")
elif marks > 60:
    print("C")
else:
    print("F")
    
Student_Name = input("Please Enter the name ")
Roll_Number = int(input("please Enter the Roll number"))
print("Name = ",Student_Name)
print("Roll Number = ",Roll_Number)
print("Marks = ",marks,"/100")


#marksheet work
#1 first of all we are going to make total subject and there mark which will be defined by user
Chemistry = int(input('Chemistry ='))
physic = int(input('Physic = '))
math = int(input('Math = '))
Urdu = int(input('Urdu = '))

#2 Now we make an analysis which is total mark and obtained mark 

marks_Obtained = Chemistry+physic+math+Urdu
total_Marks =400

#3 after that we calculate percentage of total mark and obtained mark
Grade = (marks_Obtained / total_Marks) * 100

# 4 display the user input data

name = input("Name :")
Roll_No = int(input("Roll_No"))
print("Marks :",marks_Obtained,"/",total_Marks)
print("Chemistry :",Chemistry,"out of 100")
print("Physic :",physic,"out of 100")
print("Math \t:",math,"out of 100")
print("Urdu \t:",Urdu,"out of 100")
print("Per  \t:",Grade)


# 3 these conditon is related to grade section where we defined 
if Grade >=80:
    print("A")
elif Grade >=70 :
    print("B")
elif Grade >=60 :
    print("C")
elif Grade >= 50 :
    print("D")
else :
    print("F")
    
    
    
    # 15 list
temperatures = [40,44,43,39,35,34]

temperatures[0]=-45
#the above value show that we rearrange previous values into new data

temperatures.append(-56)
print(temperatures[-1])
#append is for adding new values

print(temperatures)
print(len(temperatures))

# in python hertogenic data store  ,it mean we insert number or string in a single statement
#example
# temp_list =[10,"pakistan,true"]

print(temperatures[0])
#if we want to second temp
print(temperatures[5])
#we have to remember that we calcluate value by n-1 like we want to find 6 value to above we put 7 than we find 6
print(temperatures[-2])
#this is inverse section



#add two other city temp
temperatures_karachi=[20,23,25,26,29,30]
temperatures_Lahore=[34,30,40,38]
temp_pk = temperatures_karachi+temperatures_Lahore
print(temp_pk)

#sub temp value
temperatures=[1,2,3,[10,14,15,18],4,5,6]
print(temperatures[0])
print(temperatures[3])
#if we want to find deep value of 3  which is [10,14,15,18] we find it like
print(temperatures[3][2])# which is 15 after 14

temp = [1,2,3,[15,16,17,18],4,5]
#add new value this is point that we add 1 value or we add list , we can't add 2 value 
#like this temp.appand(6,7) this will show an error 
#therefore 
temp.append(6)
print(temp)
#-------------or--------------
temp.append([6,7,8,9])
print(temp)

#if we extend same value ([6,7,8,9]) then it insert data like value not a list like intger 4,5,6,7,8,9 where as in appand this it look like [6,7,8,9]

temp.extend([6,7,8,9])
print(temp)
#for insert new index and where you want  now want to insert new index 49 on places of 5 which is value is 4
temp.insert(5,49)
print(temp)


# for finding what is place of inex 3
print(temp.index(6)) #which is on the place of 2

#for remove index we use

print(temp.remove(3))

#pop if you don't give index address then pop remove last index
print(temp.pop)# which drop 9 


#for remove index we from sub list which is([6,7,8,9])







temp = [1,2,3,[15,16,17,18],4,5]
#add new value this is point that we add 1 value or we add list , we can't add 2 value 
#like this temp.appand(6,7) this will show an error 
#therefore 
temp.append(6)
print(temp)
#-------------or--------------
temp.append([6,7,8,9])
print(temp)

#if we extend same value ([6,7,8,9]) then it insert data like value not a list like intger 4,5,6,7,8,9 where as in appand this it look like [6,7,8,9]

temp.extend([6,7,8,9])
print(temp)
#for insert new index and where you want  now want to insert new index 49 on places of 5 which is value is 4
temp.insert(5,49)
print(temp)


# for finding what is place of inex 3
print(temp.index(6)) #which is on the place of 2

#for remove index we use

print(temp.remove(3))

#pop if you don't give index address then pop remove last index
print(temp.pop)# which drop 9 


#for remove index we from sub list which is([6,7,8,9])





num = [1,2]
print(num)

num.append(3)
print(num)

num.extend([4,5])
print(num)

num.append([6,7,8,9])
print(num)

print(num[4])

print(num[5][2])





cities = ["Karachi" ,"Qamber" ,"Larkana","Sukker"]

cities_tup =("Karachi" ,"Qamber" ,"Larkana","Sukker")

city_of_light = "Karachi"

for C in range(len(cities)):
    if city_of_light == cities[C]:
        print("Found")
    else :
        print("not Found")
        
        
 
 
 # IN this example we are going to find city and if the city will found then it will brack on the spot

cities = ["Karachi" ,"Qamber" ,"Larkana","Sukker"]

city_of_light = "Karachi"
city_of_beauty= "Sukker"

for C in range(len(cities)):
    if city_of_light.lower() == cities[C].lower():
        print("Found")
        break
    elif  city_of_beauty == cities_tup:
        print("Found")
        break
    else :
        print("not Found")
    
    
cities = ["Sukker", "Kamber","Larkana","Lahore"]

city_beauty = "Kamber"
for city in range(2):
    if city_beauty == cities[city]:
        print("Found")
    else :
            print(" not Found")

        
