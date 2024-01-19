#include <stdio.h>

int positiveornegative()
{
int a;
 printf ("Enter the value  A  :");
    scanf("%d",&a);
if (a>0)
{
    printf ("the value is positive number...:");
}
else if (a<0)
{
    printf("the value is negative number....:");
}
else
{
printf("The vslue is 0:");
}
return 0;
}