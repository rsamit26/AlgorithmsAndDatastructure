#include<iostream>
using namespace std;

// Swap two numbers
void swap(int *xp, int *yp){
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}
// Selection sort algorithm
void selectionSort(int arr[], int n){
  int minSoFar;
  for(int i=0; i<n; i++){
    minSoFar = i;
    for(int j = i+1; j<n; j++){
      if(arr[minSoFar] > arr[j]){
        minSoFar = j;
      }
    }
    if(minSoFar!= i){
      swap(&arr[i], &arr[minSoFar]);
    }
  }
}

// Traversing the array
void printArray(int arr[], int size){
  for(int i = 0; i < size; i++){
    cout << arr[i] << " ";
  }
  cout << " " << endl;
}

// main function
int main(){
  int arr[] = {10,9,8,7,6,5,4,3,2,1};
  int n = sizeof(arr)/sizeof(arr[0]);
  selectionSort(arr,n);
  printf("Sorted Array using bubble sort is ");
  printArray(arr, n);
  return 0;
}
