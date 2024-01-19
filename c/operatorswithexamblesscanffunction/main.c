#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>
#include <stdlib.h>

int main()
{
    additon(getA(),getA(),getB());
    subtraction(getA(),getB());
    multiplication(getA(),getB());
    increment(getA());
    decrement(getB());
    divison2(getB(),getA());
    moduleprogram(getA(),getB());
    return 0;

}
int getA()
{
 int a;
 printf("Enter the value  :");
 scanf("%d",&a);
    return a;

}
int getB()
{
    int b;
    printf("Enter the value  :");
    scanf("%d",&b);
    return b;
}
int additon(int a,int b,int c)
{
    printf("add value is ...:%d\n",a+b+c);
}
int subtraction(int a, int b)
{
    printf("sub value is...:%d\n",a-b);
}
int multiplication(int a,int b)
{
    printf("multi valu is...%d\n",a*b);
}
int increment(int a)
{
    printf("incre value is %d\n",++a);
}
int decrement(int b)
{
    printf("decre the value is %d\n",--b);

}
int divison2(int a,int b)
{
    printf("divi the value is %d",a/b);

}
int moduleprogram(int a,int b)
{
 printf("module value is %d",a%b);
}

