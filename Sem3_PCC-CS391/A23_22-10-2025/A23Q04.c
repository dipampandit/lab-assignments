// Recursive Selection Sort

#include <stdio.h>

void selectionSortRecursive(int arr[], int n, int index) {
    if (index == n)
        return;

    int min_idx = index;
    for (int j = index + 1; j < n; j++) {
        if (arr[j] < arr[min_idx])
            min_idx = j;
    }

    if (min_idx != index) {
        int temp = arr[min_idx];
        arr[min_idx] = arr[index];
        arr[index] = temp;
    }

    selectionSortRecursive(arr, n, index + 1);
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSortRecursive(arr, n, 0);

    printf("Sorted array (Recursive Selection): ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
