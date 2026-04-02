// Implement Merge Sort using Recursion

#include <stdio.h>

void merge(int arr[], int low, int mid, int high) {
    int tempArr[high - low + 1];
    int i = low, j = mid + 1, k = 0;

    while (i <= mid && j <= high) {
        if (arr[i] <= arr[j]) {
            tempArr[k++] = arr[i++];
        }
        else {
            tempArr[k++] = arr[j++];
        }
    }

    while (i <= mid) {
        tempArr[k++] = arr[i++];
    }

    while (j <= high) {
        tempArr[k++] = arr[j++];
    }

    for (int i = low; i <= high; i++) {
        arr[i] = tempArr[i - low];
    }
}

void mergeSort(int arr[], int low, int high) {
    if (low < high) {
        int mid = low + (high - low) / 2;

        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);

        merge(arr, low, mid, high);
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements of the array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    mergeSort(arr, 0, n - 1);

    printf("Sorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}