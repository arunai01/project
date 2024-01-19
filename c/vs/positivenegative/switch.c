#include <stdio.h>
int switch1()
{
int e;
int a;
int b;
int c;
int d;
int f;
int g;
printf("Enetr how many value  :");
scanf("%d",&e);
if (e==2)
{
printf("Enter the value 1....:");
scanf("%d",&a);

printf("Enter the value 2...:");
scanf("%d",&b);

printf("Enter the operator");
scanf("%d",&c);
switch(c)
{
case 1:
g=a+b;
printf("selected addition  :");
printf("A added value 1 and 2 is :%d", g);
break;
case 2:
g=a-b;
printf("selected subtraction  :");

printf("A subtract value 1 and 2 is :%d", g);
break;
case 3:
g=a*b;
printf("selected multiplication  :");

printf("A multi value 1 and 2 is :%d", g);
break;
case 4:
g=a/b;
printf("selected division  :");

printf("A dive value 1 and 2 is :%d", g);
break;
case 5:
g=a%b;
printf("selected module  :");
printf("A module value 1 and 2 is :%d", g);
break;
}
}
else 
{
printf("Enter the value 1...:");
scanf("%d",&a);

printf("Enter the value 2....:");
scanf("%d",&b);

printf("Enetr the value 3....:");
scanf("%d",&d);

printf("Enter the operator  :");
scanf("%d",&c);
switch(c)
{
case 1:
g=a+b+d;
printf("selected addition  :");
printf("A added value 1 and 2 is :%d", g);
break;
case 2:
g=a-b-d;
printf("selected subtraction  :");
printf("A subtract value 1 and 2 is :%d", g);
break;
case 3:
g=a*b*d;
printf("selected multiplication  :");
printf("A multi value 1 and 2 is :%d", g);
break;
case 4:
g=a/b/d;
printf("selected division  :");

printf("A dive value 1 and 2 is :%d", g);
break;
case 5:
g=a%b%c;
printf("selected module  :");

printf("A module value 1 and 2 is :%d", g);
break;

}
}
return 0;
}
