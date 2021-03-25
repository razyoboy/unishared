#include <iostream>
#include <string>

using namespace std;
int main(){
    string name[100], n;
    int num, i, j;
    cout << "Enter the number of name you want to input >> ";
    cin >> num;
    cout << "Enter " << num << " names : \n";

    for (i=0; i<num ;i++){
        cout << " name " << i+1 << ": ";
        cin >> name[i];
    }
    cout << "Enter the name you want to search in array >> ";
    cin >> n;
    // if function does not work cuz it already terminate when n == name[j]
    for (j = 0 ; j < sizeof(name); j++){
        //cout << j+1 << "\n";
        if (n == name[j]){
            cout << "that is in the array";
            break;
        }
        
        //cout << name[j] << " ";
        
        }
        
        
        
        
    
    

}