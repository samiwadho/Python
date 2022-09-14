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



                        #9 IF CONDITON 
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
