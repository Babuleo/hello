'''a=int(input())
b=str(a)


if(a%2==0 and a>1):
    print("a is even")


if(a%2!=0 and a>1):
    print("a is even")
if(a==0):
    print("a is zero")
if(a<0):
    print("its negative number")

print(b[::-1])'''


'''a=input()
if(a=="123"):
    print("123")

if(a=="111"):
    print("111")

else:
    if a=="10":
        print("else")
    else:
        if a=="5":
            print("not else")'''


'''a=input()
if(a=="BB"):
    print("hai")

elif(a=="AA"):
    print("true")

else:
    print("end")'''

'''a=input("enter value")
if (a=="java"):
    print("true")

else:
    b=input("enter the another value")
    if b==a:
        print("okey")'''

'''name=input("Enter your name:")
roll= int(input("Enter Roll number:"))
gen=input("Gender:")
age=int(input("Age:"))
tamil=int(input("enter tamil mark:"))  #100-81=a
english=int(input("enter english mark:"))#80-61=b
maths=int(input("enter maths mark:"))     #60-41=c
science=int(input("enter science mark:"))  #40-35=d
social=int(input("enter social mark:"))    #34-1=poor
print("--------------------------------")
print("MARK SHEET")

print("name:",name)
print("Roll number:",roll)
print("gender:",gen)
print("Age:",age)

#total
total=tamil+english+maths+science+social
print("total mark is=",total)
#persentage
per=total/5
print("persentage:",per)


#tamil
if(tamil<100 and tamil>=81):
    print("mark tamil is ",tamil,"and tamil grade is A")
elif(tamil<=80 and tamil>=61):
    print("mark tamil is ",tamil,"and tamil grade is B")
elif(tamil<=60 and tamil>=41):
    print("mark tamil is ",tamil,"and tamil grade is C")
elif(tamil<=40 and tamil>=45):
    print("mark tamil is ",tamil,"and tamil grade is D")
else:
    print("mark tamil is ",tamil,"and tamil grade is poor")

#english
    
if(english<100 and english>=81):
    print("mark english is ",english,"and english grade is A")
elif(english<=80 and english>=61):
    print("mark english is ",english,"and english grade is B")
elif(english<=60 and english>=41):
    print("mark english is ",english,"and english grade is C")
elif(english<=40 and english>=45):
    print("mark english is ",english,"and english grade is D")
else:
    print("mark english is ",english,"and english grade is poor")

#maths    
if(maths<100 and maths>=81):
    print("mark maths is ",maths,"and maths grade is A")
elif(maths<=80 and maths>=61):
    print("mark maths is ",maths,"and maths grade is B")
elif(maths<=60 and maths>=41):
    print("mark maths is ",maths,"and maths grade is C")
elif(maths<=40 and maths>=45):
    print("mark maths is ",maths,"and maths grade is D")
else:
    print("mark maths is ",maths,"and maths grade is poor")
    
#science
if(science<100 and science>=81):
    print("mark science is ",science,"and science grade is A")
elif(science<=80 and science>=61):
    print("mark science is ",science,"and science grade is B")
elif(science<=60 and science>=41):
    print("mark science is ",science,"and science grade is C")
elif(science<=40 and science>=45):
    print("mark science is ",science,"and science grade is D")
else:
    print("mark science is ",science,"and science grade is poor")

#social
if(social<100 and social>=80):
    print("mark social is ",social,"and social grade is A")
elif(social<=81 and social>=61):
    print("mark social is ",social,"and social grade is B")
elif(social<=60 and social>=41):
    print("mark social is ",social,"and social grade is C")
elif(social<=40 and social>=45):
    print("mark social is ",social,"and social grade is D")
else:
    print("mark social is ",social,"and social grade is poor")


#pass or fail
if(tamil<35 or english<35 or maths<35 or science<35 or social<35):
    print("you fail")
else:
    print("you pass")'''


'''a="python"
if  (a=="java" or "html"):
    print("true")

else:
    print("false")'''

#nested if:if contains one or more if condition that is called nested if,

'''a="123"
if(a=="123"):
    b=12
    if(b==12):
        print("true")

    else:
        print("false")

else:
    print("end")'''


#login task

'''name=input("enter your name:")
if(name=="babu"):
    userid=input("enter your userid:")
    password=input("enter your password:")    

    if(userid=="babu2003" and password=="dev123"):
        print("login sucssfull")
    elif(userid!="babu2003" and password!="dev123"):
        print("invalied values")
    elif(userid!="babu2003"):
        print("invalied user id ")
    elif(password!="dev123"):
        print("invalied password")

else:
    print("enter your correct name")'''

#cheak number or string

'''value=(input("enter value"))
a=value.isalpha()
b=value.isnumeric()
c=value.isalnum()
if(a==True):
    print(a,"is leter")
elif(b==True):
    print(a,"is number")
elif(c==True):

    print(a,"is alphanumeric")'''
#check python file
'''a=input("enter the file")
b=a.endswith(".py")
if(b==True):
    print("yes its python file")
else:
    print("its not python file")'''

#find prime number
'''number = int(input("Enter a number: "))

if number <= 1:
    is_prime = False
elif number == 2:
    is_prime = True
elif number % 2 == 0:
    is_prime = False
elif number == 3:
    is_prime = True
elif number % 3 == 0:
    is_prime = False
elif number == 5:
    is_prime = True
elif number % 5 == 0:
    is_prime = False
elif number == 7:
    is_prime = True
elif number % 7 == 0:
    is_prime = False
else:
    is_prime = True

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")'''

#find prime number using if 
num=int(input("enter start  number:"))
enum=int(input("enter the end number:"))
for i in range(num,enum+1):
    if(i==1):
        print(i,"is not prime and composite number ")
    elif(i==2 or i==3 or i==5 or i==7):
        print(i,"is prime number")

    elif(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        print(i,"is not prime number")
    else:
        print( i,"jdicnjisncpnc")
    

        


    


    
