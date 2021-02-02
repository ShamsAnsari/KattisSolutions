
#include <iostream>
using namespace std;

void printMatrix(int** matrix, int rows, int cols) {
     for (int i = 0; i < rows; i++) {
          for (int j = 0; j < cols; j++) {
               cout << matrix[i][j] << " ";
          }
          cout << endl;
     }
}

bool areNeighbors(int** matrix, int node1, int node2) {
     return matrix[node1][node2];
}
bool isTriangle(int** matrix, int size, int node) {
     for (int i = 0; i < size; i++) {
          if (i == node || !matrix[node][i]) {
               continue;
          }
          for (int j = i + 1; j < size; j++) {
               if (j == node || !matrix[node][j]) {
                    continue;
               }
               if (areNeighbors(matrix, i, j)) {
                    return true;
               }
          }
          
     }
     return false;
}
int main()
{
     while (1) {
          int n;
          cin >> n;
          if (n < 0)
               break;
          int** matrix = new int* [n];

          for (int i = 0; i < n; i++) {
               matrix[i] = new int[n];
               for (int j = 0; j < n; j++) {
                    cin >> matrix[i][j];
               }
          }
          
          for (int r = 0; r < n; r++) {
               if (!isTriangle(matrix, n, r)) {
                    cout << r << " ";
              }
          }
          cout << endl;
           
     }
}

