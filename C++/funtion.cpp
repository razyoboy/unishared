#include <iostream>
using namespace std;
float height, weight;
float h ;

float calculateBMI(){
    h = height/100;
    float bmi = weight/(h*h);
    return bmi;
}
 main(){
    
    cout << "Input your weight (kg): ";
    cin >> weight;
    cout << "Input your height (cm): ";
    cin >> height;
    cout << calculateBMI();
    return 0;
}