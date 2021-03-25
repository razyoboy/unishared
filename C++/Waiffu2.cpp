#include <iostream>
#include <string>
#include<bits/stdc++.h> 

using namespace std;
string waifu, husbando;
int key, j;
string waifey[] = {"amber", "barbara", "beidou", "diona", "fishcl", "ganyu", "jean", "keqing", "klee", "lisa",
                  "mona", "ningguang", "noella", "qiqi", "sucrose", "xiangling", "xinyan", "lumine"};
string husban[] = {"albedo", "bennett", "chongyun", "diluc", "kaeya", "razor", "tartaglia", "venti", "xiao",
                   " xingqiu", "zhongli", "aether"};

string Waifucalculator(){
    cout << "Welcome to waifu library. " << "Here, we have many types of waifu\n" 
    << "Please input the name of waifu that you want : ";
    cin >> waifu;
    transform(waifu.begin(), waifu.end(), waifu.begin(), ::tolower);
    waifu[0] = toupper(waifu[0]);
    cout << "So, your waifu is "<< waifu << "\n";
    transform(waifu.begin(), waifu.end(), waifu.begin(), ::tolower);
    for (j=0; j <= sizeof(waifey); j++) {
        if (waifu == waifey[j]){
            cout << "Let me think about that for a sec....\n " ;
            if (waifu == "ganyu"){
                cout << "That is one fine choice my good sir!\n Glory to Cocogoat, the Legendary Adeptibeast!";
            }else if (waifu == "mona"){
                cout << "Lol, you still do not get her?\n";
                cout << " Eh, you got her but not in your main account ?\n I feel sorry for you.";
            }else {
                cout << "Okay, that's kinda lame ";
            }
        break;
        }
       }if(j > sizeof(waifey)){
           cout << "Sorry sir, the inputed name is invalid...";

       }
    return waifu;
}
string Husbandocalculator(){
    cout << "Welcome to husbando library. "<< "Here, we have many types of husbando\n";
    cout << "Please input the name of husbando that you want : ";
    cin >> husbando;
    transform(husbando.begin(), husbando.end(), husbando.begin(), ::tolower);
    husbando[0] = toupper(husbando[0]);
    cout << "So, your husbando is "<< husbando << "\n";
    transform(husbando.begin(), husbando.end(), husbando.begin(), ::tolower);
    for(j=0; j <= sizeof(husban); j++){
        if (husbando == husban[j]){
            cout << "Let me think about that for a sec....\n " ;
            if (husbando == "zhongli"){
                cout << "Well, well. If it ain't the Geodaddy. All hail Rex Lapis and his cheap fake death!";
                cout << "I bet Ganyu is going to be pissed about you faking your death.";
                break;
            }else if (husbando == "venti"){
                cout << "EHE TE NANDAYO";
                break;
            }else {
                cout << "Meh, lame";
                break;
            }
        }
    }
    if (j > sizeof(husban)){
        cout << "Sorry sir, the inputed name is invalid...";
    }
    
    return husbando;
}

main (){
    cout << "Hello, welcome to Waifu calculator!!!\n" ;
    cout << "Please input the number (1 for waifu - 2 for husbando) : ";
    cin >> key;
    if (key == 1){
        Waifucalculator();
    }else if (key == 2){
         Husbandocalculator();
    }else{
        cout << "The input is invalid... try again later";
        exit;
    }
    
}

        