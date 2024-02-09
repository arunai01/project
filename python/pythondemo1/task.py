#write to code in python 93571 9357 935 93 9

n="93571"
space =" "
count =0
while len(n) >=1:
    curr_space=space*count
    print(curr_space,end='')
    for c in n:
        print(c,end='')
        print(curr_space+"\n",end='')
        n=n[:-1]
        count -=1

          
          
