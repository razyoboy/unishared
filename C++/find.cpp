/*
#include<bits/stdc++.h> 

int main () 
{ 
    std::vector<int> vec { 10, 20, 30, 40 }; 
      
    // Iterator used to store the position  
    // of searched element 
    std::vector<int>::iterator it; 
      
    // Print Original Vector 
    std::cout << "Original vector :"; 
    for (int i=0; i<vec.size(); i++) 
        std::cout << " " << vec[i]; 
          
    std::cout << "\n"; 
      
    // Element to be searched 
    int ser = 30; 
      
    // std::find function call 
    it = std::find (vec.begin(), vec.end(), ser); 
    if (it != vec.end()) 
    { 
        std::cout << "Element " << ser <<" found at position : " ; 
        std::cout << it - vec.begin() << " (counting from zero) \n" ; 
    } 
    else
        std::cout << "Element not found.\n\n"; 
          
    return 0; 
} 
*/
#include<bits/stdc++.h> 
using namespace std; 
  
int main() 
{ 
    // su is the string which is converted to uppercase 
    string su = "Jatin Goyal"; 
  
    // using transform() function and ::toupper in STL 
    transform(su.begin(), su.end(), ::toupper); 
    cout << su << endl; 
  
    // sl is the string which is converted to lowercase 
    string sl = "Jatin Goyal"; 
  
    // using transform() function and ::tolower in STL 
    transform(sl.begin(), sl.end(), sl.begin(), ::tolower); 
    cout << sl << endl; 
  
    return 0; 
} 