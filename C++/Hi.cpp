#include <iostream>
using namespace std;
int main(){
    int score;
    cout << "How was today for you??\n" << "2 = Today was worth living \n" <<"1 = It was a good day.\n" << "0 = Nothing, just a hallowed day\n"<< 
    "-1 = A bit disappointed\n" << "-2 = Why am I still living ???\n" << "From these 5 scores, please choose one of them. Don't worry, I won't tell anyone : ";
    cin >> score;
    if (score == -2){
        cout << "Oh dear, I'm sorry to hear. However, You have to fight it. Don't let those tears overcome you.\n A better tomorrow is waiting. And I'm looking to hear a good news from you :)";
    }else if (score == -1){
        cout << "Don't worry about it!!. Life is always having 2 sides. I believe you will get over it";
    }else if (score == 0){
        cout << "Don't worry there might be something good next day. Cheer up!!. I believe there is more to discover in this world :)";
    }else if (score == 1){
        cout << "Really?!, I know it would be. Keep doing it!!. Something amazing waiting for you in future ";
    }else if (score == 2){
        cout << "I have known all along this day will come!! I will allow be with you onward \nBelieve me this will not be the last time you experience something mesmerizing!!!";
    }
    system("Hi.sh");
}
