// Recursive Bubble Sort

#include <stdio.h>

void bubbleSortRecursive(int arr[], int n) {
    if (n == 1)
        return;

    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    bubbleSortRecursive(arr, n - 1);
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSortRecursive(arr, n);

    printf("Sorted array (Recursive Bubble): ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
