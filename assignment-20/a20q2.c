#include <stdio.h>
#include <stdlib.h>

void insertionSort(float *arr, int n) {
    int i, j;
    float key;
    for(i = 1; i < n; i++) {
        key = *(arr + i);
        j = i - 1;
        while(j >= 0 && *(arr + j) > key) {
            *(arr + j + 1) = *(arr + j);
            j--;
        }
        *(arr + j + 1) = key;
    }
}

int main(void) {
    float *arr = NULL;
    int n = 0, choice;
    float num;

    do {
        printf("Enter a number: ");
        scanf("%f", &num);
        
        // dynamic memory allocation for float
        arr = (float *)realloc(arr, (n + 1) * sizeof(float));
        *(arr + n) = num;
        n++;

        // sort after every insertion
        insertionSort(arr, n);

        printf("Current array: ");
        for(int i = 0; i < n; i++) {
            printf("%.2f ", *(arr + i)); // printing floats
        }
        printf("\n");

        printf("Do you want to continue? (1 for Yes / 0 for No): ");
        scanf("%d", &choice);
    } while(choice == 1);

    free(arr);
    return 0;
}
