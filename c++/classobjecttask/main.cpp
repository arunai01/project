#include<iostream>
using namespace std;

class animal{
private :
    string name;
    string color;
    int weight;
    string food;
    string sound;
    string animaltype;
public:
    void setmyname()
    {
        cout << "Enter the animal name  :";
        cin >> name;
    }
    string getmyname()
    {
        return name;
    }
    void setmycolor()
    {
        cout <<"\nEnter the color  :";
        cin >>color;
    }
    string getmycolor()
    {
        return color;
    }
    void setmyweight()
    {
        cout <<"\nenter the weight  :";
        cin >> weight;
    }
    int getmyweight()
    {
        return weight;
    }
    void setmyfood()
    {
        cout <<"\nEnter the food item  :";
        cin >>food;
    }
    string getmyfood()
    {

    string tp;
        if (food=="grass")
        {
            tp ="herbivorous";
            return tp;      }
        else
        {
            tp ="carnivores";
            return tp;

        }
    }
};
class
int main()
{
    animal a;
    a.setmyname();
    a.setmycolor();
    a.setmyweight();
    a.setmyfood();
    cout << "my name is :"<<a.getmyname() << endl;
    cout << "my color is :" << a.getmycolor() <<endl;
    cout << "my weight is :" << a.getmyweight() <<endl;
    cout << "i am " << a.getmyfood();
    return 0;
}






















/*#include <iostream>
using namespace std;

class bikes
{
    public :
    string brand="Yamaha\n";
    void typebike()
    {
        cout << "welcome to yamaha\n";
    }
};

class biketype{
public:
    void biketype1(string model,string version)
    {
        cout << "you choose " << model <<"\n" ;
        cout << "you select " <<version <<"\n";
    }
};
class bike : public bikes,public biketype
{


};

int main ()
{
    string model;
    string version;
    bike b;
    cout << b.brand;
    b.typebike();
    cout <<"select your model type :\n";
    cin >> model;
    cout <<"choose the version :";
    cin >> version;
    b.biketype1(model,version);


}*/















/*#include<iostream>
using namespace std;

class consoverload
{
public:
    consoverload()
    {
     int age;
     if(age>=18)
     {
         cout << "age supported";
     }
      else if (age>=50)
      {
          cout << "age limited is over";
      }
      else
        cout << "age not supported";

    }
    consoverload(int a,string name,string game)
    {



        switch(a){
          case 1:
                for (int j=0;j<1;++j)
                {
                    cout <<name<< " is a good boy\n";
                    cout <<game<< " is fav game\n";
                }

                break;

          case 2:
            for (int i=0;i<3;++i)
            {
                cout << "he is bad" <<"\n";
            }
           break;
          case 3:
            for (int i=0;i<3;i++)
            {
                cout << "he is arrogant\n";
            }
    }
    }
};
int main()
{
    //int age;
    int a;
    string name;
    string game;
    //cout << "enter your age";
    //cin >> age;
    cout << "enter your number   :";
    cin >> a;
    cout << "enter your name   :";
    cin >>name;
    cout << name << " what is your fav game  :";
    cin >> game;

    //consoverload col;
    consoverload col1(a,name,game);
    return 0;
}*/
























/*#include<iostream>
using namespace std;

class accessspecifiar
{

private :
    int amount;
public :
    string empname;
  void setamount(int s)
    {
        amount=s;
    }
   int getamount()
   {
       return amount;

   }

   void tosalary()
   {
       cout << amount;
   }
};
int main()
{
    accessspecifiar as;
    as.setamount(500);
    cout << as.getamount() << endl; //50
    as.tosalary();
     if (as.getamount()==500){
        cout << "its a return type";
    }
    if (as.getamount()==500){
        cout << "its a return type";
    }
    return 0;

}*/




























/*#include<iostream>
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
     aadharid(string name,int age,string aadharnumber){

     aadharid(name,age);

     cout << "\n your aadhar number" << aadharnumber;

     }
    aadharid(string name,int age,string  aadharnumber,string phone)
    {

     aadharid(name,age,aadharnumber);
    cout << "\n checking the phone number" << phone;
    }
 };

int main()
{
    stringusing su;
    //su.aadharid();
    int age;
    /*c
    out << "\nenter the age";
    cin >> age;
    su.aadharid(age);*/
    /*string name;
    cout << "\nenter the name....:";
    cin >>name;
    cout << "\nenter the age...:";
    cin >> age;
    //su.aadharid(name,age);
    string aadharnumber;
    cout <<"\n enter your aadhar number  :";
    cin >> aadharnumber;
    string phone;
    cout << "\n enter your phone number    :";

    cin >>phone;
    //su.aadharid(name,age,aadharnumber);
    su.aadharid(name,age,aadharnumber,phone);

} */

































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
