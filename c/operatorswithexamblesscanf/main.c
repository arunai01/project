#include <stdio.h>

int main()
{
int a,b;
 printf ("Enter the value  A  :");
    scanf("%d",&a);
    printf("enter the value  B  :");
    scanf ("%d",&b);


    additonprogram(a,b);
    subtractionprogram(a,b);
    multiplicationprogram(a,b);
    divisionprogram(a,b);
    moduleprogram(a,b);
    incrementprogram1(a);
    decrementprogram(b);

    return 0;
}
int additonprogram(int x,int y)
{
    int z=x+y;
    printf("added value is ...:%d\n",z);

}
int subtractionprogram(int a,int b)
{
     int c=a-b;
    printf("sub value is ...%d\n",c);
}

int multiplicationprogram(int a,int b)
{
    int c=a*b;
    printf("multi value is ...:%d\n",c);

}

int divisionprogram(int d,int e)
{
    int a=d/e;
    printf("Divi value is ...:%d\n",a);
}
int moduleprogram(int a,int b)
{
 int c=a%b;
 printf("Modu value is ....%d\n",c);

}
 int incrementprogram1(int a)
{
     a++;
    printf("increment value is :%d\n",a);
}
int decrementprogram(int b)
{
    b--;
    printf("decrement value is  :%d\n",b);
}
