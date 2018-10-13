#include<iostream>
using namespace std;
void swap(int *xp, int *yp){
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

void bubbleSort(int arr[], int n){
  for(int i =0; i< n-1; i++){
    for(int j = 0; j <n-i-1; j++){
      if (arr[j] > arr[j+1]){
        swap(&arr[j], &arr[j+1]);
      }
    }
  }
}

void printArray(int arr[], int size){
  for(int i = 0; i < size; i++){
    cout << arr[i] << " ";
  }
  cout << " " << endl;
}

int main(){
  int arr[] = {2,1,3,5};
  int n = sizeof(arr)/sizeof(arr[0]);
  bubbleSort(arr,n);
  printf("Sorted Array using bubble sort is ");
  printArray(arr, n);
  return 0;
}
