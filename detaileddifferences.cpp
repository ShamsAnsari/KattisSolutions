#include <iostream>
#include <string>
using namespace std;
int main()
{
     int  T;
     cin >> T;
     cin.ignore();
     while (T--) {

          string s1;
          string s2;
          getline(cin, s1);
          getline(cin, s2);

          cout << s1 << endl << s2 << endl;
          
          for (int i = 0; i < s1.length(); i++) {
               if (s1[i] == s2[i])
                    cout << ".";
               else
                    cout << "*";
          }

          cout << endl << endl;
          
     }
}

