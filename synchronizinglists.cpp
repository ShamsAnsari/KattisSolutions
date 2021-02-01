
#include <iostream>
#include <algorithm>

using namespace std;

int getIndex(int* arr, int size, int num) {
     for (int i = 0; i < size; i++) {
          if (arr[i] == num) {
               return i;
          }
     }

     return -1;
}
int main()
{
     while (1) {
          int T;
          cin >> T;
          if (!T)
               break;
          int* arr1 = new int[T];
          int* arr2 = new int[T];
          int* arr1Sorted = new int[T];
          int* arr2Sorted = new int[T];
          int* finalArr = new int[T];

          for (int i = 0; i < T; i++) {
               cin >> arr1[i];
               arr1Sorted[i] = arr1[i];
          }

          for (int i = 0; i < T; i++) {
               cin >> arr2[i];
               arr2Sorted[i] = arr2[i];
          }

          sort(arr1Sorted, arr1Sorted + T);
          sort(arr2Sorted, arr2Sorted + T);
          
          for (int i = 0; i < T; i++) {
               finalArr[i] = arr2Sorted[getIndex(arr1Sorted, T, arr1[i])];
               cout << finalArr[i] << endl;
          }
          cout << endl;

     }

}

