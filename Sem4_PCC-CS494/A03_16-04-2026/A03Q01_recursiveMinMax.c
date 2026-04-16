// Find minimum and maximum element using divide and conquer (recursive function call) method.

#include <stdio.h>

struct MinMax {
    int min;
    int max;
};

struct MinMax findMinMax(int arr[], int low, int high) {
    struct MinMax result, left, right;

    // only one element present condition
    if (low == high) {
        result.min = arr[low];
        result.max = arr[low];
        return result;
    }

    // only two elements present condition
    if (high == low + 1) {
        if (arr[low] < arr[high]) {
            result.min = arr[low];
            result.max = arr[high];
        }
        else {
            result.min = arr[high];
            result.max = arr[low];
        }
        return result;
    }

    int mid = (low + high) / 2;
    left = findMinMax(arr, low, mid);
    right = findMinMax(arr, mid + 1, high);

    if (left.min < right.min)
        result.min = left.min;
    else
        result.min = right.min;

    if (left.max > right.max)
        result.max = left.max;
    else
        result.max = right.max;

    return result;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    struct MinMax result = findMinMax(arr, 0, n - 1);
    printf("Minimum: %d\n", result.min);
    printf("Maximum: %d", result.max);

    return 0;
}