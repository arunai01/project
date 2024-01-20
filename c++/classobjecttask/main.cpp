#include<iostream>
using namespace std;

 class stringusing
 {
 public :
   aadharid()
    {
        string name;
        cout << "\n Enter the name  :";
        cin >> name;
        cout <<"\n hi.." << name << endl;

            cout <<name << " welcome to aadhar website";
        }
    aadharid(int age)

    {

        if (age>=5)
        {
        cout <<"\n\t you are eligible for biometric";
        }
        else
        {
            cout << "\n\t age does't match";
        }
    }
    aadharid(string name,int age)
    {
        cout <<"\nhi.." << name << endl;
            cout << name << "\nwelcome to aadhar";
    {

        if (age>=5)
        {
        cout <<"\nyou are eligible for biometric";
        }
        else
        {
            cout << "\nage does't support......sorry";
        }
    }
    }
 };

int main()
{
    stringusing su;
    su.aadharid();
    int age;
    cout << "\nenter the age";
    cin >> age;
    su.aadharid(age);
    string name;
    cout << "\nenter the name....:";
    cin >>name;
    cout << "\nenter the age...:";
    cin >> age;
    su.aadharid(name,age);
}

































/* #include<iostream>
using namespace std;

 class aadharid
 {
 public:
    aadharid()
    {
        int age;
        cout << "Enter the age";
        cin >> age;
        if (age>=5)
        {
        cout <<"you are eligiple for biometric";
        }
        else
        {
            cout << "age does't match";
        }
    }
    aadharid(float age)
    {

    if (age>4.9)
    {
        cout <<"\n eligiple for bio";
    }
    else
    {
        cout <<"age not match";
    }


    }


 };

int main()
{
    float age;
    aadharid ai;
    cout << "\n enter the second age";
    cin >> age;
    aadharid a2 (age);
}*/














































/*#include<iostream>


using namespace std;
class additon
{
public:     //access

    void checkage(int age)
    {
        if (age>=18)
        {
            cout << "you are eligible";

        }
        else
        {
            cout << "not eligible";
        }
    }

};

int main()
{
int age;
    additon ad;
    cout <<"enter the age";
    cin >> age;
    ad.checkage(age);
}*/





































/*#include<iostream>


using namespace std;
class arithoptrs
{
public:     //access

    void addition()
    {
        int x,y;
        cout <<"enter first value....";
        cin >>x;
        cout <<"\nenter second value...";
        cin >>y;
        cout <<"\n added value is ....";
        cout <<(x+y);

    }
        void subtraction()
    {
        int x,y;
        cout <<"\nenter first value....";
        cin >>x;
        cout <<"\nenter second value...";
        cin >>y;
        cout <<"\n subtract value is....";
        cout <<(x-y);

    }
    void multiplication()
    {
        int x,y;
        cout <<"\nenter first value....";
        cin >>x;
        cout <<"\nenter second value...";
        cin >>y;
        cout <<"\n multi value is....";
        cout <<(x*y);

    }
    void devision();
    void modulas();
    void increment();

};
 void arithoptrs::devision()
    {
        int x,y;
        cout <<"\nenter first value....";
        cin >>x;
        cout <<"\nenter second value...";
        cin >>y;
        cout <<"\n devision value is....";
        cout <<(x/y);

    }
    void arithoptrs::modulas()
    {
        int x,y;
        cout <<"\nenter first value....";
        cin >>x;
        cout <<"\nenter second value...";
        cin >>y;
        cout <<"\n modulas value is....";
        cout <<(x%y);

    }
    void arithoptrs::increment()
    {
        int x;
        cout <<"\nenter first value....";
        cin >>x;
        cout <<"\n increment value is....";
        cout <<(x++);

    }
    int main()
    {
        arithoptrs AOP,ASP,APO;
        AOP.addition();
        ASP.subtraction();
        AOP.multiplication();
        AOP.devision();
        AOP.modulas();
        AOP.increment();

        return 0;

    }*/



































































/*#include<iostream>


using namespace std;
class fclsmethod
{
public:     //access
    int a;
    void multiply()
    {
        int x,y;
        cout <<"enter first value....";
        cin >>x;
        cout <<"enter second value...";
        cin >>y;
        cout <<(x*y);

    }
    void messagesecond();
};
void fclsmethod::messagesecond()
{
    cout <<"\n addition";
}
int addition()
{
    int a,b,c;
    cin >>a;
    cin >>b;
    c=a+b;
    cout <<c;
    return 0;
}

int main()
{
    fclsmethod FCM,FCM1;
    FCM1.messagesecond();
    addition();
    FCM.a;
    FCM.multiply();

    return 0;

}*/




























































































/*int main()
{
    int age,ep,a;
    cout<<"Enter the age";
    cin>>age;
    cout<<"All method ";
    cin>>ep;
    switch (ep)
    {
    case 1:
    if(age>=18,age<=40)
    {
        cout<<"you are eligible for supplyment";
    }
    else if (age<18)
    {
        cout<<"you are under 18 not allowed";
    }
    else
    {
        cout<<"you are 40+not allowed";

    }
    case 2:
        for (int a=0;a<5;a++)
        {
            int a=0;
            cout<<"A value is...\n">>a;
        }

    }

    return 0;
}*/


















































/*#include <iostream>

using namespace std;

int main()
{
    int fvalue1,fvalue2,total,op;
    cout<<"Enter the value 1.....:";
    cin>>fvalue1;
    cout<<"\nEnter the value 2....:";
    cin>>fvalue2;
    cout<<"\noperators type.....:";
    cin>>op;
    switch (op)
    {
    case 1:
        total=fvalue1+fvalue2;
        cout<<"added value"<<total;
        break;
    case 2:
        total=fvalue1-fvalue2;
        cout<<"subtract value"<<total;
        break;
    case 3:
        total=fvalue1*fvalue2;
        cout<<"multi value"<<total;
        break;
    case 4:
        total=fvalue1/fvalue2;
        cout<<"subtract value"<<total;
        break;
    }
    return 0;
}*/
