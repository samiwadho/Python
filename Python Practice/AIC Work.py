               #1 PRINT 
print('My name is Abdul Sami')
print('I attedence batch 37 online Session')
print('I live at Karachi "CITY OF LIGHT"')
print('student of University of Sindh')
print('Department of Computer Science')


                #2 VARIABLES
Name='Abdul Sami'
PIAIC_batch= "37 Online"
Age= 22
Home_town="Karachi'City of light'"
University_Name= "University of Sindh"
Department="Computer Science"
print("NAME =",Name)
print("PIAIC batch =",PIAIC_batch)
print("Age =",Age)
print("Home town =",Home_town)
print("University Name=",University_Name)
print("Department =",Department)


                #2 VARIABLES with showing Data type
Name='Abdul Sami'
PIAIC_batch= "37 Online"
Age= 22
Home_town="Karachi'City of light'"
University_Name= "University of Sindh"
Department="Computer Science"
print("NAME =",type(Name),Name)
print("PIAIC batch =",type(PIAIC_batch),PIAIC_batch)
print("Age =",type(Age),Age)
print("Home town =",type(Home_town),Home_town)
print("University Name=",type(University_Name),University_Name)
print("Department =",type(Department),Department)



                #3 number 
num1 =5
num2 =25
num3 =4
print(num1*num2)
print(num1/num2)
print(num1+num3*num2)
print(num1+14*(10+num2)-140)
print(num3*10+(num1-10)+num2)

            #7 Math expressions: Eliminating ambiguity
  
total_cost =1+(3*2)
print(total_cost)

total_cost =(1+3)*2
print(total_cost)

total_cost =((1+3)*2)
print(total_cost)

total_cost =(1+(3*2))
print(total_cost)

result_of_computation = (2 * 4) * 4 + 2
print(result_of_computation)

result_of_computation = ((2 * 4) * 4) + 2
print(result_of_computation)

total = (12+2)*(13+1)
print(total)


            #8 Concatenating text strings
Full_Name="Abdul"+" Sami"+" Wadho"
print(Full_Name)

Department = "AI"+" (Artifical Intellgence)"+" At PIAIC"
Batch =" Batch"+" 37"+" Online"
print(Department + Batch)


              #9 IF CONDITON 
shop =int(input('shop ma kya kya ha!= '))

if shop==1:
    print('Milk')
    print('oil')
    print('eggs')
else:
    print('the shop is empty')
