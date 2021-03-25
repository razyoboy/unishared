#include <iostream>
#include <string>


using namespace std;
string waifu, husbando;
string waifey;
int num;
string waifucalculator(){
    cout << "Oh ho, so you have chosen for waifu?\n" << "What is your favourite one : ";
    cin >> waifu;
    if(waifu == "Ganyu"){
        cout << "Solid choice , wise words\n" ;
        return waifu;
    }else{
        cout << "Please, C H O O S E the valid choice\n";
        return 0;
    }  
}

string husbandocalculator(){
    cout << "You are not a man of culture, GET LOST";
    return 0;
}
main(){
    cout << "Welcome you horny man, please choose the function to run 1 or 2 :";
    cin >> num;

    if(num==1){
        waifucalculator();
        cout << "WOW, So "<< waifu << " is your waifu (beuty and titties)";
    }else if(num==2){
        husbandocalculator();
    }else {
        cout << "Please enter valid choice you, horny";
    }

    
}

