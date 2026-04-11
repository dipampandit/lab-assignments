// Implement Quick Sort

#include <stdio.h>

int partition(int arr[], int low, int high) {
    int pivot = arr[(low + high) / 2];
    int i = low, j = high;

    while (i <= j) {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;

        if (i <= j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    return i;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int index = partition(arr, low, high);
        quickSort(arr, low, index - 1);
        quickSort(arr, index, high);
    }
}

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    quickSort(arr, 0, n - 1);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}