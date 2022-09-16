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

    
              # 15,16,17,18,19 list
              
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
 
 
                             # 21 for loop
num =[1,2,3,5,]

for i in num :
    print(i)

# In this program the Grade will show in horzital way
Grade = [40,50,60,70,80,90,100]
 
for assending in Grade :
    print(assending)

# In This program the temp list will printing in vertical way
temp_karachi = [40,45,42,46,43,49,48]
for temp in range(3):
    print(temp_karachi)

# In This program the temp list will printing in horzital way till the range you want like
#  like here we want to print till 4
temp_karachi = [40,45,42,46,43,49,48]
for temp in range(4):
    print("temp till the range we want =",temp_karachi[temp])
    
    
    
    
                     # 22 NEST FOR LOOP
first_names = ["BlueRay ", "Upchuck ", "Lojack ","Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
print("First_name : ",first_names)
print("Last_name : ",last_names)

# with for loop  to display list of name 
for first_name in (first_names):
    print("First_name =",first_name)

for last_name in (last_names):
    print("last_name =",last_name)
    
for  last_name in last_name:
    full_names.append(first_name+' '+last_name)
    print("full_names =",full_names)
