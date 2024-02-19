def my_function():
    a=1+2+5
    print(a)
    
    if a<10:
        print("a is 3")
        x=("not match in a")
        if a<10:
            print("a less than 10")
            for x1 in x:
                print(x1)
            x=x.split(" ")
            for x2 in x:
                print(x2)
    elif a==10:
        print("a is greater")
    else :
        print ("not match")

    y=input("Enter the value").split(",") 
    print(y)   
my_function()