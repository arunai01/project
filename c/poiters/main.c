#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=10,b=20;
    printf("Value of a    :%d\t\n",a);
    printf("address of a  :%d\n",&a);
    printf ("----------\n");
    printf("value of b     :%d\t\n",b);
    printf("address of b    :%d\n",&b);
    printf ("----------\n");

    int *p=&a;
    printf("value of p                       :%d\t\n",p);
    printf("Address of p                     :%d\t\n",&p);
    printf("value stored in the address of p :%d\t\n",*p);

    int **q=&p;
    printf("value of q                       :%d\t\n",q);
    printf("Address of q                     :%d\t\n",&q);
    printf("value stored in the address of q :%d\t\n",**q);

    int ***r=&q;
    printf("value of r                      :%d\t\n",r);
    printf("Address of r                     :%d\t\n",&r);
    printf("value stored in the address of r :%d\t\n",***r);

    void *s=&a;
    printf("value of s                        :%d\t\n",s);
    printf("address of s                      :%d\t\n",&s);
    printf("value stored address of s address are a   :%d\t\n",*(int*)s);
    return 0;
}
