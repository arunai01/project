#include<iostream>
using namespace std;
int main()
{

    string name="arun";
    cout << "my name is      :" << name << endl;
    cout << "my name address is :"<< &name << endl;

    string *p=&name;
    cout << "value of p    :" << *p <<endl;


}












































/*#include <iostream>

using namespace std;

int main()
{
    int a=10,b=20;
    cout << "address of the value  :" << &a <<endl;
    cout << "Value of a    :" << a <<endl;
    cout << "Address of the value b  :"<<&b <<endl;
    cout << "Value of b     :"<< b << endl;

    int *c=&a;
    cout << "Value of   c :"<< c <<endl;
    cout << "Address of the value c  :"<< &c <<endl;
    cout << "stored address value of c   :" << *c <<endl;

int *d=&b;
    cout << "Value of   d :"<< d
 <<endl;
    cout << "Address of the value d  :"<< &d <<endl;
    cout << "stored address value of d   :" << *d <<endl;
void *i=&a;
    cout << "Value of   i :"<< i <<endl;
    cout << "Address of the value i  :"<< &i <<endl;
    cout << "stored address value of i  :" << *(int*)i <<endl;

    return 0;
}*/
