#include <stdio.h>

int forloop1()
{

   int i, j, rows;
   printf ("Enter the Rows :");
   scanf("%d",&rows);
 
 for (i=1;i<=rows; i++)
 {
  
    for (j=1;j<=rows;j++)
    {
        printf (" ");
    }
for (j=i;j<=rows;j++)
{
    printf ("*");
}

       printf ("\n");
       }

       return 0;
 
 }