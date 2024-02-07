"""print("Arun welcome to python");
a=10;
b=20;
print(a+b);
print(a-b);
print()
a=int(input("enter the value a :"));
print (a);
b= int(input("enter the value :"));
print (b);
c=int(input("enter the value c :"));
print(c);
print ("Enter the addition value",a+b-c);


#if shortcut
if a>b :
    
    print ("a greater than b ");
else : 
    print("b greater than a");
#elseifshort

print("a greater than b") if a>b else print("b greater than a")

print("a greater than b") if a>b else print (" a and b is equal") if a == b else ("b greater than a")
 #and method
if a>b and c>a :
    print ("both condition same");
    #or method
if  a>b or c>a:
    print ("any one condition is true ")
#nested if
if a < b:
    if a < c and c > a:
        print ("a less  than c");
    elif a>b or c>a:
        print ("any one condition is true ");
    else :
        print ("All not match");
else :
    print("not match");
#concat
name=input("Enter your fname :");
name1=input("enter your sname :");
print (name);
print (name1);
print (name + " " + name1);
print (name.strip());
print (name.upper());
print (name1.lower());
print (name.title());
print (name.replace("a" ,"r"));
#while loop
i=int (input("enter the value i  :"));


while i < 10:
    print (i);
    if (i == 10):
        break
    i += 1 
    

fruits=["apple","banana","cherry","orange"]
for y in fruits:
    print (y)
    #looping though a string
for x in "apple":
    print (x)
#breakstatement
fruits1 =input("Fruits name :").split(",")
#fruits=["apple","orange","banana","lemon","mango"]
for z in fruits1:
    z1=z.split(" ")
    print(z1)

    if z == "banana":
        break
fruits1 =input("Fruits name :").split(",")
for y in fruits1:
    if y =="cherry":
        continue
   
    z=y.split(",")
    print(z)



#else in forloop

a=int(input("Enter the input :"))
for x in range (a):
    print(x)
else:
    print("finished")

a=int(input("Enter the input :"))
for x in range (a):
    if x== 3 :break
    print(x)
else:
    print("finished")

#class objest
#the str__ in function
class person:
    def __init__(self ,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"

        
a1 = person("Arun",22)
print(a1)


#object methods
class detail:
    def __init__(self,name,age,shename):
        self.name=name
        self.age=age
        self.shename=shename

    def myfunc(self):
        print("my name is" + self.name)
        print("my age is" , self.age)
        print("she name is " + self.shename)
m1 = detail("arun",22,"rathi")
m1.myfunc()
#modify object
m1.age=20
print (m1.age)"""

car=input("Enter your car name :")
#bike=input("Enter the bike name :").split(",")
x= (car.split(","))
#x.append("rollys royce")
#x.clear()
#x.copy()
#y=x.count("bmw")
#x.extend(bike)
x.index("m15")
print(x)
