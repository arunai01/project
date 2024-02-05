"""print("Arun welcome to python");
a=10;
b=20;
print(a+b);
print(a-b);
print()"""
a=int(input("enter the value a :"));
print (a);
b= int(input("enter the value :"));
print (b);
c=int(input("enter the value c :"));
print(c);
print ("Enter the addition value",a+b-c);

'''if a>b :
    
    print ("a greater than b ");
else : 
    print("b greater than a");
print("a greater than b") if a>b else print("b greater than a")'''
#print("a greater than b") if a>b else print (" a and b is equal") if a == b else ("b greater than a")

'''if a>b and c>a :
    print ("both condition same");
if  a>b or c>a:
    print ("any one condition is true ")'''
'''if a < b:
    if a < c and c > a:
        print ("a less  than c");
    elif a>b or c>a:
        print ("any one condition is true ");
    else :
        print ("All not match");
else :
    print("not match");'''

name=input("Enter your fname :");
name1=input("enter your sname :");
print (name);
print (name1);
print (name + " " + name1);