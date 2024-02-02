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
    string getmyfood(){

string tp;
        if ("grass"||"tree" ==food)
        {
            tp= " my food is "+ food +"  i am herbivorous";

                }
        else
        {
            tp=" my food is "+ food +" my carnivores";


        } return tp;
    }

};
class animal1:public animal{
    public :
                    string s="sound";

         void setmysound(){

            cout << "enter the sound  :\n";
            cin >>s;
        }
        string getmysound()
        {
            return s;
        }
};
class animal2:public animal1{
public :
            string atype="animaltype";

    void setmyatype()
    {

        cout << "enter the animal type";
        cin >>atype;
    }
string getmyatype()
{
     return atype;
}

};
int main()
{
    /*animal a;
    a.setmyname();
    a.setmycolor();
    a.setmyweight();
    a.setmyfood();

    cout << "my name is :"<<a.getmyname() << endl;
    cout << "my color is :" << a.getmycolor() <<endl;
    cout << "my weight is :" << a.getmyweight() <<endl;
    cout << "my food is  :" <<a.getmyfood() <<endl;
    //cout << "i am " << a.getmyfood1();


animal1 a1;
    a1.setmyname();
    a1.setmycolor();
    a1.setmyweight();
    a1.setmyfood();
    a1.setmysound();
    cout << "my name is :"<<a.getmyname() << endl;
    cout << "my color is :" << a.getmycolor() <<endl;
    cout << "my weight is :" << a.getmyweight() <<endl;
    cout << "i am " << a.getmyfood();
    cout << "my sound is :" << a1.getmysound()<<endl;*/


animal2 a2;
    a2.setmyname();
    a2.setmycolor();
    a2.setmyweight();
    a2.setmyfood();
    a2.setmysound();
    a2.setmyatype();
    cout << "my name is "<<a2.getmyname() << endl;
    cout << "my color is " << a2.getmycolor() <<endl;
    cout << "my weight is " << a2.getmyweight() <<endl;
        cout  << a2.getmyfood()<< endl;
    cout << "my sound is " << a2.getmysound()<<endl;
    cout << "i am " <<a2.getmyatype()<<endl;





    return 0;
}




