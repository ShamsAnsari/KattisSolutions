
#include <iostream>
#include <iomanip>

using namespace std;


int main()
{
     const double PI = 3.141592653589793238463;
     double r;
     double m, c;
     while (1) {
          cin >> r >> m >> c;
          if (!(r && m && c))
               break;

          double realArea = PI * r * r;
          double estimateArea = c / m * 4 * r * r;
          
          cout << fixed << setprecision(6) << realArea << " " << estimateArea << endl;
     }
}

