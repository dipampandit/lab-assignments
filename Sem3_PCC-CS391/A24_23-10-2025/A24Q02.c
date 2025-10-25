// Recursive Insertion Sort

#include <stdio.h>

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void insertionSortRecursive(int arr[], int n, int step) {
    if (n <= 1)
        return;

    insertionSortRecursive(arr, n - 1, step + 1);

    int last = arr[n - 1];
    int j = n - 2;

    while (j >= 0 && arr[j] > last) {
        arr[j + 1] = arr[j];
        j--;
    }
    arr[j + 1] = last;

    printf("After inserting element %d: ", n);
    printArray(arr, n);
}

int main() {
    int arr[] = {9, 5, 1, 4, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, n);

    insertionSortRecursive(arr, n, 1);

    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
