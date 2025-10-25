// Recursive Merge Sort

#include <stdio.h>

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSortRecursive(int arr[], int l, int r, int n) {
    if (l >= r) return;

    int m = l + (r - l) / 2;
    mergeSortRecursive(arr, l, m, n);
    mergeSortRecursive(arr, m + 1, r, n);
    merge(arr, l, m, r);

    printf("After merging (%d,%d): ", l, r);
    printArray(arr, n);
}

int main() {
    int arr[] = {9, 5, 1, 4, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, n);

    mergeSortRecursive(arr, 0, n - 1, n);

    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
