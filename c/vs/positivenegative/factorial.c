#include<stdio.h>


   int factorial()

   {
    int a,b;
    unsigned long long fact =1;
    printf("Enter the integer number :");
    scanf("%d",&a);


    if (a<0)
    printf("Error ! factorial number its a negative number ");

    else {
   for (b=1;b<=a;++b)
   {
    fact *=b;

   }
    printf ("Factorial of %d = %llu",a,fact);
    }
    return 0;
   }