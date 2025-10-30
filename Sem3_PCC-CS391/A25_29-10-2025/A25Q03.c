// Iterative Heap Sort

#include <stdio.h>

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

void heapifyIterative(int arr[], int n, int i, int total) {
    while (1) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < n && arr[l] > arr[largest])
            largest = l;
        if (r < n && arr[r] > arr[largest])
            largest = r;

        if (largest != i) {
            int temp = arr[i]; arr[i] = arr[largest]; arr[largest] = temp;
            printArray(arr, total);
            i = largest;
        } else break;
    }
}

void heapSortIterative(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapifyIterative(arr, n, i, n);

    for (int i = n - 1; i >= 0; i--) {
        int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
        printArray(arr, n);
        heapifyIterative(arr, i, 0, n);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Original array:\n");
    printArray(arr, n);
    heapSortIterative(arr, n);
    printf("Sorted array:\n");
    printArray(arr, n);
    return 0;
}
